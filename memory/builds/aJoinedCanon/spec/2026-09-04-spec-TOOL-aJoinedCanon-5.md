# TOOL-aJoinedCanon-5 — a criterion declares what it needs before it can be observed

**Status:** CLOSED · rev-5 · 2026-09-06 · node a · Tier-1 · base 750ca0ca · streams tooling · order 5 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aJoinedCanon-1-acceptance-ledger.md](../build/2026-09-06-build-TOOL-aJoinedCanon-1-acceptance-ledger.md) | journal | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 TOOL-aJoinedCanon-11 |

<!-- /gen:spec-records -->

## 1. Goal

§6 asks for an observation and never asks what the observation needs before it can be made. Add an
instructional block to §6 telling an author to declare a criterion's preconditions as four named
sub-fields — its `cost:`, its `permission:`, the `fixture:` or live instance it needs, and whether a
`figure:` it states is derived or pinned — and add one Writing rule stating the derived-or-pinned
obligation for every measured number a spec pins, in any section, of which `figure:` is §6's
instance. Finding
A5 of `memory/builds/aWeighedCanon/build/2026-09-04-build-TOOL-aWeighedCanon-2-what-the-spec-format-is-missing.md`
measured 81 acceptance criteria amended at build time across 32 records, and 37 of them trace to one
of those four things going unsaid.

## 2. Scope (IN)

- **S1** — An instructional block added to §6 of `tools/memory-tree/SPEC-TEMPLATE.template.md`,
  inside the skeleton fence, naming the four preconditions as four named sub-fields — `cost:`,
  `permission:`, `fixture:`, `figure:` — written as lines under the criterion's own bullet, and
  stating that a field which does not apply is OMITTED rather than written as `none`. Observed by
  AC7 for the four spellings and AC2 for the cost-and-permission silence the finding measured.
- **S1b** — One bullet added to the `## Writing rules` list of the same file, OUTSIDE the skeleton
  fence, stating that a measured number a spec pins says whether it is DERIVED or PINNED, in any
  section. This is the owner's ruling of 2026-09-05 on §8's F2, against this spec's own
  recommendation of §6 alone. That bullet OWNS the obligation; §6's `figure:` field points at it and
  restates none of it, which is the ownership decision §4 records. Observed by AC6.
- **S2** — Both edits present in `memory/TEMPLATE-SPEC.md`, produced by re-rendering the twin
  rather than by hand-editing the live copy. Observed by AC1, which grades SAMENESS and nothing
  else, in company with AC2, AC6 and AC7, which read the rendered content.
- **S3** — This spec's own §6 written in the shape S1 proposes, so the first instance of the rule
  exists in the tree on the day the rule lands rather than being asserted about a future author.
  Observed by AC5.

## 3. Non-goals (OUT)

- **No arm, no gate leg, no cutoff key.** §7 states why. A follow-up is named there and only there.
- **No retrofit.** Nothing in the 479-spec corpus is edited, and no landed spec goes red — there is
  no predicate for one to fail.
- **Not the failure-mode question.** "What would turn this criterion red" is `TOOL-aJoinedCanon-4`.
  A precondition is what the observation NEEDS; a break is what it would SHOW. Sibling units, and
  both land in §6, which is why they are sequenced rather than parallel.
- **Not §7's arm-location question.** Where a new gate's arm lives is `TOOL-aJoinedCanon-7`, and the
  overlap is deliberate: a criterion may declare that its arm's suite is one this run may not
  execute, which is this unit's `permission:` field, while unit 7 owns where the arm is written.
- **Not the ledger side.** This changes what a criterion declares, never what an acceptance ledger
  answers. `TOOL-aJoinedCanon-6` owns the join.
- **No new §5 row.** The production-readiness row set is `TOOL-aJoinedCanon-9`'s subject.
- **No edit to any other skeleton section.** The Writing rule added by S1b binds every section,
  which reads as licence to add a matching line to §4's skeleton prose about its inventories and
  estimates. It is not. The rule has one home and §6 has the one pointer at it; a third carrier in
  §4 would be the two-copies drift this build exists to close, one section over.

## 4. Design

### The four preconditions, and the evidence for each

