# TOOL-aJoinedCanon-3 — a scope item names the criterion that observes it

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-2 · base 750ca0ca · streams tooling · order 3 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

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
  `tools/memory-tree/.memory-tree.conf.example`. Blank means off, taking `STREAMS_CUTOFF`
  semantics rather than `SPEC10_CUTOFF`'s forward resolution. Observed by AC3, AC7 and AC10.
- **S2** — the rule stated in `tools/memory-tree/SPEC-TEMPLATE.template.md`: one paragraph in the
  skeleton's §2 body, under the line beginning `What this unit builds, as a bounded numbered list`,
  parallel to the acceptance-witness paragraph that opens `Once a spec's filename date reaches
  SPEC_WITNESS_CUTOFF`, plus a clause on the numbering bullet that begins `Number scope and
  acceptance items`. Observed by AC6 for the render and AC9 for the content.
- **S3** — `memory/TEMPLATE-SPEC.md` re-rendered from that template, never hand-edited. Observed by
  AC6, and only in company with AC9: a byte-compare is equally green when neither half moved.
- **S4** — a new branch in check 12's awk body, placed after the acceptance-witness arm, whose last
  statement prints `acceptance bullets naming no backticked witness`, and therefore above the
  Tier-1 cut, the `if (hdr ~ /Tier-1/) next` line that opens the section canon.
  It walks §2's column-0 items and reports every item whose own text names neither an `AC<n>` token
  nor the escape. Observed by AC1, AC2 and AC4.
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

Three things follow. The corpus passes this predicate at 3.4%, so the cutoff carries everything and
the arm grades no landed spec on day one — S6 exists because of that number. The escape spelling is
unclaimed, so it cannot pass an item by accident. And grading the bullet rather than the label costs
61 items over the corpus, which is the price of not being opt-out-able by deleting two characters.

The last two rows are the pre-change baselines AC9 and AC10 need. Both are 0 today, so neither grep
can be green before the edit lands — which is the whole difference between those two criteria and a
byte-compare that is equally green when nothing moved.

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
| `tools/memory-tree/check-memory-hygiene.sh` | the arm, its `-v` binding on check 12's awk invocation, the default, the announcement |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the fixtures and their `hit`/`miss` assertions |
| `.memory-tree.conf` | the declaration |
| `tools/memory-tree/.memory-tree.conf.example` | the same key, blank |

Both template halves move in one commit: `tools/memory-tree/kit-dogfood-parity.test.sh` renders
TEMPLATE to LIVE and byte-compares, so editing either alone reds `kit/dogfood doc parity`. The
direction is stated at that file's header and the render is
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.

The commit also owes a `gov:kit memory-tree@` version bump in EVERY carrier. Derive the carrier set
with `grep -rl 'gov:kit memory-tree@'` and never from a remediation message: backlog row
`TOOL-dSettledRoster-4` records that message naming three carriers when six exist, and records the
same defect being hit twice, the second time costing a full extra bar cycle.

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
  disables the branch. A spec with only one of the two headings, or a §2 with no column-0 bullet, is
  silent rather than red.
- observability — the message names the cutoff, the file and every offending item. The zero-
  population announcement prints whenever the arm grades nothing.
- risks (concurrency, data-loss, rollback hazards) — none to data. The rollback is blanking the
  conf key, which turns the arm off without touching a spec. The live risk is a false red on a
  legal spec shape, which is what the pre-wiring corpus run and the Tier-1 fixture exist to bound.
- testing + left-shift gates — the fixtures in S7 are the coverage, because the corpus exercises
  nothing on day one. `check-arms.py` cannot force them: check 12 aggregates every awk finding into
  one `fail 12` call site, the `[ -n "$bad12" ] && fail 12` line in
  `tools/memory-tree/check-memory-hygiene.sh`, so the arm requirement
  does not reach a new awk branch and the discipline is this spec plus build rule 4.
- migration / rollback — see §4. No spec is edited.
- user docs — N/A. The template IS the user doc for this rule and S2 changes it.

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
  proving `memory/TEMPLATE-SPEC.md` matches `tools/memory-tree/SPEC-TEMPLATE.template.md` rather than
  having been hand-edited. It grades SAMENESS, and is equally green when neither file was touched, so
  it observes S2 and S3 only in company with AC9, which supplies the content half.
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
  after the edit it exits 0, and `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0 with
  its engine-preset parity arm satisfied. The key is absent today, per §4, so the grep is red before
  the edit and that self-test arm reds from the moment the engine gains the preset until the shipped
  example declares it — the third of S1 that no criterion previously reached.

## 7. Gates

- `memory hygiene` · `memory-hygiene self-test` · `kit version markers`
- `harness arms (fail branches armed or pinned)` · `spec tokens (a spec's own names resolve)`
- `kit/dogfood doc parity`

The first two are the arm's own bar. `kit/dogfood doc parity` is what makes the two template halves
one edit. `kit version markers` reds if any `gov:kit memory-tree@` carrier is left behind. This unit
adds no new leg; the arm lives inside check 12, which is already on the bar.

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
