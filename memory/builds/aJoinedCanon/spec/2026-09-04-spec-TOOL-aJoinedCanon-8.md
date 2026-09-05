# TOOL-aJoinedCanon-8 — a unit declares its sibling edges and its external preconditions

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 8 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

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
  section above the skeleton. Observed by AC6 and AC9.
- **S2** — `memory/TEMPLATE-SPEC.md` re-rendered from that template with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, never hand-edited. Observed by AC9.
- **S3** — a new cutoff key `SPEC_EDGES_CUTOFF`, declared in `.memory-tree.conf` beside its siblings,
  preset blank in `tools/memory-tree/check-memory-hygiene.sh` beside the `SPEC10_EVIDENCE_CUTOFF=""`
  preset whose trailing comment reads `blank = never required`, and shipped blank in
  `tools/memory-tree/.memory-tree.conf.example`. Blank means off, which is `STREAMS_CUTOFF`
  semantics and not `SPEC10_CUTOFF`'s forward resolution. Both conf carriers, per build rule 3: a
  key in one and not the other gives an adopter a dead arm reading as armed. Observed by AC7.
- **S4** — the SHAPE arm: a branch in check 12's awk that reds a Tier-2 spec at or after the cutoff
  whose §3 carries no `### Edges` block, and reds a bullet inside that block whose head is neither
  verb. It reads ONE file and joins nothing, so it is the only arm here that stays live under
  `--staged`, where it is the committer's own file it grades. Observed by AC1, AC2 and AC12.
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
- **S10** — the declaration bookkeeping: `ARMS_FLOORS` re-measured for
  `tools/memory-tree/check-memory-hygiene.sh` with `python tools/memory-tree/check-arms.py
  --report`, and `KIT_MEMORY_TREE_VERSION` bumped in every carrier of the marker, the set derived
  rather than counted. Measured today, seven tracked files carry the version value and the
  `TOOL-dSettledRoster-4` row says six, which is the reason to derive it. Observed by AC11.
- **S11** — the check-12 paragraph in `tools/memory-tree/HYGIENE.template.md` gains the two
  sentences its sibling ratchets each get, and the arm's own header states what it does not check.
  Observed by AC9.
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
  beside `TEMPLATE-SPEC.md` line 16 and "puts no other count in its place", so a new key arriving at
  order 8 leaves no number at order 10 to update. Unit 10 is Tier-1 and carries no `### Edges` block,
  so this edge has no reciprocal and S14's membership test makes it silent — the first live instance
  of the grammar is also the first live instance of the skip. An earlier rev of this bullet claimed
  the sentence unit 10 corrects "must count it", which is the opposite of what unit 10 does.
- **consumes-from** external — owner scope approval on §8's fork, SATISFIED 2026-09-05: the cutoff
  sits strictly ahead of every live spec filename date. S9 and AC7 are written to that answer, so the
  back-fill this edge used to hang on is refused rather than pending.

## 4. Design

### The evidence

450 of 479 specs (94%) sit in multi-spec build folders, 60 of the 89 folders holding a spec. The
template's only cross-unit field is the permitted `order <n>`, carried by 159 of 479. Those are the
research record's post-skeptic figures, and they reproduce today at 455 of 484 across 61 of 90 with
164 carrying `order` — the delta is exactly this build's own five specs written so far.

`order` expresses sequence and never an edge, and the confirmed cross-unit defects are edge failures.
`dRetiredFork` H4 hands 39 literal sites in `tools/check-wiring.sh` to `TOOL-dRetiredFork-13`, whose
own S1 population is the shipped test and selftest files and whose §3 excludes everything else. The
outward-facing half is finding 27: seven confirmed amendments where a criterion rested on something
the unit does not build, four of them in one spec. That spec is `dScaffoldedMirror-8`, whose AC1,
AC2, AC3 and AC5 all name `--probe --write`, and whose §9 rev-1 status line records the owner cutting
`--probe --write` from the unit. Four criteria died in place and nothing in the format had asked what
they rested on.

Three separate reviews have already proposed this arm as a left-shift, which is the strongest
argument for building it once rather than re-deriving it per build. `dRetiredFork` round 1 proposes a
cross-spec handoff join at H4 and reaches for it again at H8, and `dFoldedVerdict` round 1 proposes
the same join at `:110`.

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

Line numbers are not cited here: units 3, 4 and 6 edit `check-memory-hygiene.sh` before this one, so
every number in this section would be stale by the time it is read. Each site is named by its own
text, per build rule 6.

The shape arm is a branch in the batched awk that check 12 runs over `c12_sel`, placed BELOW the
`if (hdr ~ /Tier-1/) next` cut beside the section canon and the empty-body walk, because it is Tier-2
only. It reports inline like the other per-file findings in that pass, so it adds no `fail` branch,
and it reads exactly one file.

The three join arms accumulate in that same pass and emit in its END block, tagged the way the
canon-diff arm tags its excerpt request with a `\001` sentinel record. The `case "$bad12_raw" in`
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
  already sanctions, costs no canon change, and cannot red a grandfathered spec. Measured: no
  tracked spec carries a `### Edges` sub-head and exactly one carries any `###` inside §3, so the
  name is free.
- **A generated `build-edges` region per unit.** The name is already taken at build granularity —
  `GEN_REGIONS` at `gen_build_index.py:85-86` and `render_edges` at `:1013` render parent and child
  BUILDS from the README's authored `parents:` key. A unit-level twin would be a second region, a
  fourth marker pair in every build README, and a committed artifact whose only consumer is a check
  in the same language. Charter §12 says to derive that live and commit nothing. The arm reads the
  specs directly. If a reader later wants the graph rendered, it is a follow-up unit and the field
  is already the single source it would render from.