| Field | The question §6 does not ask | Evidence |
|---|---|---|
| `cost:` | What does making this observation cost, when it is not seconds? | 23 of 81 amendments were over cost or permission. `grep -ciE 'cost\|budget\|minutes\|hours' memory/TEMPLATE-SPEC.md` returns `0` — verified 2026-09-04, and the silence is total. |
| `permission:` | May THIS run execute the thing that observes it? | Same 23. The unrunnable suite and the boundary an unattended run may not cross are both this class. |
| `fixture:` | Does the tree contain the live instance this observation needs? | 6 amendments named one it did not contain. `TOOL-dHonouredPark-4` AC10 is the worked case: "zero tracked specs produce a heading whose id does not parse, so the condition has no live instance and its fixture is in the unrunnable suite." |
| `figure:` | Is a number this criterion states re-derived at observation time, or typed as a literal? | 8 amendments pinned a measured literal that was stale by build time. `TOOL-aNamedGesture-1` AC13 is the worked case, and its repair is the rule: "The witness is now the command, not a number." |

The `figure:` row is the one of the four whose rule is not §6's alone, and the next sub-section says
which document owns it.

23 plus 8 plus 6 is 37 of the 81. The cost and permission pair is the largest class that bins, and
that qualifier is load-bearing: 33 of the 81 resist binning, so nothing here claims a largest cause
overall. The four are one mechanism because they answer one question — what this criterion needs
before it can be observed — and BUILD-METHOD M2 allows a unit exactly one.

### The shape: four named sub-fields

Four named lines under the criterion's own bullet, not one `Preconditions:` line. This is the
owner's ruling of 2026-09-05 on §8's F1, against this spec's own recommendation, and the reason is
the one F1's losing side conceded: four names read as a checklist and are what a future arm would
grade, where one line is prose that happens to start with a word.

An author writes only the fields that APPLY and omits the rest. A field that does not apply is
absent, never written as `none` — the four names are questions the template asks, not blanks a
bullet must fill, and a criterion carrying none of them is the common case rather than an
under-filled one. That property is not a residue of the losing branch: it is the axis F1 never
disputed, and §7 depends on it.

### Which document owns the derived-or-pinned rule

The owner ruled on 2026-09-05 that the rule lands in BOTH §6 and the Writing rules, overruling this
spec's recommendation of §6 alone. That widening carries a cost this spec named while recommending
against it: the unit now writes to two places in one document, and two copies of one rule in one
document is exactly the drift this build exists to close. So ONE of the two locations owns the rule
and the other points at it, the same one-text-one-home split `TOOL-aJoinedCanon-2` makes when the
fold clause `Review corrections fold in here; bump the header rev and log it in §9.` in
`tools/memory-tree/SPEC-TEMPLATE.template.md` becomes a pointer at BUILD-METHOD M4.

**The Writing rules OWN it. §6's `figure:` field is its instance and restates none of it.** The
decision is by READER, not by subject. A Writing rule is read by an author filling ANY section; the
§6 block is read only by an author filling §6. The rule the ruling widened to is precisely one that
binds outside §6 — a §4 inventory or estimate pins measured literals too — so a home only a §6
author reads cannot carry it. The reverse split fails on the same test: a general rule parked in §6
would have to be restated for §4 to reach it, which is the second copy.

That relationship is spelled in both directions rather than left to inference. The Writing rule
names `figure:` as the field an acceptance criterion answers it in, and §6's `figure:` bullet names
the Writing rule as where the obligation lives. Neither says what the other says. What §6 keeps is
the FIELD — its spelling, and that it answers derived-or-pinned for a number the criterion states;
what moves out is the obligation and its reason, which used to trail that bullet as the clause
"a pinned literal names when it was measured, because the writing rules verify at writing time".
Under F1's ruling the four sub-fields already put a derived-vs-pinned answer in §6, so the Writing
rules half is not a duplicate of `figure:`: it is the general statement of which `figure:` is one
instance.

### The text

Two blocks, in two places, saying different things. First, inside the §6 skeleton block, after the
acceptance-witness paragraph:

```
A criterion that cannot be observed for free, by this run, or against today's tree says so with the
criterion instead of leaving the next session to discover it. Four things go unsaid and get paid for
in build-time amendments. Declare whichever of them apply as named lines under the criterion's own
bullet:

- `cost:` — what the observation costs, when it is not seconds.
- `permission:` — the suite, boundary or credential that observes it is one THIS run may not execute.
- `fixture:` — the live instance or path the observation needs, and whether the tree holds one today.
  A criterion observing a gate arm names every cutoff key its fixture conf arms: an arm sitting
  inside a second key's guard is graded by nobody when that second key is blank, and the fixture
  that arms both cannot tell you so.
- `figure:` — whether a number the criterion states is DERIVED at observation time or PINNED as a
  literal. The writing rule on measured numbers states the obligation; this field is where a
  criterion answers it.

Write only the fields that apply and OMIT the rest. A field written as `none` is a blank being
filled rather than a question being answered, and a criterion whose preconditions are all trivial
carries no fields at all — the common case. Nothing grades these lines.
```

