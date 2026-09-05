# TOOL-aJoinedCanon-3 — a scope item names the criterion that observes it

**Status:** SPECCED · rev-5 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 3 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

Join §2 to §6. Every scope item names the acceptance criterion that observes it, or states that none
does and why, and a dated check-12 arm asserts the shape.

Be precise about what the evidence says, because overstating it is how this unit gets refuted.
Finding A1 measures a CITATION RATE: over the 460 specs carrying both numbered lists, 408 of 3,061 S
ids (13.3%) are named anywhere in their own §6, and 260 specs (56.5%) name none at all. That is a
measure of HABIT, not of coverage. A spec can observe every one of its scope items without ever
writing an S id, and many do. What the number establishes is that the template's own stated reason
for numbering both lists — so they can be cited stably, the `Number scope and acceptance items`
bullet in `memory/TEMPLATE-SPEC.md` — buys almost
nothing today.

The evidence that scope items genuinely go unobserved is the review corpus, not the citation rate.
Sixteen distinct builds confirm the class. In `dRetiredFork` round 1 it is the set's dominant
failure with five rows, one of them a BLOCKER on that build's own named highest-risk mitigation.
The join is worth building because those reviews keep finding it by hand at a full agent fan per
build, and because the answer is doc-local: it needs no tree access and no second file.

## 2. Scope (IN)

- **S1** — a new cutoff key `SCOPE_JOIN_CUTOFF`, declared in `.memory-tree.conf` beside its
  siblings, defaulted blank in `tools/memory-tree/check-memory-hygiene.sh` in the preset block whose
  `SPEC10_EVIDENCE_CUTOFF=""` line ends `blank = never required`, and shipped blank in
  `tools/memory-tree/.memory-tree.conf.example` UNDER the adopter comment each sibling ratchet
  carries there: what the rule is, that blank means off, and that the value is set strictly ahead of
  every dated spec on every live branch. Blank means off, taking `STREAMS_CUTOFF` semantics rather
  than `SPEC10_CUTOFF`'s forward resolution. Observed by AC3 for the gating, AC7 for the
  announcement, AC10 for the shipped key AND its comment, and AC12 for blank meaning off. The last
  two are new at rev-4: a bare `SCOPE_JOIN_CUTOFF=""` line is a key an adopter meets with no way to
  know what arming it costs, and the off-state is the rollback path §5 names and nothing exercised.
- **S2** — the rule stated in `tools/memory-tree/SPEC-TEMPLATE.template.md`: one paragraph in the
  skeleton's §2 body, under the line beginning `What this unit builds, as a bounded numbered list`,
  parallel to the acceptance-witness paragraph that opens `Once a spec's filename date reaches
  SPEC_WITNESS_CUTOFF`, plus a clause on the numbering bullet that begins `Number scope and
  acceptance items`. Observed by AC6 for the render and AC9 for the content.
- **S3** — `memory/TEMPLATE-SPEC.md` re-rendered from that template, never hand-edited. Observed by
  AC6, and only in company with AC9: a byte-compare is equally green when neither half moved.
- **S4** — a new branch in check 12's awk body, OUTSIDE the acceptance-witness guard and at the same
  nesting level as it: after the CLOSING brace of the block that opens
  `if (wcut != "" && fdate != "" && fdate >= wcut) {` and whose last statement prints
  `acceptance bullets naming no backticked witness` — after the brace, not after the print, which
  sits inside the guard — and therefore above the Tier-1 cut, the `if (hdr ~ /Tier-1/) next` line
  that opens the section canon. Outside is the whole of it: nested there, this arm's population
  would be the INTERSECTION of `SCOPE_JOIN_CUTOFF` and `SPEC_WITNESS_CUTOFF`, and the witness key
  ships blank in `tools/memory-tree/.memory-tree.conf.example`, so an adopter arming this key alone
  would get an arm that never runs while its own key reads as armed. The branch carries its own
  liveness test on its own `-v jcut=` binding and reads no other cutoff. It walks §2's column-0
  items and reports every item whose own text names neither an `AC<n>` token nor the escape.
  Observed by AC1, AC2, AC4 and AC11.
- **S5** — the arm's population guards: both section headings matched by HEADING TEXT rather than by
  number, and the arm silent unless both are present. Observed by AC5.
- **S6** — the zero-population announcement, modelled on the §10 evidence arm's in
  `tools/memory-tree/check-memory-hygiene.sh`, the line printing `the §10 reuse-evidence arm graded
  NO spec`. At adoption this arm grades no tracked spec, and a skip that looks like a pass is
  indistinguishable from coverage. Observed by AC7.
