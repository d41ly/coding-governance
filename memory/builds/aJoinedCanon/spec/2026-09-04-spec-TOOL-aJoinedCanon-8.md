# TOOL-aJoinedCanon-8 — a unit declares its sibling edges and its external preconditions

**Status:** CLOSED · rev-5 · 2026-09-06 · node a · Tier-2 · base 750ca0ca · streams tooling · order 8 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aJoinedCanon-1-acceptance-ledger.md](../build/2026-09-06-build-TOOL-aJoinedCanon-1-acceptance-ledger.md) | journal | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

Almost every spec has siblings and none of them says what it takes from one or hands to one. Give
§3 a declared `### Edges` block over two verbs, and a dated check-12 arm that joins both ends of
every edge whose far end the check actually grades, so a handoff into a unit that never accepted it
reds instead of landing. Where the far end is outside that population — a Tier-1 sibling, a
grandfathered spec, the other half of a partial staging — the arm is silent and says so, because
absence from the graded set is a different answer from disagreement inside it.

## 2. Scope (IN)

- **S1** — the `### Edges` block, its two verbs and its payload rule, stated in
  `tools/memory-tree/SPEC-TEMPLATE.template.md` inside the skeleton's §3 body and in the prose
  section above the skeleton. Observed by AC6 and AC14. AC9 is NOT an observer of this item: it
  compares the pair's bytes and is equally green when neither half moved.
- **S2** — `memory/TEMPLATE-SPEC.md` re-rendered from that template with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, never hand-edited. Observed by AC9
  for the render and by AC14 for the text the render must carry.
- **S3** — a new cutoff key `SPEC_EDGES_CUTOFF`, declared in `.memory-tree.conf` beside its siblings,
  preset blank in `tools/memory-tree/check-memory-hygiene.sh` beside the `SPEC10_EVIDENCE_CUTOFF=""`
  preset whose trailing comment reads `blank = never required`, and shipped blank in
  `tools/memory-tree/.memory-tree.conf.example`. Blank means off, which is `STREAMS_CUTOFF`
  semantics and not `SPEC10_CUTOFF`'s forward resolution. Both conf carriers, per build rule 3: a
  key in one and not the other gives an adopter a dead arm reading as armed. Observed by AC7 for
  the repo's own conf and by AC15 for the shipped example, which is the adopter's copy and the one
  no criterion reached before rev-4.
- **S4** — the SHAPE arm: a branch in check 12's awk that reds a Tier-2 spec at or after the cutoff
  whose §3 carries no `### Edges` block, and reds a bullet inside that block whose head is neither
  verb. It reads ONE file and joins nothing, so it is the only arm here that stays live under
  `--staged`, where it is the committer's own file it grades. **The branch sits OUTSIDE every other
  cutoff guard on that awk path, on its own `-v edgecut=` binding, and tests `SPEC_EDGES_CUTOFF`
  and nothing else**, so its population
  is its own key rather than an intersection with `SPEC_WITNESS_CUTOFF` or any sibling's; an arm
  nested inside a neighbour's guard reads as armed in an adopter conf that arms only this key and
  never executes. Observed by AC1, AC2 and AC12.
- **S5** — the RECIPROCITY arm: a `hands-off` naming a sibling that declares no matching
  `consumes-from` back reds, and so does the mirror case. Graded only where the sibling is IN the
  graded population, per S14. Observed by AC3 and AC13.
- **S6** — the ORDER arm: a `consumes-from` whose target declares a greater `order` reds, and a
  `hands-off` whose target declares a smaller one reds. Graded only where both headers carry a
  conforming verb AND the target is in the graded population, per S14. Observed by AC4 and AC13.
- **S7** — the EXTERNAL-PAYLOAD arm: a bullet whose payload is `external` and whose prose backticks
  an id in this build's roster reds and names the verb it should have used. It reads the sibling
  population to know what the roster holds, so it is a join like S5 and S6 and is held with them by
  S13. Observed by AC5.
- **S8** — the zero-population announcement, modelled on the §10 evidence arm's, whose notice opens
  `memory-hygiene: the §10 reuse-evidence arm graded NO spec` and is itself guarded to full mode.
  Under the cutoff §8 resolved on, this is load-bearing rather than a nicety: the arm grades no
  tracked spec on day one, so the notice is the only thing separating its silence from coverage.
  Observed by AC8.