Second, one bullet in the `## Writing rules` list, placed under the existing
`Verify every claim about existing code against source at writing time` bullet whose seam it closes:

```
- A measured number a spec pins says whether it is PINNED or DERIVED. The rule above verifies at
  WRITING time, so a number true when written goes stale in place and nothing re-checks it: a pinned
  one names when it was measured, a derived one names what re-derives it. This binds every section,
  §4's inventories and estimates included; §6's `figure:` sub-field is where an acceptance criterion
  answers it.
```

Wording is indicative, not byte-exact; the reviewed diff is the authority. The four spellings are
not indicative: they are the owner's, and a rendering that spells them otherwise has not landed the
ruling. The ownership direction is not indicative either — a second copy of the obligation under
`figure:` is a failed landing of F2's ruling, not a stylistic variant of it.

### Where it goes, and why that placement is not arbitrary

Inside the skeleton, after the witness paragraph and before the author's own bullets. At `order` 4
`TOOL-aJoinedCanon-4` adds its own `Red when:` paragraph to this same block, so this one follows
that: two instructional paragraphs, one placement question, and the later-`order` unit is the one
that has to know.

Verified against the block under `# ---- acceptance witnesses:` in
`tools/memory-tree/check-memory-hygiene.sh`: the acceptance-witness arm sets `lab` only on a line
matching its AC-label regex and appends every later line to `acc` until the next label or the next
`## `. Instructional prose sitting ABOVE an author's first bullet is therefore read with `lab` empty
and can satisfy nothing. Prose left BELOW an author's last bullet would fold its backticks into that
bullet's witness blob, which is why the paragraph joins the existing §6 instructions rather than
trailing the section. The hazard is pre-existing and unchanged in kind — the two paragraphs already
there carry backticks — and it is recorded because a later editor moving this text down would
silently weaken the witness arm.

**That verification was made against a structure `TOOL-aJoinedCanon-4` restructures first, and it is
re-run at build time rather than trusted.** Unit 4's S3 HOISTS this accumulator out of the
`if (wcut != "" && fdate != "" && fdate >= wcut) {` guard it sits in today, so at `order` 5 the loop
runs under different conditions and at a different indent. Nothing above depends on the guard — the
argument is about where `lab` is set and what `acc` swallows, and the hoist moves neither — but
"nothing depends on it" is a claim about code that has changed, so re-read the hoisted loop before
placing the paragraph and correct this sub-section if the `lab` semantics moved with it.

Two consequences of the four-field shape land on that same arm, and both were checked against the
source rather than assumed. The block's own field-name bullets cannot be misread as criteria: the
label regex — the line matching `AC[0-9]+[a-z]?` after an optional list marker — requires that
label, so a field-name bullet is instructional prose like the paragraphs beside it. And a sub-field
line under a real criterion IS appended to that criterion's witness blob, because `acc` accumulates
every line until the next label — so a bullet whose only backticked token sits in its `fixture:`
line satisfies the witness arm while the criterion sentence itself names nothing. That was already
true of any continuation line and is not a regression, but four permitted lines widen the surface,
and an author reading this should put the witness in the criterion and let the fields add to it.

The Writing-rules bullet sits OUTSIDE that fence, in the list under the `## Writing rules` heading,
and none of the paragraph above reaches it. The witness arm scans a spec's own §6, and the Writing rules are
never copied into a spec — they are read while writing one. So the second half carries no arm
interaction at all, and its only placement constraint is the one it takes for free: it goes directly
under the writing-time verification bullet, because it is that bullet's seam and a reader must not
have to hold the two apart.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | The authored source, in TWO places: the §6 block inside the fence, the Writing-rules bullet outside it. Edit here. |
| `memory/TEMPLATE-SPEC.md` | Re-rendered from the twin, never hand-edited. |

**F2's ruling widened the text and did not widen this table.** Both halves land in the same two
files, so the unit still touches two paths, adds no code, crosses no contract and moves no gate —
which is why the header stays Tier-1 after the fold rather than moving with the scope.

**No version bump is owed, and that was checked rather than assumed.** Both shipped templates carry
a `gov:kit memory-tree@` marker that `tools/check-kit-versions.sh` compares against
`KIT_MEMORY_TREE_VERSION`, so editing a template body while leaving the constant alone keeps that
leg GREEN — every carrier still agrees. `tools/memory-tree/check-verdict-epoch.sh` scans the engine
and its named delegates for behaviour-bearing lines, and this unit touches none of them: it adds no
arm and moves no verdict. Sibling units that DO change the engine owe both legs; this one owes
neither, which is why no version carrier appears in the table above.