- **S7** — red and green fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`, in this
  unit's declared block `tFixture-110` upward. The build README's rules own that number space and
  hand `order` 3 the block at 80 + 10·3; no spec re-derives it from the file's high-water, which is
  true only for whichever of the three units sharing this harness lands first. Plus the staged-red
  run against the real tree that build rule 4 requires. Observed by AC1 through AC5 and AC8.
- **S8** — the version bookkeeping every engine-touching unit owes: `KIT_MEMORY_TREE_VERSION` in
  `tools/memory-tree/check-memory-hygiene.sh` advances, and every `gov:kit memory-tree@` marker
  carrier moves with it. The carrier set is DERIVED at build time by §4's recipe and is counted
  nowhere in this spec. Bookkeeping rather than mechanism, and in scope because this unit changes
  what the engine's verdicts are, which is the thing the constant dates. Observed by AC13.
- **S9** — the rule reaches the check catalog: one sentence in the check-12 entry of
  `tools/memory-tree/HYGIENE.template.md`, in the shape that entry's sibling ratchets already use —
  the sentence beginning `Every acceptance bullet must name a witness in backticks once the filename
  date reaches` and its SHAPE-only caveat — with `memory/HYGIENE.md` re-rendered from it and never
  hand-edited. That file's catalog heading declares it the prose home for every check in
  `tools/memory-tree/check-memory-hygiene.sh`, so a ratchet absent from it is a ratchet no reader of
  the catalog can find, and the four sibling ratchets are each named there today. Observed by AC6
  for the render and AC14 for the content.
- **S10** — `memory/guides/SESSION-KICKOFF.md` is re-stamped: `last-audit` moves to a fresh
  `<ISO datetime> @ <sha>` per that manifest's own stamping rule, which this spec does not restate.
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf` are both `watch:` pathspecs of
  that manifest, read off its own audit block, and S1 and S4 edit both — so this unit's landing is a
  watched change, and check C5 of `skills/session-kickoff/manifest-check.sh`, `no unaudited watch
  drift`, reds on a watched change with no re-stamp at or after it. `last-body-change` does NOT move
  and §B gains no delta line: this unit changes no gate command, entrypoint, layout convention or
  front-loaded claim, and the manifest's own rule is "no delta → no touch". §B's bullet beginning
  `The hygiene engine PRE-SETS its conf keys` already describes the preset-plus-blank mechanism S1
  uses, so nothing that file front-loads becomes false. Observed by AC15.

## 3. Non-goals (OUT)

- **Grading whether the named criterion actually observes the item.** No substring test reaches it.
  §4 states the limit in the gate's own header style and the arm's message does not overclaim.
- **Requiring §2 items to carry `S<n>` labels.** The template already asks for a numbered list and
  nothing checks it; 3,146 of 3,207 items (98.1%) comply anyway. Grading the BULLET rather than the
  LABEL is what makes this unit indifferent to that gap, so closing it separately is not owed here.
- **Retrofitting any landed spec.** Build rule 3. The cutoff carries the whole corpus and this unit
  edits no existing spec. Per F2 this build's own eleven specs are grandfathered with the rest: the
  cutoff is set ahead of every spec on every live branch, so the rule's first live subject is the
  next build.
- **The reverse join, §6 to §2.** A criterion that observes nothing in scope is a different and
  weaker defect, and walking criteria cannot see an unobserved scope item at all.
- **Anything in check 23's ledger join**, which is `TOOL-aJoinedCanon-6`, and anything in §7's leg
  resolution, which is `TOOL-aJoinedCanon-7`.
- **The four specs whose §2 carries no column-0 bullet.** They stay ungraded. §4 names them as a
  pinned gap rather than widening the walker to prose.
- **A deny-list of parity-only observers inside this arm.** Review H9's left-shift proposes the arm
  refuse an item whose named criterion runs nothing but a byte-compare. That is the first non-goal
  above wearing a different hat: to classify a criterion's commands the arm must resolve the label
  into §6 and read what it says, which is the semantic step no substring test reaches. It stays a
  follow-up for a unit that can see §6. H9's Fix — an observation that fails when the rule text is
  absent — is folded, and it is what closes the instance.