- **S9** — red and green fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`, in this
  unit's block under the build README's `tFixture-(80 + 10N)` allocation: `tFixture-160` upward.
  Every red is OBSERVED before the arm lands. The fixtures are the ENTIRE graded population at
  adoption, because §8 resolved the cutoff strictly ahead of every live spec filename date: no
  tracked spec is back-filled, this build's own eleven included. Observed by AC1 through AC8 and by
  AC12 and AC13.
- **S10** — the `ARMS_FLOORS` half of the declaration bookkeeping: the pair re-measured for
  `tools/memory-tree/check-memory-hygiene.sh` with `python3 tools/memory-tree/check-arms.py
  --report`, never typed. Observed by AC11.
- **S10b** — the VERSION half, split out of S10 at rev-4 because AC11 was never its observer:
  `KIT_MEMORY_TREE_VERSION` advanced and the `gov:kit memory-tree@` marker moved in every carrier,
  the set derived with `grep -rl` at build time and never counted here. The backlog row
  `TOOL-dSettledRoster-4` records a remediation that named three carriers when more existed, which
  is the whole reason the set is derived rather than written down — including in this bullet.
  Observed by AC16.
- **S11** — the check-12 paragraph in `tools/memory-tree/HYGIENE.template.md` gains the two
  sentences its sibling ratchets each get, and the arm's own header states what it does not check.
  Observed by AC9 for the pair's parity and by AC14 for the sentences themselves.
- **S12** — this spec's own §3 carries the block in the shape S1 proposes, so the first instance is
  in the tree on the day the rule lands. Observed by AC6.
- **S13** — the THREE JOIN ARMS (S5, S6, S7) are HELD under `--staged`, and say so. Their input is
  `c12_sel`, which the selection loop narrows with `in_scope "$f" || continue` — the line whose own
  comment reads `no-op in full mode; decides the WHOLE selection under --staged`. Under a partial
  staging one end of an edge is simply absent, so a join run there grades a truncated corpus. The
  hold is the shape check 23 already ships: a `[ "$STAGED" = 1 ]` branch printing an announce line
  in the wording of `memory-hygiene: check 23 HELD under --staged`, and the arms themselves behind
  the `[ "$STAGED" = 0 ]` gate beside it. The push boundary is where the joins bind. Observed by
  AC12.
- **S14** — MEMBERSHIP BEFORE AGREEMENT: an edge whose target id has no spec in the graded
  population is SILENT, never red. The population is what the pass registered, so a Tier-1 sibling —
  `next`-ed at `if (hdr ~ /Tier-1/) next` before it records anything — is absent by construction,
  and so is any target the cutoff grandfathered. Absence from the population and disagreement inside
  it are different answers and the arm gives different ones. This is what makes a correct Tier-2 to
  Tier-1 edge quiet rather than a red on honest work, and §3 records the resulting gap as skipped by
  a named test rather than as an unenforceable hope. Observed by AC13.
- **S15** — `memory/guides/SESSION-KICKOFF.md` is re-stamped: `last-audit` moves to a fresh
  `<ISO datetime> @ <sha>` per that manifest's own stamping rule, which this spec does not restate.
  THREE of this unit's write-set paths are `watch:` pathspecs of that manifest, and the third is the
  one a per-spec sweep misses: `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`
  are named on the `watch:` line outright, and `memory/guides/BUILD-METHOD.md` arrives through
  S10b — `PAIRS` in `tools/memory-tree/kit-dogfood-parity.test.sh` binds it to
  `BUILD-METHOD.template.md` and `render_doc` copies the whole file including its line-1
  `gov:kit memory-tree@` marker, so advancing the constant re-renders a watched file this unit never
  otherwise opens. Check C5 of `skills/session-kickoff/manifest-check.sh`, `no unaudited watch
  drift`, is TOPOLOGICAL: it reds when the newest watch-touching commit is not an ancestor of the
  newest commit that changed the `last-audit` value, whatever the body says. `last-body-change` does
  NOT move and §B gains no delta line — this unit changes no gate command, entrypoint, layout
  convention or front-loaded claim of that file, and the charter's rule is "no delta → no touch".
  Not an edge and not a handoff: every unit that edits a watched path re-stamps at its own landing,
  so units 1 and 2 carrying the same obligation hand this unit nothing and take nothing from it.
  Observed by AC17.

## 3. Non-goals (OUT)

- **No new generated region in the build README.** §4 Alternatives rejected states the reason and
  names the follow-up. `gen_build_index.py` is not edited by this unit.
- **No retrofit.** No landed spec is edited and none goes red. The cutoff is what carries the corpus,
  and build rule 3 is the reason.
- **No semantic check.** Nothing here grades whether the sibling's scope actually covers the handed
  work. That is what a reviewer reads, and §4 says so where the arm is written.
- **Not §6's preconditions.** What one criterion needs before it can be observed is
  `TOOL-aJoinedCanon-5`. What the whole unit takes from outside itself is this one. Both are
  answers to finding 27's shape and they are cut at the criterion boundary.
- **Not the §2-to-§6 join.** Scope items naming their criteria are `TOOL-aJoinedCanon-3`.
- **Tier-1 is not graded, and an edge INTO one is SKIPPED by a named test.** A Tier-1 spec may have
  no §3 at all under the light profile, so an arm demanding a block inside it would demand a section
  the profile exempts. That leaves a Tier-1 unit's own edges undeclared, and it leaves the reciprocal
  side of an edge INTO a Tier-1 unit with nothing to match. The residual is a SILENCE, not a red:
  S14's membership test is what produces it, AC13 is what observes it, and this build's roster is why
  it had to be built rather than noted — four of eleven units are Tier-1, so the first instance of
  the grammar in the tree is an edge into one. An earlier rev of this bullet called that case
  "unenforceable" while the arm as specced would have redded it, which is a gate whose header
  describes a behaviour it does not have.

### Edges

*Written in the shape S1 proposes. It is not graded — this spec predates the cutoff S3 declares.*

- **consumes-from** `TOOL-aJoinedCanon-7` — §7's declared shape for naming a gate leg and an arm's
  home. This spec's §7 is written to what that unit is expected to require, and owes a rev if it
  lands different.
- **hands-off** `TOOL-aJoinedCanon-10` — `SPEC_EDGES_CUTOFF` is one more declared cutoff key, and
  what unit 10 owes it is nothing but knowing it exists: that unit's S1 DELETES the cutoff count
  from the sentence naming the declared keys and puts no other count in its place, so a new key
  arriving at order 8 leaves no number at order 10 to update. Unit 10's rev-3 DOES declare the
  reciprocal — a `consumes-from` `TOOL-aJoinedCanon-8` bullet in its own `### Edges` block, naming
  the key's existence as the whole of what it accepts. The pair is still silent, on the other
  ground: unit 10 is Tier-1, so it is `next`-ed at `if (hdr ~ /Tier-1/) next` before the pass
  registers it and it is outside the population S14 tests membership against. The first live
  instance of the grammar is also the first live instance of the skip, and the skip survives the
  reciprocal existing — which is the point, because reciprocity is not what produces the silence.
  Two earlier revs of this bullet were wrong about unit 10 in opposite directions: rev-2 claimed the
  sentence it corrects "must count it", and rev-3 claimed it carries no `### Edges` block.