Roughly 1,450 B added to each. That figure is PINNED — an ESTIMATE from the draft text above and
not a measurement — and the pre-change sizes are deliberately not pinned beside it, because AC4
derives the before-and-after pair at observation time and a byte count typed here is stale the
moment any of the five lower-`order` units re-renders the pair. The estimate rose from rev-1's
roughly 900 B for the four named fields, and again at rev-3 for F2's
Writing-rules bullet net of the clause that bullet takes out of `figure:`. Verified 2026-09-04
that no size gate binds either file: neither has a row in
`tools/template-size-limits.txt`, and `bash tools/memory-tree/check-memory-hygiene.sh
--print-index-set` does not list `memory/TEMPLATE-SPEC.md`, so check 6's per-class caps do not
reach it.

### Migration

None. No cutoff key is declared, and that is compliance with this build's dated-cutoff rule rather
than an exception to it: a cutoff exists so a new machine-graded demand cannot red landed work, and
this unit adds no machine-graded demand. Declaring one would put a key in `.memory-tree.conf` that
no arm reads — a key that reads as armed with nothing behind it, which is the mirror image of the
defect `TOOL-aJoinedCanon-10` repairs rather than the same one. Unit 10's key IS read by the engine
and is missing from this repo's conf; this one would be present and read by nothing. Both directions
break the same join, and this build's dated-cutoff rule forbids the second as plainly as unit 10
repairs the first.

### Alternatives rejected

- **A fifth `##` section for preconditions.** The template forbids additional `##` headings and
  check 12 compares the section list for equality, so this is a new canon and a new dated cutoff for
  a paragraph. Rejected on cost.
- **One `Preconditions:` line per criterion.** This spec's own recommendation in §8's F1, and
  OVERRULED by the owner on 2026-09-05. Recorded here as the rejected alternative it now is; the
  argument for it, and the cost the ruling accepts, stay in F1 rather than being re-litigated here.
- **A required field set plus an arm that demands all four per bullet.** Rejected: four names that
  have nothing to say get typed as `none` across the corpus's AC lines — 1,404 of them, PINNED as
  measured 2026-09-04 at base `750ca0ca`, and rising as this build's own eleven specs add criteria —
  and the gate then measures typing.
  This is the same rejection rev-1 made against a required `Preconditions:` line, and the ruling
  makes it four times louder rather than retiring it. §7.
- **The derived-or-pinned rule in §6 ALONE.** This spec's own recommendation in §8's F2, and
  OVERRULED by the owner on 2026-09-05. It leaves a §4 that pins stale literals unaddressed, which
  the fork text conceded while recommending it. The argument stays in F2 rather than here.
- **The same text in both places.** The obvious way to obey "both", and the one thing the ruling
  cannot have meant: two carriers of one rule in one document is the class this build closes. The
  ownership split above is the answer instead.
- **§6 owning the rule, with the Writing rules pointing at it.** Rejected on reader: a §4 author
  never opens §6's skeleton instruction, so the general obligation would have to be restated there
  to reach them, and the restatement is the second copy again.

## 5. Production-readiness checklist

- security — N/A. A documentation paragraph in a tracked template; no write path, no input, no
  surface.
- perf / scale — N/A. No code runs. The byte cost is in "Files touched" and no size gate binds it.
- a11y — N/A. No user interface.
- i18n — N/A. Single-language repo documentation.
- error / empty / loading states — N/A. Nothing executes.
- observability — N/A. Nothing emits.
- risks — Two, both documentation risks, both recorded in §4 where an editor reads them. A later
  editor moves the §6 paragraph below an author's bullets and weakens the acceptance-witness arm.
  And a later editor, finding §6's `figure:` bullet terse, restates the Writing rule's obligation
  under it — which turns the pointer into the second copy F2's ruling was resolved to avoid, and is
  the more likely of the two because it looks like an improvement. Rollback is a revert of the same
  two files it was before the ruling, and the twin parity gate refuses a revert of only one.
- testing + left-shift gates — **No gate, deliberately, and this row names the compensating check.**
  A `cost:` label is greppable — that is what the ruling's four names buy — but "did the author
  declare the cost TRUTHFULLY, and did they notice they had one" is not mechanically distinguishable
  from prose, so no arm is written and none is claimed. The Writing-rules half is even further from
  gradeable — it sits outside the skeleton fence, so no spec-scoped arm reaches it at all. The
  compensating check is a re-measurement, not a review pass: after
  five more builds close, re-run finding A5's method — count acceptance criteria amended at build
  time, bin them by cost, permission, fixture and stale literal, and compare against the 23, 6 and 8
  recorded here. F2's ruling widens that re-measurement rather than only its subject: the stale-literal
  bin is counted over §4's pinned figures as well as §6's, because a rule that now binds every section
  is not measured by a count taken in one. If the classes have not moved, this unit did nothing and
  should be reverted rather than reinforced. That check is manual, deferred, and owned by whoever next
  audits the spec format; it is filed as a backlog row at build time, not asserted here as done.