- **The three widenings spec-audit round 3 proposed for this arm.** Four of that round's left-shifts
  name this unit as their mechanism: grade a Files-touched row against the scope item or criterion
  that owns it (H2's second half, M4), grade a criterion's named artefact against the scope item that
  constructs it (H5), and grade each CLAUSE of a scope item rather than the item (M7). None is a
  widened predicate of this arm, because each walks a different population — a table's rows, §6's
  bullets, a sentence's clauses — and the third needs the semantic step the first non-goal above
  rules out. They are recorded rather than parked, because this build has no round 4.
  **Follow-up:** a `TOOL` backlog row against `tools/memory-tree/check-memory-hygiene.sh`, opened at
  this build's landing, carrying all four with the population each needs. This unit discharges its
  OWN instance of H2 by hand, as S10.

## 4. Design

### Data model

The rule, as an author reads it: every column-0 item in `## N. Scope (IN)` names in its own text at
least one acceptance criterion by label, spelled `AC` followed by digits, or carries the marker
`NOT OBSERVED` followed by the reason. One escape spelling, deliberately not widened, for the
reason the §10 terms arm records in its own comment, the one reading `A false red names its own
remedy`: the template states the accepted spelling, while a false pass is silent.

`SCOPE_JOIN_CUTOFF` gates it by FILENAME date, exactly as `SPEC_WITNESS_CUTOFF` does. Blank turns
the arm off. The value is set at landing time strictly ahead of every spec dated on every live
branch, enumerated with `git for-each-ref refs/heads`, which is the idiom `.memory-tree.conf`
records for `SPEC10_EVIDENCE_CUTOFF` under its `WHY 2026-09-01 AND NOT THE LANDING DAY` comment,
and the reason that cutoff is 2026-09-01 rather than its build date.

### The walk

An ITEM is a column-0 `- ` or `* ` line plus every following line until the next column-0 bullet,
the next `## ` heading, or the next `### ` sub-head. An indented bullet is a continuation, so an
item may enumerate its criteria as sub-bullets and still be graded as one item. Fenced content never
reaches the walk: the `_unfenced` fence machine in `tools/memory-tree/check-memory-hygiene.sh`,
the block headed `the _unfenced fence machine, verbatim: CR strip, marker-matched fences`, builds
the body array with fenced lines excluded, so a `- ` inside a code block is not an item and an `AC1`
inside one cannot satisfy anything.

Both headings are matched by TEXT, never by number, and the arm stays silent unless both are
present. That is not caution, it is a defect this corpus already paid for: review M13 of
`dUnstalledConvoy` found a unit whose population keyed on `## 6.` and reds a Tier-1 spec that is
legal under the format, because two closed Tier-1 specs number their criteria under §5 and carry
Gates at §6. Matching heading text handles those two, and requiring both headings means a Tier-1
spec that legitimately writes no acceptance section is untouched rather than told to grow one.

The heading regexes are copied from the sibling witness arm verbatim, literal-tab character class
included, so the two agree by construction rather than by coincidence.

**Where the branch sits, and why `TOOL-aJoinedCanon-4`'s hoist is a different hoist.** The branch is
a top-level block in the same awk body as the acceptance-witness arm and OUTSIDE that arm's guard,
which opens `if (wcut != "" && fdate != "" && fdate >= wcut) {` and does not close until after its
own print. Nesting inside it would make this arm's population the intersection of two cutoffs — dead
for any adopter who arms `SCOPE_JOIN_CUTOFF` while `SPEC_WITNESS_CUTOFF` sits blank, which is what
`tools/memory-tree/.memory-tree.conf.example` ships, and dead invisibly, because this key would read
as armed. `TOOL-aJoinedCanon-4` fixes that same class in its own arm by HOISTING the accumulator out
of the guard so two arms can ride one walk over the SAME §6 bullets. That hoist does nothing here and
cannot, for two independent reasons: it lands at `order` 4, one step after this unit builds, and it
moves an accumulator this arm never reads. The §2 walk is separate code over a different section with
its own state and no shared string, so there is nothing for a hoist to free — independence is bought
by PLACEMENT and by reading only `jcut`. Two hoists, two blocks, one class.

**The binding is named `jcut`, and this paragraph is this build's namespace registry.** The rule the
build README hands this unit: a unit introducing an awk binding, a function name or a fixture number
CLAIMS it HERE before a sibling reads it, and a sibling CITES this register rather than copying it —
a copied list is stale the moment any unit renames, which is what the three surviving copies show —
units 8, 9 and 11 each restate a taken list and all three still say `mcut`. Nine
names are bound on the one check-12 awk invocation today, verified at source on the `bad12_raw=` line:
`canon`, `canon10`, `cut10`, `mroot`, `discalt`, `scut`, `wcut`, `fcut`, `ecut`. Check 23 is a
SEPARATE invocation with its own namespace — its `-v cut=` carries the shell's `alcut` — so an arm
added there cannot collide here and nothing here can collide there. The `tFixture` number space is
NOT restated in this register: the README allocates it by formula at `80 + 10N`, so it derives and
this would only rot.

| Name | Claimant | Key it carries |
|---|---|---|
| `revscopecut` | `TOOL-aJoinedCanon-1` | `REV_SCOPE_CUTOFF` |
| `jcut` | `TOOL-aJoinedCanon-3` | `SCOPE_JOIN_CUTOFF` |
| `fmcut` | `TOOL-aJoinedCanon-4` | `SPEC_FAILURE_MODE_CUTOFF` |
| `rrows` and `rcut` | `TOOL-aJoinedCanon-9` | `READINESS_ROWS` and `READINESS_ROWS_CUTOFF` |
| `edgecut` | `TOOL-aJoinedCanon-8` | `SPEC_EDGES_CUTOFF` |
| `bcut` | `TOOL-aJoinedCanon-11` | `BASE_RESOLVE_CUTOFF` |

Read off each sibling's own text at this fold, not remembered; every one of them is at rev-5 bar
`TOOL-aJoinedCanon-10`, which adds no binding. Units 2, 5, 7 and 10 add none either. Check 23's
`alsel` invocation is the separate namespace named above and `TOOL-aJoinedCanon-6` claims `lcut` and
`tcut` on it, for `LEDGER_LABEL_CUTOFF` and `LEDGER_TOKEN_CUTOFF`; they are recorded here because the
rule is one owner per shared ENGINE name, and they cannot collide with the table above.

`edgecut` arrived during this same fold — rev-4 of that spec named no spelling at all, and its rev-5
both picks one and says this register "owes a row for this name". That is the register working at the
only speed it can: a sibling claims, this file records, and the claim is checked against the table
rather than against a copy of it.

**Round 3's blocker was this register being WRONG rather than absent.** It named
`TOOL-aJoinedCanon-4` as the sole claimant of `mcut` while `TOOL-aJoinedCanon-1`, three `order` steps
EARLIER, was taking the same name on the same invocation. Last `-v` wins for the whole awk program, so
from `order` 4 one arm would have been graded by the other's key with its own conf key still reading
as armed — this build's own subject, shipped as a defect. Both renamed at rev-5, off the
one-letter-plus-`cut` convention that made the collision reachable and onto names spelled from their
keys. `jcut` was never in that collision and does not move. One disagreement survives and is recorded
here because there is no round 4 to settle it: `TOOL-aJoinedCanon-1` builds the mechanical check as
its AC16, a self-test assertion that the extracted check-12 invocation binds no name twice, while
`TOOL-aJoinedCanon-4`'s §3 declines to build that arm and routes it to a backlog row. Unit 1 lands at
`order` 1, so the assertion exists before unit 4 needs it; the register is the interim control either
way.

AC11 is this unit's own observation: a scratch tree that arms this key and NO witness key, still red.
It is also the regression net for unit 4's hoist one step later, since it reds if any later
restructuring of the neighbouring block draws this branch back inside a guard. It does NOT see a
rebind of `jcut` itself, and nothing else in this spec does either — that is unit 1's AC16, above.

The message names each offending item the way the witness arm names each offending label in its own
`print`.
An item carrying an `S<n>` label is named by that label. An unlabelled item is named by its ordinal
within the section, because a message that names only the file leaves the author to re-derive which
of a median seven items it meant.

### Inventory

The candidate predicate was run over the real tree before being proposed, per charter §7, at base
750ca0ca and excluding this build's own folder, whose sibling units are landing while this is
written. That exclusion matters: two runs minutes apart over the unfiltered glob disagreed by three
specs for exactly that reason.

| Measured | |
|---|---|
| Specs with a parseable status header | 474 |
| Carrying a `## N. Scope (IN)` heading | 471 |
| Of those, also carrying `## N. Acceptance criteria` | 471 — every one |
| Of those, no column-0 bullet in §2 (ungraded) | 4 |
| Column-0 §2 items | 3,207 |
| Items carrying an `S<n>` label | 3,146 (98.1%) |
| Items naming an `AC<n>` in their own text | 110 (3.4%) |
| Items containing the string `not observed` | 0 |
| Tier-1 share, graded under F1 | 114 specs · 519 items |
| `NOT OBSERVED` in `memory/TEMPLATE-SPEC.md` and its template today | 0 in each |
| `^SCOPE_JOIN_CUTOFF=` in `tools/memory-tree/.memory-tree.conf.example` today | 0 |
| `SCOPE_JOIN_CUTOFF` in `memory/HYGIENE.md` and its template today | 0 in each |

Three things follow. The corpus passes this predicate at 3.4%, so the cutoff carries everything and
the arm grades no landed spec on day one — S6 exists because of that number. The escape spelling is
unclaimed, so it cannot pass an item by accident. And grading the bullet rather than the label costs
61 items over the corpus, which is the price of not being opt-out-able by deleting two characters.

The last three rows are the pre-change baselines AC9, AC10 and AC14 need. All are 0 today, so none of
those greps can be green before the edit lands — which is the whole difference between those
three criteria and a byte-compare that is equally green when nothing moved. Both doc pairs are
covered that way at rev-4: the template pair by AC9, the HYGIENE pair by AC14.

The near-miss worth reporting: closing an item on a `### ` sub-head rather than only on `## `
changes the item count by 2 across the whole corpus. It is kept because a sub-head between items
otherwise glues them together and an `AC` token below the sub-head buys a pass for the item above.

### What this arm does NOT check

Stated here in the gate's own header style, because a structural check reads as a semantic one to
everybody who did not write it.

It checks SHAPE. It asserts that an item names a criterion label, never that the named criterion
observes that item, never that the label exists in §6, and never that the criterion is any good. A
scope item that names `AC9` when the spec numbers eight criteria passes. So does one that names the
criterion for a different item.

The bound is measurable on the far side too, and finding 21 puts a number on it after its
suite-green half was refuted in part: 56 of 3,917 criteria across 471 specs observe nothing more
than a suite being green. So pointing at a criterion is usually pointing at a real observation, and
occasionally it is not, and this arm cannot tell the two apart.

Two populations stay dark and are pinned rather than implied away. The four specs whose §2 holds no
column-0 bullet are ungraded, because prose and tables have no item boundary a walker can find. And
on Tier-1, where the section canon is not enforced, deleting the acceptance heading silences the
arm; on Tier-2 the same deletion reds the canon compare, so the escape does not exist there.

### Migration

None for existing specs. The cutoff is the migration.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | the rule, in the §2 body and the numbering bullet |
| `memory/TEMPLATE-SPEC.md` | re-rendered, never hand-edited |
| `tools/memory-tree/check-memory-hygiene.sh` | the arm outside the `wcut` guard, its `-v jcut=` binding on check 12's awk invocation, the blank preset, the announcement, and the `KIT_MEMORY_TREE_VERSION` constant |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the fixtures and their `hit`/`miss` assertions |
| `.memory-tree.conf` | the declaration |
| `tools/memory-tree/.memory-tree.conf.example` | the same key, blank, with its adopter comment |
| `tools/memory-tree/HYGIENE.template.md` | S9, one sentence in the check-12 entry |
| `memory/HYGIENE.md` | re-rendered from it, never hand-edited |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp only; no body delta (S10) |
| every `gov:kit memory-tree@` marker carrier | the version marker; the set is derived below, never listed here |

Both template halves move in one commit: `tools/memory-tree/kit-dogfood-parity.test.sh` renders
TEMPLATE to LIVE and byte-compares, so editing either alone reds `kit/dogfood doc parity`. The
direction is stated at that file's header and the render is
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.

The commit also owes a `gov:kit memory-tree@` version bump in EVERY carrier, which is S8. Derive the
set at build time with `git grep -l 'gov:kit memory-tree@'` and keep the carriers — the files whose
marker `tools/check-kit-versions.sh` grades — rather than the whole hit list, because the raw grep
also matches records that merely QUOTE a marker, this spec among them. Never take the set from a
remediation message: backlog row `TOOL-dSettledRoster-4` records one naming three carriers when six
existed, and records the same defect being hit twice, the second time costing a full extra bar cycle.
The two legs behind it fail for different reasons and AC13 states which is which: an engine edit with
the constant left alone reds `verdict epoch`, since the constant is what DATES a verdict change,
while `kit version markers` is what reds when the constant advances and a carrier is left behind.

### Alternatives rejected

- **Host the rule in `tools/check-spec-tokens.py`.** It is the repo's other spec-section joiner and
  it already scopes by heading. Rejected on population: its `LIVE` status regex grades only
  OPEN, SPECCED, INPROGRESS and BLOCKED specs, so a rule hosted there stops grading a spec the
  moment it goes CLOSED. Check 12 grades every post-cutoff spec at any status, which is what a
  format rule needs.
- **A trailer table mapping S to AC at the foot of §2.** Cheaper to author at a median seven rows,
  but it separates the claim from the item and the arm would then grade the table rather than the
  items. The unit's mechanism is per-item by roster.
- **Require the join in the other direction, on the criterion.** See §3.
- **Grade `S<n>`-labelled items only.** Two characters wide to opt out of, which is the silent
  opt-out class `TOOL-aJoinedCanon-7` exists to close in §7. Rejected for that reason alone.

## 5. Production-readiness checklist

- security — N/A. A read-only text walk inside an existing gate, over tracked files.
- perf / scale — the walk is one more pass over the `body` array already in memory, over a
  population of 471 specs. No new file reads and no new process.
- a11y — N/A. Gate output on a terminal.
- i18n — N/A. ASCII labels and one ASCII marker.
- error / empty / loading states — a blank `SCOPE_JOIN_CUTOFF` or a blank `SPEC_FORMAT_CUTOFF`
  disables the branch, which AC12 observes. A spec with only one of the two headings, or a §2 with no
  column-0 bullet, is silent rather than red.
- observability — the message names the cutoff, the file and every offending item. The zero-
  population announcement prints whenever the arm grades nothing.
- risks (concurrency, data-loss, rollback hazards) — none to data. The rollback is blanking the
  conf key, which turns the arm off without touching a spec. The live risk is a false red on a
  legal spec shape, which is what the pre-wiring corpus run and the Tier-1 fixture exist to bound.
- testing + left-shift gates — the fixtures in S7 are the coverage, because the corpus exercises
  nothing on day one. `check-arms.py` cannot force them: it scans SHELL `fail` call sites, and check
  12 collects its awk findings into `bad12` and reports them through the
  `[ -n "$bad12" ] && fail 12` line in `tools/memory-tree/check-memory-hygiene.sh`, so a new awk
  branch is invisible to the arm requirement whatever the number of those call sites happens to be
  when this lands. The discipline is this spec plus build rule 4.
- migration / rollback — see §4. No spec is edited.
- user docs — the two an adopter actually meets: the spec template, which S2 changes and AC9 reads,
  and the check catalog in `memory/HYGIENE.md`, which S9 changes and AC14 reads. The comment on the
  shipped conf key is the third, in S1 and read by AC10. No `help/` page: this repo ships none.

## 6. Acceptance criteria

- **AC1** — When a spec dated on or after the cutoff carries a §2 item naming neither an `AC<n>`
  token nor the escape, `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 and its output
  names that item and `SCOPE_JOIN_CUTOFF`.
- **AC2** — When that same item gains an `AC` label, the run is silent for that fixture, asserted by
  a `miss` line in `tools/memory-tree/check-memory-hygiene.test.sh`.
- **AC3** — When the identical item sits in a spec whose filename date is before
  `SCOPE_JOIN_CUTOFF`, `bash tools/memory-tree/check-memory-hygiene.sh` is silent for it, so nothing
  landed is retroactively red.
- **AC4** — When an item carries `NOT OBSERVED` and a reason, the run is silent for it, and a
  fixture whose §2 says `not observed` in ordinary prose is not thereby excused, since the corpus
  run in §4 measured 0 of 3,207 items containing that string.
- **AC5** — When a spec carries a `## N. Scope (IN)` heading and no `## N. Acceptance criteria`
  heading, `bash tools/memory-tree/check-memory-hygiene.sh` is silent for it, pinning the M13 class
  from `dUnstalledConvoy`. A Tier-1 fixture carrying BOTH headings and one unjoined item reds, as a
  `hit` line, pinning F1's both-tiers ruling.
- **AC6** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the edit, it exits 0,
  proving `memory/TEMPLATE-SPEC.md` matches `tools/memory-tree/SPEC-TEMPLATE.template.md`, and
  `memory/HYGIENE.md` its own template, rather than either live half having been hand-edited. It
  grades SAMENESS on both pairs, and is equally green when neither half of a pair was touched, so it
  observes S2 and S3 only in company with AC9 and S9 only in company with AC14 — those two supply the
  content half it structurally cannot.
- **AC7** — When the cutoff is ahead of every tracked spec, a full run prints the zero-population
  announcement naming `SCOPE_JOIN_CUTOFF`, and when it is not, the announcement is absent.
- **AC8** — When the cutoff is temporarily lowered to a date the corpus reaches and
  `bash tools/memory-tree/check-memory-hygiene.sh` is run against the real tree, it reds naming
  tracked specs, and the §4 measurement predicts it names essentially all of them at a 3.4% pass
  rate. The lowering is unstaged before the commit and the transcript goes in the build record.
- **AC9** — When `memory/TEMPLATE-SPEC.md` is read after the render, `grep -c 'NOT OBSERVED'` on it
  returns non-zero, its §2 body names the `AC<n>` spelling, and the numbering bullet beginning
  `Number scope and acceptance items` carries the new clause. §4's inventory derives the pre-change
  count as 0 in both `memory/TEMPLATE-SPEC.md` and its template, so this grep cannot be green until
  the rule text exists — which is the observation S2 lacked while AC6 was its only observer.
- **AC10** — When `grep -qE '^SCOPE_JOIN_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` runs
  after the edit it exits 0; the comment block immediately above that line names the rule, says blank
  is off, and says to set the value ahead of the corpus, which
  `grep -B6 '^SCOPE_JOIN_CUTOFF=' tools/memory-tree/.memory-tree.conf.example | grep -ci 'blank'`
  returns non-zero for; and `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0 with its
  derived engine-preset parity arm satisfied — the arm that greps the shipped example for every bare
  `*_CUTOFF` preset the engine declares. The key and the comment are both absent today, per §4, so
  both greps are red before the edit, and that self-test arm reds from the moment the engine gains
  the preset until the shipped example declares it. The bare key was the third of S1 that no
  criterion reached before rev-3; the comment beside it was the fourth, and an adopter reads that
  before anything in this repo.
- **AC11** — When a fixture dated on or after `SCOPE_JOIN_CUTOFF` carries an unjoined §2 item in a
  scratch tree whose conf declares `SCOPE_JOIN_CUTOFF` and declares NO `SPEC_WITNESS_CUTOFF`,
  `bash tools/memory-tree/check-memory-hygiene.sh` still exits 1 naming that item. The break it
  stages: the branch nested inside the `wcut` guard, where this arm's real population is the
  intersection of two cutoffs and an adopter arming this key alone gets a dead arm whose own key
  reads as armed. It is `TOOL-aJoinedCanon-4`'s AC7 in this unit's numbering, for the same defect one
  `order` step earlier — round 1 ruled the class on that unit at `order` 4, and this unit writes the
  block first at `order` 3. Per build rule 4 the red is observed before the arm lands.
- **AC12** — When `SCOPE_JOIN_CUTOFF` is blank in the fixture conf, the AC1 fixture passes and
  `bash tools/memory-tree/check-memory-hygiene.sh` prints no join finding at all. This is the only
  exercise of the `jcut != ""` conjunct and of §5's rollback path; the break it stages is the blank
  string comparing earlier than every date and arming the rule over the whole grandfathered corpus,
  which is the one thing the cutoff mechanism exists to prevent.
- **AC13** — When the landing commit is in place, `bash tools/check-kit-versions.sh` and
  `bash tools/memory-tree/check-verdict-epoch.sh` both exit 0. The break it stages is the engine
  edited with `KIT_MEMORY_TREE_VERSION` left alone, which reds `verdict epoch` and NOT
  `kit version markers` — an unmoved constant still agrees with every carrier, so the marker leg is
  green exactly when the version is most wrong. `kit version markers` is the leg that reds the other
  way, when the constant advances and a carrier derived per §4 is left behind. Together they observe
  S8.
- **AC14** — When `memory/HYGIENE.md` is read after the render, its check-12 entry names
  `SCOPE_JOIN_CUTOFF` and carries the SHAPE-only caveat beside it. §4's inventory records
  `grep -c 'SCOPE_JOIN_CUTOFF' memory/HYGIENE.md` as 0 before the edit, in both halves of the pair,
  so this cannot be green until the sentence exists — which is what AC6's byte-compare can never tell
  you about the HYGIENE pair, on exactly the terms it cannot tell you about the template pair.
- **AC15** — When `bash skills/session-kickoff/manifest-check.sh` runs on the landing commit it exits
  0, and `memory/guides/SESSION-KICKOFF.md`'s `last-audit` names a sha at or after the commit that
  edits `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`. The break it stages is
  the revert of S10 alone: keep the engine and conf edits, restore the old stamp, and check C5 — `no
  unaudited watch drift` — reds naming those two files as watched changes with no re-stamp at or
  after them. `last-body-change` is the SAME sha before and after, which is the half that observes
  the "no delta → no touch" side of the rule rather than the re-stamp side. That command was run on
  the unedited tree at this fold and exits 0, so a red is this unit's edit and not a standing one.

## 7. Gates

- `memory hygiene` · `memory-hygiene self-test` · `kit version markers`
- `verdict epoch (kit version dates the engine)` · `harness arms (fail branches armed or pinned)`
- `spec tokens (a spec's own names resolve)` · `kit/dogfood doc parity` · `kickoff-manifest ratchet`

Every name above is a leg NAME in `tools/gate-legs.json`, checked against that manifest at rev-5,
and not a script path. The join in `tools/check-spec-tokens.py` grades NAMES; a path is not one and
does not become one when `TOOL-aJoinedCanon-7` widens what resolves at `order` 7, so a path written
here would contribute no graded leg either before or after that unit.

The first two are the arm's own bar. `kit/dogfood doc parity` is what makes each doc pair one edit —
the template pair for S2 and S3, the HYGIENE pair for S9. The two version legs fail for opposite
reasons and AC13 states which: `verdict epoch` reds when this unit changes the engine's verdicts and
`KIT_MEMORY_TREE_VERSION` does not move, and `kit version markers` reds when the constant moves and a
`gov:kit memory-tree@` carrier is left behind. This unit adds no new leg; the arm lives inside check
12, which is already on the bar.

`kickoff-manifest ratchet` is the one leg here this unit does not itself exercise. Read at HEAD it
carries `subject: repo` and no `guard`, so it runs on every bar whatever this unit does, and its
`argv` is exactly the command AC15 runs. It is on the list because S1 and S4 edit two `watch:`
pathspecs of `memory/guides/SESSION-KICKOFF.md`, which makes S10's re-stamp the thing that keeps it
green; AC15 is the observed red.

## 8. Open questions

- **F1 · Does the arm run on both tiers, or on Tier-2 only?** RESOLVED (owner, 2026-09-05): both
  tiers, guarded by the both-headings precondition, so the 114 Tier-1 specs and their 519 items are
  in the graded population. Both-tiers is the acceptance-witness arm's own answer, recorded in that
  arm's own comment in `tools/memory-tree/check-memory-hygiene.sh` as "a Tier-1 spec
  is exempt from the canon, not from meaning what it writes", and the conf records that narrowing
  that arm to Tier-2 left its harness byte-identical until a fixture existed. Against it: Tier-1 is
  the light profile the template calls "ceremony is conditional", and the evidence for this join is
  entirely Tier-2 multi-unit builds. The population at stake is 114 specs and 519 items, 16.2% of
  the graded items. RECOMMENDATION: both tiers, guarded by the both-headings precondition, which
  makes a Tier-1 spec that writes only §2 untouched either way. It was the owner's knob and not this
  spec's, because it changes what the gate demands of every future Tier-1 spec.
- **F2 · Does this build retrofit its own eleven specs to the new form?** RESOLVED (owner,
  2026-09-05): grandfather them, ruled for the whole build at once — the cutoff sits ahead of every
  spec on every live branch, so this build's own eleven do not follow the rule they add, and the
  arm's coverage is its fixtures. The cutoff must be set ahead of them, so they are grandfathered
  and the rule's first live subject is the next build. That
  is the established idiom and it means the build that adds the join ships eleven specs that do not
  follow it. The alternative is a voluntary rev-2 fold across all eleven at fold time, which is
  authoring rather than a gate retrofit and so does not collide with build rule 3, but it edits ten
  specs written by other writers who never had the rule. RECOMMENDATION: grandfather them, and let
  the arm's coverage be its fixtures, exactly as `SPEC10_EVIDENCE_CUTOFF` did one week earlier.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §3 · §4 · §6 · folded the owner's rulings on both forks. F1: both
  tiers, so the 114 Tier-1 specs and 519 items are in the graded population and AC5's Tier-1 fixture
  is a `hit` line rather than a fixture whose tier scope the fork still decided. F2: grandfather this
  build's own eleven specs, which §3 now states as a non-goal in its own right.
- rev-3 · 2026-09-05 · §1 · §2 · §3 · §4 · §5 · §6 · §8 · §10 · folded spec-audit round 1. H1: S7 moves
  to the README-allocated block `tFixture-110` upward and drops the file-high-water claim that was
  true only for whichever of three units lands first. H9: AC9 and AC10 are new, observing the rule
  text in the rendered template and the key in the shipped example conf, both against a pre-change
  count of 0 now recorded in §4; AC6 is rewritten to say that a byte-compare grades sameness and is
  green when neither file moved; S1, S2 and S3 name the new observers. §3 declines H9's left-shift
  deny-list with its reason. Every line number this spec pinned in a file a lower-`order` unit moves
  first became a citation by literal text, per the build's rule.
- rev-4 · 2026-09-05 · §2 · §4 · §5 · §6 · §7 · folded spec-audit round 2 and swept its 23 classes.
  B1: S4 now places the branch OUTSIDE the `wcut` guard, after that block's closing brace rather than
  after its print, on its own `-v jcut=` binding; §4 gains "Where the branch sits", which says why
  `TOOL-aJoinedCanon-4`'s hoist is a different hoist — it lands one `order` step later and moves an
  accumulator this §2 walk never reads — and AC11 is the observation, a scratch tree arming this key
  with NO `SPEC_WITNESS_CUTOFF` that still reds. H1: S8 is new for the version bookkeeping, §4's
  Files-touched table gains its carrier row, §4's derivation becomes `git grep -l` filtered to the
  carriers `check-kit-versions.sh` grades, §7 gains `verdict epoch (kit version dates the engine)`,
  and AC13 observes both legs with the attribution corrected — an unbumped constant reds `verdict
  epoch`, not `kit version markers`. From the class sweep rather than from a named finding: S9 and
  AC14 for the check-12 catalog entry in the HYGIENE pair, which had no scope item and no observer at
  all (H2/H4 class); S1's shipped-conf comment and AC10's second grep (M6 class); AC12 for blank
  meaning off, which S1 declared and no criterion exercised (M10 class); AC6 restated to cover both
  doc pairs; §5's `fail 12` call-site count dropped for the property that does not depend on it (L1
  class); §5's user-docs row rewritten from `N/A`. Swept and absent, each re-checked rather than
  assumed: no `path:line` citation survives anywhere in this file (H9, M1, M2, M3, L2); every command
  and flag named in §6 was run or read at source before rev-4 shipped, including that
  `kit-dogfood-parity.test.sh` with no argument asserts parity and covers both doc pairs (H6, H7); no
  design argument rests on the shape or behaviour of code a LOWER-`order` sibling restructures, units
  1 and 2 touching neither the fence machine nor the witness block (H10, M5); every §7 entry is a
  `tools/gate-legs.json` leg name (M4); no criterion offers a whole-corpus green as its proof, AC8
  lowering the cutoff and AC7 reading the announcement in both directions (M7); the zero-population
  line goes to stdout like every sibling announcement and this spec prescribes no header contract
  (M8); the claims this spec makes about siblings were re-read against their own rev-3 text (M9); and
  no criterion grades a retrieval result the edit does not drive (H8).
- rev-5 · 2026-09-05 · §2 · §3 · §4 · §6 · §7 · folded spec-audit round 3, the TERMINATING fold:
  there is no round 4, so every item below is fixed here or has a stated destination. H2: S10, a
  Files-touched row, AC15 and the `kickoff-manifest ratchet` leg carry the
  `memory/guides/SESSION-KICKOFF.md` `last-audit` re-stamp. S1 and S4 edit
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`, both read off that manifest's
  own `watch:` line, and check C5 `no unaudited watch drift` is the observed red; `last-body-change`
  does not move, with the reason stated rather than assumed. B1's unit-3 half: §4's binding paragraph
  becomes this build's namespace REGISTER, as a table — it had named `TOOL-aJoinedCanon-4` as the sole
  claimant of `mcut` while `TOOL-aJoinedCanon-1` was taking it three `order` steps earlier, which is
  the fact that made the blocker invisible. The table now carries `revscopecut`, `jcut`, `fmcut`,
  `edgecut`, `rrows`/`rcut` and `bcut` against their keys, each read off the sibling's own current
  text and not remembered, with check 23's `lcut`/`tcut` recorded as the separate namespace they are;
  the nine pre-existing names were re-verified on the engine's `bad12_raw=` line. The register also
  states its own rule — claim here first, CITE this table rather than copy it, since the three siblings
  that copied it instead all still say `mcut` — declines to restate the `tFixture` space the README allocates by
  formula, and records the one thing no round can now settle: `TOOL-aJoinedCanon-1` builds the
  duplicate-`-v` self-test as its AC16 while `TOOL-aJoinedCanon-4`'s §3 routes that arm to a backlog
  row. `TOOL-aJoinedCanon-8` claimed `edgecut` during this same fold, having named no spelling at
  rev-4, and its row went in on a re-scan rather than on the first pass. PROMOTED, not parked: §3
  gains the disposition of round 3's four left-shifts that name this arm as their mechanism — the
  Files-touched join (H2's second half, M4), the criterion-to-fixture reverse join (H5) and
  clause-level coverage (M7) — each walking a population this arm does not, so each goes to a `TOOL`
  backlog row opened at this build's landing, named there and not numbered here. Re-read table fired
  §2→§3,§6 and §4→§2,§6,§7 and §6→§2,§7 and §7→§6. It caught two things a per-section edit
  would have left: §7's "checked against that manifest at rev-4" stamp, which had to move with the
  leg added on the line above it, and AC15, which §2→§6 forced rather than letting S10 ship as the
  unobserved scope item this unit's whole subject is. RUN, not asserted:
  `bash skills/session-kickoff/manifest-check.sh` exits 0 on the unedited tree, so AC15's red will be
  this edit's; that leg's `argv`, `subject: repo` and absent `guard` were read out of
  `tools/gate-legs.json`; and §4's three pre-change baselines were re-measured and are still 0 in
  both halves of each pair.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "walk numbered items in a spec section and grade each
item's own text"` returned 645 symbols, 188 inventory keys, 19 affordance seams and 20 dossiers, and
its ranked candidates were `extract_section` in `tools/check-spec-tokens.py` and `parse_spec` in
`tools/memory-tree/gen_build_index.py`. Neither is the seam. The seam this unit extends is not in
the symbol index at all, because it is an inline awk block rather than a named function: the
acceptance-witness label walker in `tools/memory-tree/check-memory-hygiene.sh`, the block that ends
in the print naming `SPEC_WITNESS_CUTOFF`, which
already solves continuation lines, the three sanctioned label spellings and the phantom-head bug
that a cross-reference on a continuation line used to cause. This unit is that walker with a
different heading, a different label prefix and a different per-item predicate. The recall probe
also surfaced `memory/builds/cTracedPromise/spec/2026-08-15-spec-cTracedPromise-2.md`, the spec that
built that walker, which is the shape precedent for this one; and review M13 in
`memory/builds/dUnstalledConvoy/reviews/2026-08-20-review-TOOL-dUnstalledConvoy-1-1.md`, which is why
§4 keys on heading text.

Recall terms used: `spec format check 12 acceptance witness cutoff scope item criterion join awk
label walker grandfather ratchet`, passed to `python tools/memory-recall/query.py` with the question
"why does the spec format number scope and acceptance items without joining them".