- **Extending the unattended kit's order gate.** `tools/unattended/unattended.sh:4611-4653` already
  resolves sibling units and blocks a `--dispatch` that runs ahead of its declared order, reading
  `order_verb_of` and `unit_ids_of`. It is live prior art and it is deliberately not extended: it
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
| `tools/memory-tree/.memory-tree.conf.example` | the same key, blank |

The commit also owes a `gov:kit memory-tree@` bump in every carrier. Derive that set with
`grep -rl 'gov:kit memory-tree@'` rather than from a remediation message, which
`TOOL-dSettledRoster-4` records naming three carriers when six existed.

## 5. Production-readiness checklist

- **security** — N/A. The arm reads tracked spec text the same pass already reads and writes nothing.
- **perf / scale** — no new file read and no second pass. The END-block arrays are bounded by the
  selected spec population, 484 files today. The `memory hygiene` leg's cost is recorded per run in
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
  contributes to THAT build's roster, since `rosters()` at `gen_build_index.py:661-693` keys on the
  id's own slug component; the grammar adds no new instance of that because a joined edge names a
  sibling in this build only.
- **testing + left-shift gates** — S9. Each red is staged, observed, unstaged, per build rule 4.
- **migration / rollback** — §4 Migration.
- **user docs** — `memory/HYGIENE.md` item 12 and the template itself are what an author reads. This
  repo ships no `help/` tree.

## 6. Acceptance criteria

- **AC1** — When a Tier-2 fixture spec dated at or after `SPEC_EDGES_CUTOFF` carries a §3 with no
  `### Edges` block, `bash tools/memory-tree/check-memory-hygiene.sh` reds naming that file and the
  missing block. Staged, observed RED, unstaged.
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
- **AC8** — When no tracked spec reaches the cutoff, the full run prints the named zero-population
  notice on stdout, in the shape the §10 evidence arm's `graded NO spec` notice already uses.
- **AC9** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the template edit, it
  is green, and `git diff` shows `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md` changed only by
  the render.
- **AC10** — When the candidate predicate is run standalone over
  `git ls-files 'memory/builds/*/spec/*'` BEFORE it is wired, it prints its hits AND its
  near-misses, and the near-miss list is read for false positives rather than counted. Charter §7
  requires this, and it is the run that decides AC5's shape.
- **AC11** — When `python3 tools/memory-tree/check-arms.py --check` runs with the re-measured
  `ARMS_FLOORS`, it is green, and `--report` shows the three new `fail 12` branches armed rather than
  pinned.
- **AC12** — When exactly ONE spec of a conforming edge pair is staged in the self-test scratch tree
  and `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs, the run does not red on that
  pair and prints the HELD announce line naming check 12, in the wording
  `memory-hygiene: check 23 HELD under --staged` already ships. The same run still reds the staged
  file's own missing `### Edges` block, which is what proves the shape arm stayed live rather than
  the whole check going quiet. The harness is the existing `--staged` block in
  `tools/memory-tree/check-memory-hygiene.test.sh`, the one whose comment reads
  `in_scope is the ONLY thing deciding selection there`.
- **AC13** — When a Tier-2 fixture declares `hands-off` a Tier-1 sibling that carries no `### Edges`
  block, a FULL `bash tools/memory-tree/check-memory-hygiene.sh` is silent about that pair, and it is
  silent the same way for an edge naming a spec the cutoff grandfathered. Staged, observed GREEN
  against the version of the arm that lacks the membership test — that arm reds, which is the failing
  case this criterion exists to have seen.

## 7. Gates

- `memory hygiene` · `memory-hygiene self-test`
- `kit/dogfood doc parity` · `kit version markers`
- `harness arms (fail branches armed or pinned)` · `verdict epoch (kit version dates the engine)`
- `spec tokens (a spec's own names resolve)`

This unit adds no leg. The arm's home is check 12 inside `tools/memory-tree/check-memory-hygiene.sh`,
which the `memory hygiene` leg already runs. Its fixtures live in
`tools/memory-tree/check-memory-hygiene.test.sh`, run by `memory-hygiene self-test`, which is guarded
to `tools/memory-tree/` and so fires on this unit's own diff. `kit/dogfood doc parity` is what makes
the two template halves one edit, `kit version markers` reds if a `gov:kit memory-tree@` carrier is
left behind, and `harness arms (fail branches armed or pinned)` is what the three new `fail 12`
branches move.

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

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declaring a dependency edge between two sibling spec
units in one build"` returned the build-README region machinery as its nearest seams,
`add_spec_records_region` in `tools/memory-tree/gen_build_index.py` and `apply_region` in the
`build-readme-surface` dossier. That is the seam this unit deliberately does NOT extend, for the
reason §4 Alternatives rejected records. The seam it does extend is check 12's batched awk over
`c12_sel` in `tools/memory-tree/check-memory-hygiene.sh`, which the map does not index because it
holds no shell symbols. The recall probe found the live prior art the map could not:
`tools/unattended/unattended.sh:4611-4653` already resolves sibling units by their `order` verb and
blocks a dispatch that runs ahead of them, which is sequence rather than an edge, and it is a
different kit on a different trigger.

Recall terms used: `spec unit sibling handoff order verb build roster cross-spec join hygiene check
12 cutoff edge`.