- **consumes-from** external — owner scope approval on §8's fork, SATISFIED 2026-09-05: the cutoff
  sits strictly ahead of every live spec filename date. S9 and AC7 are written to that answer, so the
  back-fill this edge used to hang on is refused rather than pending.

## 4. Design

### The evidence

450 of 479 specs (94%) sit in multi-spec build folders. The
template's only cross-unit field is the permitted `order <n>`, carried by 159 of 479. Those are the
research record's post-skeptic figures under finding A4, quoted as the record's, and they are the
only two numbers this section holds. An earlier rev added a third — "60 of the 89 folders holding a
spec" — inside the same attribution: A4 does not carry it, and it does not reproduce live either.
The live corpus is DERIVED rather than restated: count it with
`git ls-files 'memory/builds/*/spec/*.md'`, group by the folder segment for the multi-spec share,
and `git grep -lE '^\*\*Status:\*\*.*· order [0-9]'` over the same set for the `order` share. Every
earlier rev pinned a live re-measurement beside the record's figures, and the pin was stale within a
day because this build's own specs land into the population it counts.

`order` expresses sequence and never an edge, and the confirmed cross-unit defects are edge failures.
`dRetiredFork` H4 hands 39 literal sites in `tools/check-wiring.sh` to `TOOL-dRetiredFork-13`, whose
own S1 population is the shipped test and selftest files and whose §3 excludes everything else. The
outward-facing half is finding 27: seven confirmed amendments where a criterion rested on something
the unit does not build, four of them in one spec. That spec is `dScaffoldedMirror-8`, whose AC1,
AC2, AC3 and AC5 all rest on `--probe --write` — AC1 and AC5 name the verb, AC2 runs "the same
command" and AC3 reads the ledger AC2's run writes — and whose §9 rev-1 status line records the owner
cutting `--probe --write` from the unit. Four criteria died in place and nothing in the format had
asked what they rested on. Two of the four never spell the verb, which is why the join has to be
declared rather than grepped.

Three separate reviews have already proposed this arm as a left-shift, which is the strongest
argument for building it once rather than re-deriving it per build. `dRetiredFork` round 1 proposes a
cross-spec handoff join at H4 and reaches for it again at H8, whose left-shift says in terms that the
same join proposed at H4 covers it. `dFoldedVerdict` round 1 proposes it in H4's own left-shift
paragraph, the one opening `A cross-spec arm, and this build is the argument for building it`, and
reaches for that paragraph twice more in the same record. An earlier rev cited it as `:110`, which is
a blank line.

### Data model

A `### Edges` sub-head inside `## 3. Non-goals (OUT)`, holding one bullet per edge or the single
word `none`.

```markdown
### Edges

- **consumes-from** `<unit-id>` — what this unit takes, and what breaks without it
- **hands-off** `<unit-id>` — what this unit leaves for that unit to do
- **consumes-from** external — the precondition this unit does not build
- **hands-off** external — the work this unit defers outside this build
```

Two verbs, one payload rule. The payload is either a backticked unit id whose spec sits under the
same `builds/<slug>/spec/` prefix, or the bare token `external` followed by prose. A third verb was
drafted and cut: `depends-on` and `consumes-from` answer one question, and finding 27's case is an
inbound edge whose far end happens to be outside the build, which the payload rule already expresses.

The marker bytes are ASCII on purpose. The acceptance-witness arm's own comment in
`check-memory-hygiene.sh` records a multibyte em dash reaching this file as mojibake,
because those bytes cross the writing tool, the shell and the awk regex parser and only the last has
an opinion about encoding.

### Where it lives

Line numbers are not cited here: units 1, 3, 4 and 6 all edit `check-memory-hygiene.sh` before this
one, so every number in this section would be stale by the time it is read. Each site is named by its
own text, per build rule 6.

**And the SHAPE of that file is a lower-`order` sibling's to change too, so this placement argument
is re-verified at build time rather than assumed.** Unit 4 HOISTS the acceptance-witness accumulator
out of the `wcut` guard, and units 1 and 3 each add an arm and a `-v` binding to the same check-12
invocation. Every structural claim below — which guard encloses what, where the END block routes,
what the post-pass switches on — is asserted against the file as those four leave it, and a builder
who finds it different amends this section rather than the code. Round 2's H10 is the class: a
design argument verified against a structure that no longer exists at build time.

The shape arm is a branch in the batched awk that check 12 runs over `c12_sel`, placed BELOW the
`if (hdr ~ /Tier-1/) next` cut beside the section canon and the empty-body walk, because it is Tier-2
only. That position is OUTSIDE every cutoff guard on the path: the cut and the two walks below it sit
at the top level of the record body, the `scut`, `wcut` and `fcut` blocks all close above it, and the
`ecut` §10-evidence block below it is a sibling rather than an enclosure.
**The binding is `-v edgecut=`, and the name is claimed rather than assumed.** Check 12's awk opens
with exactly `-v canon -v canon10 -v cut10 -v mroot -v discalt -v scut -v wcut -v fcut -v ecut`
today, and the siblings adding to that same invocation take `revscopecut` (unit 1), `jcut` (unit 3),
`mcut` and `fmcut` (unit 4), `rcut` and `rrows` (unit 9) and `bcut` (unit 11); `grep -rn edgecut`
over the tree returns nothing. It is spelled out rather than shortened to `ecut`-adjacent bytes on
purpose — `ecut` is `SPEC10_EVIDENCE_CUTOFF` and a one-character neighbour in a nine-name `-v` list
is a rebind nobody reads. A second `-v` of one name is last-wins for the whole program, which is
round 3's B1 and the reason build rule 6 exists; `TOOL-aJoinedCanon-3` §4's namespace survey owes a
row for this name, and until it carries one the taken list there is incomplete.
The branch therefore carries its own `SPEC_EDGES_CUTOFF` liveness test and inherits no neighbour's,
which is what keeps its population from becoming an intersection of two keys — the defect round 2
recorded as B1 against a sibling, where an arm anchored on a print INSIDE the `wcut` guard would
have graded only specs past both cutoffs while its own key read as armed. AC1 observes the
independence in the only way that can fail: a scratch conf arming this key ALONE. The arm reports
inline like the other per-file findings in that pass, so it adds no `fail` branch, and it reads
exactly one file.