- migration / rollback — See §4. No cutoff key, no corpus edit, no state to migrate.
- user docs — N/A. `memory/TEMPLATE-SPEC.md` IS the document; there is no separate `help/` page for
  the memory-tree kit's own rule set.

## 6. Acceptance criteria

*This section is written in the shape S1 proposes, which is the owner's ruling of 2026-09-05 on
§8's F1 and not this spec's recommendation. Each criterion carries only the sub-fields that apply,
and AC5 shows what the omission looks like in practice. AC6 observes S1b, the second carrier F2's
ruling added on the same day, and AC7 observes that the four spellings the ruling names actually
reached the rendered file — the content half AC1's sameness compare cannot supply.*

- **AC1** — When the block is added to `tools/memory-tree/SPEC-TEMPLATE.template.md` and the live
  copy is re-rendered, `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0, proving
  `memory/TEMPLATE-SPEC.md` matches the template rather than having been hand-edited. It grades
  SAMENESS, and is equally green when NEITHER file was touched, so it observes S2 only in company
  with AC2, AC6 and AC7, which supply the content half.
  fixture: the live copy must be the RENDERED one, so `--render` must have been run; a hand-edited
  `memory/TEMPLATE-SPEC.md` fails this criterion rather than satisfying it.
- **AC2** — When `grep -ciE 'cost|budget|minutes|hours' memory/TEMPLATE-SPEC.md` is run after the
  change, it returns a count greater than the `0` it returned before.
  figure: the `0` is DERIVED, measured on this branch at base `750ca0ca` on 2026-09-04 and re-run
  unchanged at HEAD `7ad96e60` on 2026-09-05, not inherited from the finding; re-derive it on the
  pre-change tree if the after-count is disputed.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the whole tree, it exits
  0, and no spec in `memory/builds/*/spec/` is newly named by check 12. **This green is a regression
  guard and not an observation of the added text, and the difference is stated because a green that
  cannot fail reads like coverage.** The section canon is the hardcoded `SPEC_CANON` constant in
  `tools/memory-tree/check-memory-hygiene.sh`, not a list read from the template, so no edit to the
  template can red a landed spec through this check — verified at source rather than assumed, and it
  is the opposite of what an earlier draft of this criterion claimed. The hazard a `## ` heading in
  the added block WOULD create is a template skeleton that disagrees with that constant, which reds
  the next author's spec and not this landing; nothing in §6 catches it, and the diff review does.
  cost: minutes rather than seconds on this node, which is exactly why the cheaper `--staged` form
  does not substitute — it grades only the diff and would report a green that means nothing here.
- **AC4** — When `wc -c` is taken over both files before and after, the growth is reported as the
  measured pair rather than as §4's estimate.
  figure: DERIVED at observation time. §4's roughly 1,450 B is a pinned estimate, restated at rev-3
  for F2's second block, and is not what this criterion grades.
- **AC5** — When this spec is read at close, its own §6 still carries named sub-fields on the
  criteria that need them, so `git grep -cE '^ +(cost|permission|fixture|figure):' -- memory/builds/aJoinedCanon/spec/2026-09-04-spec-TOOL-aJoinedCanon-5.md`
  returns a non-zero count. This is S3's observation and it is deliberately weak — it grades
  presence, exactly as the witness arm does, and claims nothing about whether the declarations are
  true. No sub-field applies to it, so it carries none, which is the omission rule being obeyed
  rather than a criterion left under-filled.
- **AC6** — When `sed -n '/^## Writing rules/,/^## Tier profiles/p' memory/TEMPLATE-SPEC.md | grep -c PINNED`
  is run after the change, it returns a count greater than the `0` it returns before, so the second
  carrier F2's ruling requires exists and is in the Writing rules rather than only in §6. AC1
  through AC5 all observe the §6 half; without this one the wider placement ships ungraded.
  figure: the `0` is DERIVED, re-run on this branch on 2026-09-05 at HEAD `7ad96e60` and again at
  base `750ca0ca`; both return `0`, and they agree because the two template files are byte-identical
  across that range. **The range is scoped for the AFTER direction, and rev-4's stated reason for it
  was false of this command.** That reason claimed an unscoped grep "would not fail before the
  change" because the whole-file count of `PINNED` or `DERIVED` is not `0`. This command greps
  `PINNED` alone, whole-file `grep -cF PINNED` returns `0` too, and the single whole-file `DERIVED` —
  the `order` bullet ending `DERIVED from this field, which is why the order belongs on the spec and
  not in README prose.` — sits outside the Writing-rules range, so the scoping does not exclude it
  either. The true reason is the other direction: S1's own §6 block contains the word `PINNED`, so
  after the change an unscoped grep goes non-zero from the §6 half alone and would read green with
  S1b never written. Scoping the range is what makes this criterion observe S1b rather than S1.
  fixture: a no-match `grep -c` exits non-zero while printing `0`, so this reads the printed count
  and never a `&&` chain's exit status.
- **AC7** — When
  ``sed -n '/^## 6. Acceptance criteria/,/^## 7. Gates/p' memory/TEMPLATE-SPEC.md | grep -cE '`(cost|permission|fixture|figure):`'``
  is run after the render, it returns 4 — one for each spelling the owner's F1 ruling names, inside
  the §6 skeleton block rather than anywhere in the file.
  figure: the pre-change count is DERIVED, measured as `0` on this branch at base `750ca0ca` and
  re-run unchanged at HEAD `7ad96e60`, both on 2026-09-05, so this cannot be green until the four
  fields exist. AC2's whole-file `cost` grep is
  the finding's own silence measure and reaches one of the four; this criterion is the one that
  fails when a rendering spells them otherwise, which §4 calls a failed landing of the ruling.

## 7. Gates

Kept green, by name from `tools/gate-legs.json`: `memory hygiene`, `kit/dogfood doc parity`. Both
spellings were read out of the manifest rather than typed from memory, and the whole bar —
`bash tools/run-gates/run-gates.sh` — is the DoD's invocation rather than a third leg name.

**`kit version markers` and `verdict epoch (kit version dates the engine)` are NOT owed, and that
was checked at source rather than left silent.** Every sibling unit touching the engine carries
both; this unit touches no engine file, so `verdict epoch` sees no behaviour-bearing line move, and
editing a template body without moving `KIT_MEMORY_TREE_VERSION` leaves every `gov:kit
memory-tree@` carrier in agreement, so `kit version markers` stays green on its own terms rather
than by omission. §4's Files-touched note carries the same finding where a builder reads it.

**The two cross-unit rules this build added after round 3 were both checked against this unit's
write set, and neither binds it.** It introduces no awk binding, no function name and no fixture
number, so it claims nothing in `TOOL-aJoinedCanon-3`'s namespace registry and cannot collide with a
sibling on the check-12 invocation — it writes no arm at all. And neither
`tools/memory-tree/SPEC-TEMPLATE.template.md` nor `memory/TEMPLATE-SPEC.md` appears in the `watch:`
line of `memory/guides/SESSION-KICKOFF.md`, read out of that file on 2026-09-05, so no `last-audit`
re-stamp is owed and `kickoff-manifest ratchet` stays green without one. Both checks are recorded
rather than left silent, because eight sibling units DO edit a watched path and a reader comparing
specs must be able to tell a checked exemption from an overlooked obligation.

**This unit adds no gate, and neither ruling of 2026-09-05 changes that.** The charter binds a
new arm to an observed failing case, and there is no failing case to observe. Four named fields make
the LABEL greppable where one prose line did not — that is the ruling's gain and it is real — but a
criterion that needed a `cost:` line and omitted it is still byte-identical to one that correctly
carried none, because the omission rule is what makes the fields writable at all. An arm demanding
all four on every bullet would grade typing, not declaration, and would be satisfied by `cost: none`
four times over — the could-not-fail shape one level up, which §7 of the charter names, and the
ruling multiplies the blanks rather than removing them. §5's testing row carries the compensating
manual check instead of an arm, and that is the honest trade rather than a gap left open.

F2's Writing-rules half is further from an arm still, and the reason is worth stating rather than
folding into the sentence above. It sits outside the skeleton fence, so it is not copied into any
spec and no spec-scoped predicate can find it; what it binds is an author's judgement about a number
in §4 that no arm can distinguish from a number that was never measured. AC6 grades that the bullet
EXISTS, which is presence and nothing more, and the wider placement buys no gradeability the §6-only
branch would not have bought.

If a later unit finds a sub-shape that a machine can grade — a `cost:` figure that must resolve, a
`fixture:` path that must exist in `git ls-files` — it is a separate unit with its own dated cutoff
and its own observed red. The four named fields bring that day closer, which is the strongest thing
this spec will say for the shape it did not recommend. It is still not smuggled in here.

## 8. Open questions

- **F1 · One `Preconditions:` line, or four named sub-fields?** Four sub-fields (`cost:`,
  `permission:`, `fixture:`, `figure:`) read as a checklist and are what a future arm would grade.
  One line is what the corpus already writes when it writes anything: `TOOL-aMouldedFolio-2` carries
  a `Cost` row and an `Entry budget` row in a §5 table, in prose, unprompted. Four fields multiply
  ceremony across a population that is 1,404 AC lines today, and three of the four are empty on most
  criteria. **Recommendation: one line, written only when something applies, with the four names
  listed in the template's PROMPT so the author is asked all four and emits only what is true.** The
  prompt is the checklist; the line is the answer.
  RESOLVED (owner, 2026-09-05): four named sub-fields — `cost:`, `permission:`, `fixture:`,
  `figure:` — written as lines under the criterion's bullet, with a field that does not apply
  OMITTED rather than written as `none`. The recommendation above lost: the ceremony cost across
  1,404 AC lines was heard and did not outweigh the checklist reading and the gradeability a future
  arm would need. The body is rewritten to this shape at rev-2, and §9 names every section moved.
- **F2 · Does the derived-or-pinned rule belong in §6, or in the Writing rules?** Finding 24's eight
  amendments were all acceptance criteria, which argues §6. But the Writing rules already say
  "Verify every claim about existing code against source at writing time" and a stale figure is that
  rule failing at the seam it does not cover — a spec's §4 pins stale literals too, and a §6-only
  rule leaves those unaddressed. The cost of the Writing-rules placement is that this unit then
  writes to two places in the template, which the fold rule dislikes. **Recommendation: §6 for now,
  because that is where the measured evidence sits, with a one-clause pointer added to the Writing
  rules only if a later measurement finds the class outside §6.**
  RESOLVED (owner, 2026-09-05): BOTH §6 and the Writing rules. The recommendation above LOST, and it
  lost on its own reasoning: the fork text conceded that the Writing rules already demand
  writing-time verification and that a stale pinned figure is that rule failing at a seam it does not
  reach, and it conceded that a spec's §4 pins stale literals a §6-only rule leaves unaddressed.
  Waiting for a later measurement to confirm a gap the fork had already argued was there is not
  caution, it is a second measurement of a settled question. The cost the recommendation named —
  this unit then writing to two places in one document — is accepted and DESIGNED AROUND rather than
  ignored: §4 records which location owns the rule and which points at it, so the two places carry
  one text. The Writing rules own it; §6's `figure:` field is its instance. §9 names every section
  moved.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · folded the owner's ruling on F1: four
  named sub-fields (`cost:`, `permission:`, `fixture:`, `figure:`), omitted when they do not apply,
  overruling this spec's one-`Preconditions:`-line recommendation. §1's goal sentence and S1
  respecified to the four fields; §3's arm-location non-goal now names the `permission:` field; §4
  gained the shape section, moved the one-line form into "Alternatives rejected", raised the estimate to
  roughly 1,100 B, and recorded that a sub-field line folds into its criterion's witness blob; §5's
  testing row now concedes the label is greppable and the truth is not; §6 rewritten to the fields,
  including AC5, whose grep for `Preconditions:` would have matched nothing after this fold; §7
  restated against four blanks rather than one line. F2 had not been ruled on AT THAT POINT, so
  rev-2's header carried no `ratified`; rev-3 below resolves it and adds one.
- rev-3 · 2026-09-05 · §8 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · folded the owner's ruling on F2: BOTH
  §6 and the Writing rules, overruling this spec's §6-only recommendation, with the Writing rules
  OWNING the derived-or-pinned obligation and §6's `figure:` field pointing at it. §1's goal names
  both carriers; §2 gained S1b and S2 now renders both edits; §3 gained a non-goal refusing a third
  carrier in §4's skeleton; §4 gained the ownership sub-section, a second block in "The text", the
  out-of-fence placement note, three replacement rejected alternatives where the fork used to be
  carried, and a raised estimate of roughly 1,450 B; §5's risk row gained the restatement risk and
  its testing row widens the re-measurement past §6; §6 gained AC6 for the Writing-rules half and
  AC4's `figure:` line was corrected to the new estimate; §7 states why the second half is further
  from an arm than the first. The Tier field was re-checked and stays 1: both halves land in the
  same two files §4 already listed. This entry supersedes rev-2's closing clause, which recorded F2
  as unresolved and the header as unratified — true at rev-2, false now.
- rev-4 · 2026-09-05 · §2 · §4 · §6 · §7 · §9 · §10 · folded round 2's H10 and swept all 23 of its
  defect classes over this spec, which the round-1 fold never opened. **H10, the named finding:**
  every anchor into a file a sibling edits is now literal text — the accumulator is cited as the
  block under `# ---- acceptance witnesses:`, the label regex as the line matching `AC[0-9]+[a-z]?`,
  unit 2's fold clause and the `## Writing rules` heading by their own words, and AC6's existing
  DERIVED instance by the `order` bullet's sentence. The two byte baselines are dropped, because AC4
  derives the pair. §4's placement sub-section now says outright that its verification was made
  against a loop `TOOL-aJoinedCanon-4` hoists at `order` 4 and must be re-run before the paragraph
  is placed, and it states where this paragraph sits relative to unit 4's own `Red when:` block.
  **The classes that hit beyond H10:** the H2/H3/H5 false-observer shape — AC1 is restated as the
  SAMENESS compare it is and AC7 is added for the four field spellings, whose pre-change count in
  §6's skeleton range is a derived `0`; the H4/M10 join shape — S1, S1b, S2 and S3 gained `Observed
  by` tags, each true of the whole scope item; the H6 could-not-fail shape — AC3's failing case was
  written, then checked against `SPEC_CANON` and found FALSE, so AC3 now states that the canon is a
  hardcoded engine constant and that this green is a regression guard rather than an observation of
  the added text, which is M7's class in the same edit; the M9 shape — §4's Migration cited
  `TOOL-aJoinedCanon-10` for the inverse of unit 10's actual defect and now names both directions;
  the H1/M4 shape — §4 and §7 record that `kit version markers` and `verdict epoch` are not owed
  here and why, verified at both scripts' source. §4's `1,404` and §10's probe counts are now marked
  PINNED with the date they were measured, which is this unit's own rule applied to itself.
- rev-5 · 2026-09-05 · §6 · §7 · §9 · the TERMINATING fold, round 3 having exited the audit loop on
  convergence. **M6, the only finding against this unit:** AC6's `figure:` justified its scoped sed
  range with a premise that is false of the command AC6 runs. The premise said an unscoped grep
  "would not fail before the change"; the command greps `PINNED` alone, whole-file
  `grep -cF PINNED` returns `0`, and the one whole-file `DERIVED` sits outside the Writing-rules
  range and is not what the command matches. AC6 now states the true reason — S1's own §6 block
  contains `PINNED`, so an unscoped grep would go green from the §6 half alone AFTER the change, and
  the scoping is what makes AC6 observe S1b rather than S1. Every pre-change baseline this spec
  states was re-run rather than re-read: AC2's `0`, AC6's `0` and AC7's `0` all reproduce at HEAD
  `7ad96e60` and at base `750ca0ca`, which agree because the two template files are byte-identical
  across that range, and each of the three criteria now names the shas it was re-run at. §7 gained
  the check of the two cross-unit rules added after round 3: this unit introduces no awk binding to
  claim in unit 3's registry, and neither file it writes is a `watch:` path of
  `memory/guides/SESSION-KICKOFF.md`, so no `last-audit` re-stamp is owed. The fold's re-read set
  fired §6 → §2, §7 and §7 → §6: S1b's `Observed by AC6` tag and §7's "AC6 grades that the bullet
  EXISTS" sentence both survive unchanged, because M6 moved a justification and never the command.
  Nothing is left parked and nothing is promoted to a follow-up; the finding is disposed here.

## 10. Reuse audit

No existing seam fits, and the evidence is that the closest candidates are all the wrong kind of
thing. `python tools/codebase-map/reuse_lookup.py "declaring the preconditions an acceptance
observation needs before it can be run"` returned 645 symbols over 20 dossiers — both PINNED, from
one probe run on 2026-09-04 at base `750ca0ca` — and its ranked
candidates are code seams — `extract_declarations`, `read_declared_keys`, `load_declarations`,
`declared_in_kits_json` — every one of them a reader of a machine declaration in a conf or a
registry. There is no seam for a PROSE declaration in a template, because this unit adds no code and
extends no module. The document seams it does extend are both in
`tools/memory-tree/SPEC-TEMPLATE.template.md`: the §6 instructional block, which already carries two
such paragraphs and is the established home for a rule an author reads while filling the section,
and the `## Writing rules` list, which already carries the writing-time verification bullet this
one's second half extends. Neither is a new home; F2's ruling reuses both. The recall probe found the
corpus solving this by hand, one amendment at a time: `TOOL-aMouldedFolio-2` writes an unprompted
`Cost` row in its §5 table, and `TOOL-aNamedGesture-1` AC13's repair — "The witness is now the
command, not a number" — is this unit's derived-or-pinned rule, discovered at amendment cost by a
build that had no section asking for it.

Recall terms used: `acceptance criterion cost budget minutes fixture permission derived figure stale
literal precondition witness`, passed to `python tools/memory-recall/query.py "does any spec section
already declare an acceptance criterion cost, permission or fixture precondition"` for 38 hits,
PINNED from that same run.