The three join arms accumulate in that same pass and emit in its END block, tagged the way the
canon-diff arm tags its excerpt request with a sentinel record. **The tag is `\003`, and it is a
claimed name for the same reason the `-v` binding is.** `\001` is taken: the canon-diff arm emits
`print "\001\t" f` and the `case "$bad12_raw" in` post-pass already matches `*$'\001'*`, so a second
emitter of that byte is not a second class, it is the excerpt path consuming these records.
`TOOL-aJoinedCanon-11` has claimed `\002`. One byte carries all three join classes with the class
name as the first tab field; three bytes would be three routes to write and nothing to buy. The
`case "$bad12_raw" in`
post-pass below the awk learns the tag and routes each class into its own accumulator, and three
`fail 12` calls report them — the shape check 23 already uses for its three ledger-join classes.
Each of the three then owes an armed fixture signature, and `ARMS_FLOORS` for this gate is
re-measured rather than typed: its value moves under units 3, 4 and 6 as well, so S10's `--report`
run is the only thing that may write it.

**The join is closed over `c12_sel`, and `c12_sel` is the staged set under `--staged`.** The
selection loop's own comment says it — `no-op in full mode; decides the WHOLE selection under
--staged` — and the pre-commit hook runs the check that way whenever `memory/**` is staged. A
developer committing one spec of a correctly declared pair would therefore see the other end reported
missing, which is a red on honest work and the reason S13 holds the three joins under `--staged` with
an announce line. The per-file shape arm stays live there, because a truncated corpus cannot change
its answer about the one file it reads.

**Absence is not disagreement.** Before either join compares, S14 asks whether the target id is in
the population the pass registered; if it is not, the arm is silent. Two populations produce that
absence and both are legitimate: a Tier-1 sibling, `next`-ed before it records anything, and a spec
the cutoff grandfathered. Without the membership test the two joins cannot tell "this sibling was
never graded" from "this sibling refused the edge", and they answer the second when the truth is the
first.

Per selected spec the pass keeps four values it can read from what it already has in memory: the
build slug from the path, the unit id from the `# ` H1's first token, the `order` integer from the
status header, and the edge bullets. Nothing re-reads a file.

A header carrying something order-shaped that does not conform is treated as unordered here, and that
is safe rather than silent: `gen_build_index.py` REFUSES such a value in `_parse_order`, and hygiene
check 9 runs `gen_build_index.py --check`, so the tree cannot carry one past the bar.

### What the arms do not check

Stated in the arm's own header, per charter §7, and there are three things rather than one.

Reciprocity proves that the other unit's author WROTE the matching line, never that their scope
covers the work. A rubber-stamped reciprocal passes. The arm is worth having anyway, because writing
the line requires reading the handoff, and H4's defect is that nobody did.

The joins do not run at all under `--staged` (S13), so pre-commit grades shape and nothing else. The
header says which run binds them, in the words check 23 uses, because a hold that does not announce
itself is a skip that looks like a pass.

The joins grade only edges whose far end is in the population (S14). An edge into a Tier-1 sibling,
or into a spec the cutoff grandfathered, is not checked and is not claimed to be. That is the whole
of the Tier-1 residual §3 records, and it is a declared blind spot rather than a silent one.

### Alternatives rejected

- **A new §11 section.** It needs a third section canon and a `want` selection over two cutoffs in a
  check that today picks between two. A `###` sub-head under §3 is ungraded structure the template
  already sanctions, costs no canon change, and cannot red a grandfathered spec. Measured: outside
  this build no tracked spec carries a `### Edges` sub-head, and exactly one spec in the whole tree
  carries any `###` inside §3 at all — `cTracedPromise-1`, whose sub-head is prose. So the name is
  free. The two `### Edges` blocks that DO exist are this spec's own and unit 10's reciprocal, both
  written to the grammar S1 proposes; an earlier rev said "no tracked spec carries" one and unit
  10's rev-3 falsified it the same day, which is why the exclusion is now stated rather than the
  bare zero.
- **A generated `build-edges` region per unit.** The name is already taken at build granularity —
  the `"build-edges"` row of `GEN_REGIONS` and `def render_edges(build: dict)` in
  `tools/memory-tree/gen_build_index.py` render parent and child BUILDS from the README's authored
  `parents:` key. Cited by symbol: an earlier rev pinned `render_edges` at `:1013`, which is the
  closing `return` of the function above it. A unit-level twin would be a second region, a
  fourth marker pair in every build README, and a committed artifact whose only consumer is a check
  in the same language. Charter §12 says to derive that live and commit nothing. The arm reads the
  specs directly. If a reader later wants the graph rendered, it is a follow-up unit and the field
  is already the single source it would render from.
- **Extending the unattended kit's order gate.** `tools/unattended/unattended.sh` already resolves
  sibling units and blocks a `--dispatch` that runs ahead of its declared order — the block reading
  `order_verb_of` and `unit_ids_of` and ending in the `fail 49` whose message opens `--dispatch
  declares a build pass out of the build's own declared order`. Cited by symbol and by message text:
  an earlier rev pinned it as `:4611-4653`, and a line range into a live driver this unit does not
  own is stale on someone else's commit. It is live prior art and it is deliberately not
  extended: it
  grades SEQUENCE rather than an edge, it runs only on unattended runs while the hygiene gate runs on
  every bar, and it is a different copy-installed kit, which under charter §12 may not learn another
  kit's paths.
- **Requiring the block on both tiers.** §3 Non-goals states the residual this leaves.

### Migration

None. No landed spec is touched, and the cutoff decides the population. Rollback is one edit: blank
`SPEC_EDGES_CUTOFF` and every arm goes quiet, which is why the key takes blank-means-off semantics
rather than resolving forward.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | the block, in the §3 skeleton body and the prose above it |
| `memory/TEMPLATE-SPEC.md` | re-rendered, never hand-edited |
| `tools/memory-tree/HYGIENE.template.md` | two sentences on the check-12 paragraph |
| `memory/HYGIENE.md` | re-rendered, never hand-edited |
| `tools/memory-tree/check-memory-hygiene.sh` | the preset, the `-v` binding, four arms, the membership test, the `--staged` hold and its announce line, three fails |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the fixtures, in the `tFixture-160` block, including a `--staged` scratch-tree case beside the existing one |
| `.memory-tree.conf` | the cutoff key and the re-measured `ARMS_FLOORS` |
| `tools/memory-tree/.memory-tree.conf.example` | the same key, blank, with its adopter comment |
| `memory/guides/BUILD-METHOD.md` | its line-1 marker only, re-rendered by the version bump; no prose change (S15) |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp only; no body delta, `last-body-change` unmoved (S15) |
| every `gov:kit memory-tree@` marker carrier | `KIT_MEMORY_TREE_VERSION` advanced and the marker moved; the set is DERIVED below, never listed here |

The version row is S10b and its observer is AC16. Derive the carrier set with
`grep -rl 'gov:kit memory-tree@'` rather than from a remediation message, which
`TOOL-dSettledRoster-4` records naming fewer carriers than existed. This unit changes the engine's
verdicts, so `verdict epoch (kit version dates the engine)` is the leg that reds on an unmoved
constant; `kit version markers` reds on a carrier left behind while its siblings moved. Two legs,
two different failures, and rev-3 declared the obligation in this table with no criterion behind it.
That derived set is also how a third `watch:` path enters a write set that never opens it by name:
`memory/guides/BUILD-METHOD.md` carries the marker and is bound to its template by `PAIRS` in
`kit-dogfood-parity.test.sh`, so the version bump re-renders it. S15 is the obligation that follows
and AC17 observes it.

## 5. Production-readiness checklist

- **security** — N/A. The arm reads tracked spec text the same pass already reads and writes nothing.
- **perf / scale** — no new file read and no second pass. The END-block arrays are bounded by the
  selected spec population, which `git ls-files 'memory/builds/*/spec/*.md' | wc -l` counts and no
  number here restates. The `memory hygiene` leg's cost is recorded per run in
  `<git-dir>/gate-ledger.tsv`; compare the row before and after rather than asserting the arm is free.
- **a11y** — N/A.
- **i18n** — N/A for language. The marker bytes are ASCII by decision, for the mojibake reason §4
  records.
- **error / empty / loading states** — the zero-population announcement is S8. At adoption this arm
  grades nothing, and a skip that looks like a pass is indistinguishable from coverage.
- **observability** — every join finding names BOTH ends, the file and the sibling id, because a
  message naming one end sends the reader to the document that is not wrong.
- **risks** — the two that would have redded correct work are now arms rather than notes: a partial
  staging truncates the corpus the joins close over (S13 holds them under `--staged`), and an edge
  whose far end is outside the graded population has no reciprocal to find (S14 makes it silent).
  Both were specced as behaviour before they were specced as risks, which is the direction that
  matters. What remains: a rubber-stamped reciprocal passes, as §4 says. The external-payload arm can
  false-positive on a bullet that backticks a sibling id as context, which is why AC10 runs the
  candidate predicate over the whole tree before it is wired. A cutoff set too early reds in-flight
  branches; §8 resolved that fork to the strictly-ahead date, which retires the risk and moves the
  whole day-one cost onto S8's zero-population notice. Naming a foreign build's id in prose already
  contributes to THAT build's roster, since `def rosters(root: str, tracked: list, m: str,
  families: set)` in `tools/memory-tree/gen_build_index.py` keys on the id's own slug component; the
  grammar adds no new instance of that because a joined edge names a sibling in this build only.
- **testing + left-shift gates** — S9. Each red is staged, observed, unstaged, per build rule 4.
- **migration / rollback** — §4 Migration.
- **user docs** — `memory/HYGIENE.md` item 12 and the template itself are what an author reads. This
  repo ships no `help/` tree.

## 6. Acceptance criteria

- **AC1** — When a Tier-2 fixture spec dated at or after `SPEC_EDGES_CUTOFF` carries a §3 with no
  `### Edges` block, `bash tools/memory-tree/check-memory-hygiene.sh` reds naming that file and the
  missing block — and it reds the same way in a scratch tree whose conf declares `SPEC_EDGES_CUTOFF`
  and BLANKS every other cutoff key the engine reads, which is what proves the branch carries its own
  liveness test rather than a neighbour's. Staged, observed RED, unstaged. The one-key-armed run is
  the arm that fails when the branch is nested inside another cutoff's guard; the fully-armed fixture
  conf is green either way, which is how round 2's B1 survived a sibling's whole criteria set.
- **AC2** — When a fixture's block carries a bullet whose head is neither `consumes-from` nor
  `hands-off`, the same command reds naming that bullet's label rather than the whole file.
- **AC3** — When fixture unit A declares `hands-off` `B` and B's spec declares no `consumes-from`
  `A`, a FULL `bash tools/memory-tree/check-memory-hygiene.sh` reds naming both files, and the
  mirror fixture reds the same way. Both fixtures are Tier-2, so S14's membership test admits them.
- **AC4** — When fixture A at `order 2` declares `consumes-from` a sibling at `order 7`, the same
  full run reds naming both orders; when neither header carries a conforming `order` verb, the same
  pair is silent.
- **AC5** — When a bullet reads `consumes-from external` and its prose backticks an id in the same
  build's roster, the check reds and names `consumes-from` as the verb it should have used.
- **AC6** — When the fixture build's specs each carry a conforming block, including this spec's own
  §3 block copied in as a fixture, `bash tools/memory-tree/check-memory-hygiene.sh` is green and no
  arm fires.
- **AC7** — When `SPEC_EDGES_CUTOFF` is blank, no arm fires and the run is green. And when it holds
  the strictly-ahead date §8 resolved on, `bash tools/memory-tree/check-memory-hygiene.sh` over the
  real tree is green with every tracked spec grandfathered, this build's own eleven included — the
  grandfather case is the LIVE CORPUS rather than one fixture, which is what that resolution made it.
  That green is read TOGETHER with the notice AC8 observes, never alone: a whole-corpus green with a
  graded population of zero and a whole-corpus green with a graded population of hundreds are the
  same byte, and the notice is the only thing that tells them apart. A green with no notice on it is
  a FAILED AC7, because it means the arm graded specs and said nothing about them.
- **AC8** — When no tracked spec reaches the cutoff, the full run prints the named zero-population
  notice on stdout, in the shape the §10 evidence arm's `graded NO spec` notice already uses.
- **AC9** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the template edit, it
  is green, and `git diff` shows `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md` changed only by
  the render.
- **AC10** — When the candidate predicate is run standalone over
  `git ls-files 'memory/builds/*/spec/*'` BEFORE it is wired, it prints its hits AND its
  near-misses, and the near-miss list is read for false positives rather than counted. Charter §7
  requires this, and it is the run that decides AC5's shape.
- **AC11** — When `python3 tools/memory-tree/check-arms.py --report` is run BEFORE and AFTER this
  diff, the `check-memory-hygiene.sh` row's branch and armed counts have each risen by three, and
  `--check` with the re-measured `ARMS_FLOORS` is green. Then the failing case, because green alone
  proves nothing here: `ARMS_FLOORS` is a SHRINK-ONLY floor, compared with `<`, so adding three
  branches and leaving the pin untouched passes `--check` unchanged. With the floor raised, delete
  one of the three arms' assertions from `check-memory-hygiene.test.sh`, observe `--check` RED
  naming `armed branch(es) against a floor of`, restore. That red is the only evidence that the
  re-measurement is load-bearing rather than decorative.
- **AC12** — When exactly ONE spec of a conforming edge pair is staged in the self-test scratch tree
  and `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs, the run does not red on that
  pair and prints the HELD announce line naming check 12, in the wording
  `memory-hygiene: check 23 HELD under --staged` already ships. The same run still reds the staged
  file's own missing `### Edges` block, which is what proves the shape arm stayed live rather than
  the whole check going quiet. The harness is the existing `--staged` block in
  `tools/memory-tree/check-memory-hygiene.test.sh`, the one whose comment reads
  ``--staged: `in_scope` is the ONLY thing deciding selection there`` — quoted with its backticks,
  because rev-3 quoted it without them and the string it named matches nothing in that file.
- **AC13** — When a Tier-2 fixture declares `hands-off` a Tier-1 sibling that carries no `### Edges`
  block, a FULL `bash tools/memory-tree/check-memory-hygiene.sh` is silent about that pair, and it is
  silent the same way for an edge naming a spec the cutoff grandfathered. Staged, observed GREEN
  against the version of the arm that lacks the membership test — that arm reds, which is the failing
  case this criterion exists to have seen.
- **AC14** — When the render has run, the AUTHOR-FACING TEXT is present in the rendered halves, not
  merely identical to its template. `grep -c 'consumes-from' memory/TEMPLATE-SPEC.md` returns at
  least 2 and `grep -c '### Edges' memory/TEMPLATE-SPEC.md` at least 1, against a pre-change count
  of 0 for both, measured today; `grep -c 'SPEC_EDGES_CUTOFF' memory/HYGIENE.md` returns at least 1
  against a pre-change 0. The failing case is the one AC9 cannot see: land the arm, skip the
  template edit, re-render — AC9 stays green because both halves still match, and AC14 reds. S1,
  S2 and S11 are the whole author-facing product of this unit under a cutoff that grades no live
  spec on day one, so a byte-compare is the wrong and only observer round 2 found five times.
- **AC15** — When the edit has landed, `grep -c '^SPEC_EDGES_CUTOFF=' tools/memory-tree/.memory-tree.conf.example`
  returns 1 against a pre-change count of 0, the value is blank, and the line carries an adopter
  comment saying blank means off. Deleting that line is the observed red. The example conf is the
  file an adopter reads and edits; a key present in this repo's `.memory-tree.conf` and absent from
  the shipped example is build rule 3's exact failure and nothing before rev-4 observed it.
- **AC16** — When the landing commit is in place, `bash tools/check-kit-versions.sh` and
  `bash tools/memory-tree/check-verdict-epoch.sh` both exit 0. The observed reds are two, because
  the legs fail on different things: revert `KIT_MEMORY_TREE_VERSION` alone with the engine changed
  and `verdict epoch (kit version dates the engine)` reds; move the constant in one carrier and not
  the rest and `kit version markers` reds. Both restored before the commit. This is S10b, split out
  of S10 because AC11 runs `check-arms.py` and reaches neither script.
- **AC17** — When `bash skills/session-kickoff/manifest-check.sh` runs on the landing commit it
  exits 0, and `memory/guides/SESSION-KICKOFF.md`'s `last-audit` names a sha at or after the newest
  commit touching a watched path in this write set. The failing case is the revert of S15 alone:
  keep the engine, conf and marker edits, restore the old stamp, and check C5 —
  `no unaudited watch drift` — reds naming those files as watched files changed with no re-stamp at
  or after the change. `last-body-change` is the SAME sha before and after, which is the half of the
  criterion that observes the "no delta → no touch" side of the rule rather than the re-stamp side.
  Graded on the landing commit and not under `--staged`: the staged leg runs C5s, which that
  script's own comment narrows because a blocking pre-commit cannot see a future follow-up stamp.

## 7. Gates

- `memory hygiene` · `memory-hygiene self-test`
- `kit/dogfood doc parity` · `kit version markers`
- `harness arms (fail branches armed or pinned)` · `verdict epoch (kit version dates the engine)`
- `spec tokens (a spec's own names resolve)` · `kickoff-manifest ratchet`

This unit adds no leg. The arm's home is check 12 inside `tools/memory-tree/check-memory-hygiene.sh`,
which the `memory hygiene` leg already runs. Its fixtures live in
`tools/memory-tree/check-memory-hygiene.test.sh`, run by `memory-hygiene self-test`, which is guarded
to `tools/memory-tree/` and so fires on this unit's own diff. `kit/dogfood doc parity` is what makes
the two template halves one edit and AC9 is what runs it — but the halves agreeing is not the text
being there, which is AC14's job. `kit version markers` reds if a `gov:kit memory-tree@` carrier is
left behind while its siblings moved, `verdict epoch (kit version dates the engine)` reds if the
constant sits still while the engine's verdicts change — which is exactly what this unit does to it —
and AC16 observes both, with a separate staged red for each because they fail on different things.
`harness arms (fail branches armed or pinned)` is what the three new `fail 12` branches move, and
AC11 observes the move against a deleted assertion rather than against a green. `spec tokens (a
spec's own names resolve)` grades this document's own leg names; every name in the list above was
checked against `tools/gate-legs.json` and resolves, and no script path stands in for one.
`kickoff-manifest ratchet` is `subject = repo` with NO guard in that manifest, verified there, so it
runs on every bar rather than only on a diff that touches the kickoff skill — three of this unit's
write-set paths are `watch:` pathspecs of `memory/guides/SESSION-KICKOFF.md`, and without S15 this
landing reds an unguarded leg on every subsequent bar. AC17 is the observed red.

One exemption, stated with its compensating check. S13 takes the three join arms off the pre-commit
`--staged` run entirely, so the only bar that grades them is the full `memory hygiene` leg, which
`.githooks/pre-push` runs at the push boundary. That is the same trade check 23 already makes and
for the same reason, and the compensating control is that the leg is unguarded in
`tools/gate-legs.json` — it fires on every full bar rather than only on a memory-tree diff, so no
push reaches shared `main` without the joins having run once. The announce line AC12 observes is
what keeps the pre-commit silence from reading as a pass.

## 8. Open questions

- **F1 — where the cutoff sits, and therefore whether this build's own eleven specs must carry the
  block.** Option A, strictly ahead of every spec filename date on every live branch, is the idiom
  `SPEC10_EVIDENCE_CUTOFF` records and it reds nobody, at the price that the arm grades zero specs on
  day one and its whole coverage is the fixtures. Option B, the landing date, is what
  `ACCEPTANCE_LEDGER_CUTOFF` chose so its first run would measure something real; here it means
  back-filling an `### Edges` block into all eleven of this build's specs, each a rev bump on a spec
  a sibling unit is mid-build against. RECOMMENDATION: option A. Build rule 3 says every template
  change is a dated cutoff and never a retrofit, and eleven concurrent rev bumps across a sequenced
  build is exactly the retrofit that rule exists to refuse. The zero-population announcement in S8 is
  what stops option A's silence being mistaken for coverage.

  RESOLVED (owner, 2026-09-05): option A — `SPEC_EDGES_CUTOFF` sits strictly ahead of every spec
  filename date on every live branch, and this build's own eleven specs back-fill nothing. Option B's
  text stays above as the record of what was weighed and why it lost. The two things this fork said
  it changed are changed: S9 now states the fixtures are the entire graded population at adoption,
  and AC7's grandfather case is the live corpus rather than a fixture. S8 stays, promoted from a
  nicety to the load-bearing thing that keeps day-one silence from reading as coverage.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §2 · §3 · §5 · §6 · folded the owner's ruling on F1: option A, the cutoff
  sits strictly ahead of every live spec filename date and nothing is back-filled. S9 gained the
  day-one population statement, S8 the load-bearing note, §3's external edge is marked satisfied,
  §5's cutoff risk is retired, and AC7's grandfather case moved from a fixture to the live corpus.
- rev-3 · 2026-09-05 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §10 · folded spec-audit round 1: B2, H6, M2,
  and the build's three consolidated rules. B2 — the three join arms close over `c12_sel`, which is
  the staged set under `--staged`, so S13 holds them there with check 23's announce line, §4 states
  the population constraint, §7 records the exemption with its compensating check, and AC12 observes
  a one-sided staging staying green. H6 — S14 makes an edge whose target is outside the graded
  population silent instead of red, §3's Tier-1 residual becomes a named skip rather than an
  unenforceable gap, §4 says absence is not disagreement, and AC13 observes it. M2 — the
  `hands-off TOOL-aJoinedCanon-10` bullet now says what unit 10 actually does, which is delete the
  count rather than update it. Build rules: S9 moves to the README-allocated `tFixture-160` block,
  every `check-memory-hygiene.sh` line pin in §4 and §10 becomes a text citation, S10's
  `ARMS_FLOORS` is derived rather than quoted, and S3 states both conf carriers explicitly.
- rev-4 · 2026-09-05 · §2 · §3 · §4 · §5 · §6 · §7 · folded spec-audit round 2. NAMED FINDINGS: M9 —
  the §3 `hands-off TOOL-aJoinedCanon-10` bullet said unit 10 carries no `### Edges` block, and unit
  10's rev-3 added one naming this unit; the bullet now rests on the reason that survives, which is
  that a Tier-1 spec is outside the graded population S14 tests. M10 — S10 claimed AC11 observed
  both the `ARMS_FLOORS` re-measure and the version bump; the version half is now S10b with AC16,
  and §4's file table gained the carrier row it lacked. L2 — `render_edges` is cited by its `def`
  line, not by `:1013`, which is the previous function's `return`. SWEPT CLASSES THAT HIT: B1, S4
  and §4 now state the branch sits outside every cutoff guard and AC1 arms this key alone; H1 and
  H2/H3/H5, AC14 grades the author-facing text the byte-compare cannot see and S1, S2 and S11 lose
  AC9 as their sole observer; H7, AC11 observes a shrink-only floor against a deleted assertion
  rather than against a green; H10, §4 names all four lower-`order` units that edit the engine and
  says the placement argument is re-verified at build time; M1/L1, the live corpus re-measurement,
  the `484 files` figure, the `### Edges` zero and S10's carrier count are all derived or dropped;
  M6, AC15 grades the shipped example conf; M7, AC7 must read the zero-population notice beside its
  green; plus one citation of its own finding — AC12 quoted the harness comment without its
  backticks and matched nothing. SWEPT AND CLEAN: H4 (every scope item carries a tag), H6 and M4
  (`--render`, `--check`, `--report` and all seven §7 leg names run or resolve against
  `tools/gate-legs.json`), H8, H9 (no `check-memory-hygiene.sh` line pin survives), M2, M3, M5
  (unit 6 does not touch the `check 23 HELD under --staged` line this unit copies), M8.
- rev-5 · 2026-09-05 · §2 · §4 · §6 · §7 · §10 · folded spec-audit round 3, the TERMINATING fold —
  H2, plus the eight build rules swept over this document. H2 — S15, AC17, two Files-touched rows
  and the `kickoff-manifest ratchet` leg carry the `last-audit` re-stamp this spec owed and named
  nowhere; the sweep found the finding UNDERSTATED for this unit, because a third `watch:` path,
  `memory/guides/BUILD-METHOD.md`, enters the write set through S10b's version bump via `PAIRS` in
  `kit-dogfood-parity.test.sh` rather than through any row the spec had written. RULE 6, twice, both
  the round-3 blocker's class in this document: the `-v` binding was introduced un-named and is now
  `edgecut`, checked free against the nine bound on that invocation today and against all seven
  names the siblings claim; and the END-block sentinel was described only as "the way the canon-diff
  arm tags" its `\001` record, which is the byte that arm's post-pass already routes, so the tag is
  now `\003` with `\002` recorded as unit 11's. RULE 8 and round 3's M3/M5 classes: the
  `unattended.sh:4611-4653` range in §4 and §10 became a symbol-and-message citation, and the
  `dFoldedVerdict` round 1 `:110` pin was verified to land on a BLANK line and became a text anchor
  on H4's left-shift paragraph. RULE 1: "60 of the 89 folders holding a spec" was attributed to
  finding A4, which does not carry it, and does not reproduce live either — dropped, the two figures
  A4 does carry kept. One over-claim corrected: `dScaffoldedMirror-8`'s AC2 and AC3 rest on
  `--probe --write` by reference rather than naming it. NOT FIXED HERE, and it is cross-unit by
  construction: `TOOL-aJoinedCanon-3` §4's namespace survey still lists no row for `edgecut`, which
  this document states where the name is claimed. SWEPT AND CLEAN: rules 2, 3, 4, 5 and 7 — the
  cutoff is declared in both confs, every arm names its staged red, the fixtures stay in the
  README-allocated `tFixture-160` block, and no literal a lower-`order` unit moves is pinned.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declaring a dependency edge between two sibling spec
units in one build"` returned the build-README region machinery as its nearest seams,
`add_spec_records_region` in `tools/memory-tree/gen_build_index.py` and `apply_region` in the
`build-readme-surface` dossier. That is the seam this unit deliberately does NOT extend, for the
reason §4 Alternatives rejected records. The seam it does extend is check 12's batched awk over
`c12_sel` in `tools/memory-tree/check-memory-hygiene.sh`, which the map does not index because it
holds no shell symbols. The recall probe found the live prior art the map could not:
`order_verb_of` and `unit_ids_of` in `tools/unattended/unattended.sh` already resolve sibling units
by their `order` verb and block a dispatch that runs ahead of them, which is sequence rather than an
edge, and it is a different kit on a different trigger. Cited by symbol here for the reason §4's
Alternatives entry gives.

Recall terms used: `spec unit sibling handoff order verb build roster cross-spec join hygiene check
12 cutoff edge`.
