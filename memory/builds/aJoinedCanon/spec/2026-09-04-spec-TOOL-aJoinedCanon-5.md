# TOOL-aJoinedCanon-5 — a criterion declares what it needs before it can be observed

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-1 · base 750ca0ca · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

§6 asks for an observation and never asks what the observation needs before it can be made. Add one
paragraph to §6 telling an author to declare a criterion's preconditions — its cost, its permission,
the fixture or live instance it needs, and whether a figure it states is derived or pinned. Finding
A5 of `memory/builds/aWeighedCanon/build/2026-09-04-build-TOOL-aWeighedCanon-2-what-the-spec-format-is-missing.md`
measured 81 acceptance criteria amended at build time across 32 records, and 37 of them trace to one
of those four things going unsaid.

## 2. Scope (IN)

- **S1** — One paragraph added to §6 of `tools/memory-tree/SPEC-TEMPLATE.template.md`, inside the
  skeleton fence, naming the four preconditions and the one-line form that declares them.
- **S2** — The same text present in `memory/TEMPLATE-SPEC.md`, produced by re-rendering the twin
  rather than by hand-editing the live copy.
- **S3** — This spec's own §6 written in the shape S1 proposes, so the first instance of the rule
  exists in the tree on the day the rule lands rather than being asserted about a future author.

## 3. Non-goals (OUT)

- **No arm, no gate leg, no cutoff key.** §7 states why. A follow-up is named there and only there.
- **No retrofit.** Nothing in the 479-spec corpus is edited, and no landed spec goes red — there is
  no predicate for one to fail.
- **Not the failure-mode question.** "What would turn this criterion red" is `TOOL-aJoinedCanon-4`.
  A precondition is what the observation NEEDS; a break is what it would SHOW. Sibling units, and
  both land in §6, which is why they are sequenced rather than parallel.
- **Not §7's arm-location question.** Where a new gate's arm lives is `TOOL-aJoinedCanon-7`, and the
  overlap is deliberate: a criterion may declare that its arm's suite is one this run may not
  execute, which is a permission, while unit 7 owns where the arm is written.
- **Not the ledger side.** This changes what a criterion declares, never what an acceptance ledger
  answers. `TOOL-aJoinedCanon-6` owns the join.
- **No new §5 row.** The production-readiness row set is `TOOL-aJoinedCanon-9`'s subject.

## 4. Design

### The four preconditions, and the evidence for each

| Precondition | The question §6 does not ask | Evidence |
|---|---|---|
| Cost | What does making this observation cost, when it is not seconds? | 23 of 81 amendments were over cost or permission. `grep -ciE 'cost\|budget\|minutes\|hours' memory/TEMPLATE-SPEC.md` returns `0` — verified 2026-09-04, and the silence is total. |
| Permission | May THIS run execute the thing that observes it? | Same 23. The unrunnable suite and the boundary an unattended run may not cross are both this class. |
| Fixture | Does the tree contain the live instance this observation needs? | 6 amendments named one it did not contain. `TOOL-dHonouredPark-4` AC10 is the worked case: "zero tracked specs produce a heading whose id does not parse, so the condition has no live instance and its fixture is in the unrunnable suite." |
| Derived or pinned | Is a figure this criterion states re-derived at observation time, or typed as a literal? | 8 amendments pinned a measured literal that was stale by build time. `TOOL-aNamedGesture-1` AC13 is the worked case, and its repair is the rule: "The witness is now the command, not a number." |

23 plus 8 plus 6 is 37 of the 81. The cost and permission pair is the largest class that bins, and
that qualifier is load-bearing: 33 of the 81 resist binning, so nothing here claims a largest cause
overall. The four are one mechanism because they answer one question — what this criterion needs
before it can be observed — and BUILD-METHOD M2 allows a unit exactly one.

### The text

Added inside the §6 skeleton block, after the acceptance-witness paragraph:

```
A criterion that cannot be observed for free, by this run, or against today's tree says so with the
criterion instead of leaving the next session to discover it. Four things go unsaid and get paid for
in build-time amendments. The COST of the observation, when it is not seconds. The PERMISSION it
needs, when the suite or the boundary that observes it is one this run may not execute. The FIXTURE
or live instance it needs, and whether the tree holds one today. And whether a figure the criterion
states is DERIVED at observation time or PINNED as a literal — a pinned literal names when it was
measured, because the writing rules verify at writing time and a build outlives its own
measurements. Write one `Preconditions:` line under the bullet naming whichever apply, and omit the
line when none do. Nothing grades that line: §7 of this unit's spec says why, and a criterion whose
preconditions are all trivial is the common case.
```

Wording is indicative, not byte-exact; the reviewed diff is the authority.

### Where it goes, and why that placement is not arbitrary

Inside the skeleton, after the witness paragraph and before the author's own bullets. Verified
against `tools/memory-tree/check-memory-hygiene.sh:1020-1048`: the acceptance-witness arm sets `lab`
only on a line matching its AC-label regex and appends every later line to `acc` until the next
label or the next `## `. Instructional prose sitting ABOVE an author's first bullet is therefore
read with `lab` empty and can satisfy nothing. Prose left BELOW an author's last bullet would fold
its backticks into that bullet's witness blob, which is why the paragraph joins the existing §6
instructions rather than trailing the section. The hazard is pre-existing and unchanged in kind —
the two paragraphs already there carry backticks — and it is recorded because a later editor moving
this text down would silently weaken the witness arm.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | The authored source. Edit here. |
| `memory/TEMPLATE-SPEC.md` | Re-rendered from the twin, never hand-edited. |

Roughly 900 B added to each, against 16,913 B and 16,906 B today. That figure is an ESTIMATE from
the draft text above and not a measurement; the observation in AC4 derives it rather than repeating
it. Verified 2026-09-04 that no size gate binds either file: neither has a row in
`tools/template-size-limits.txt`, and `bash tools/memory-tree/check-memory-hygiene.sh
--print-index-set` does not list `memory/TEMPLATE-SPEC.md`, so check 6's per-class caps do not
reach it.

### Migration

None. No cutoff key is declared, and that is compliance with this build's dated-cutoff rule rather
than an exception to it: a cutoff exists so a new machine-graded demand cannot red landed work, and
this unit adds no machine-graded demand. Declaring one would put a dead key in
`.memory-tree.conf` that nothing reads — which is the defect `TOOL-aJoinedCanon-10` exists to
repair one instance of.

### Alternatives rejected

- **A fifth `##` section for preconditions.** The template forbids additional `##` headings and
  check 12 compares the section list for equality, so this is a new canon and a new dated cutoff for
  a paragraph. Rejected on cost.
- **Four named sub-fields per criterion.** Carried to §8 as an open fork rather than rejected here,
  because it is the owner's shape call and not mine.
- **A `Preconditions:` marker plus an arm that requires one per bullet.** Rejected: a required line
  that has nothing to say gets written as "none" 1,400 times and the gate then measures typing. §7.
- **Putting the derived-or-pinned rule in the Writing rules instead.** Carried to §8 as a fork.

## 5. Production-readiness checklist

- security — N/A. A documentation paragraph in a tracked template; no write path, no input, no
  surface.
- perf / scale — N/A. No code runs. The byte cost is in "Files touched" and no size gate binds it.
- a11y — N/A. No user interface.
- i18n — N/A. Single-language repo documentation.
- error / empty / loading states — N/A. Nothing executes.
- observability — N/A. Nothing emits.
- risks — One, and it is a documentation risk: a later editor moves the paragraph below an author's
  bullets and weakens the acceptance-witness arm. Recorded in §4 where an editor reads it. Rollback
  is a revert of two files, and the twin parity gate refuses a revert of only one.
- testing + left-shift gates — **No gate, deliberately, and this row names the compensating check.**
  "Did the author declare the cost" is not mechanically distinguishable from prose, so no arm is
  written and none is claimed. The compensating check is a re-measurement, not a review pass: after
  five more builds close, re-run finding A5's method — count acceptance criteria amended at build
  time, bin them by cost, permission, fixture and stale literal, and compare against the 23, 6 and 8
  recorded here. If the three classes have not moved, this unit did nothing and should be reverted
  rather than reinforced. That check is manual, deferred, and owned by whoever next audits the spec
  format; it is filed as a backlog row at build time, not asserted here as done.
- migration / rollback — See §4. No cutoff key, no corpus edit, no state to migrate.
- user docs — N/A. `memory/TEMPLATE-SPEC.md` IS the document; there is no separate `help/` page for
  the memory-tree kit's own rule set.

## 6. Acceptance criteria

*This section is written in the shape S1 proposes. A `Preconditions:` line appears only where one
applies, which is the recommendation §8's first fork carries.*

- **AC1** — When the paragraph is added to `tools/memory-tree/SPEC-TEMPLATE.template.md` and the
  live copy is re-rendered, `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0.
  Preconditions: the render direction is TEMPLATE to LIVE, so `--render` must have been run; a
  hand-edited `memory/TEMPLATE-SPEC.md` fails this criterion rather than satisfying it.
- **AC2** — When `grep -ciE 'cost|budget|minutes|hours' memory/TEMPLATE-SPEC.md` is run after the
  change, it returns a count greater than the `0` it returned before.
  Preconditions: the `0` is DERIVED, measured on this branch at base `750ca0ca` on 2026-09-04, not
  inherited from the finding; re-derive it on the pre-change tree if the after-count is disputed.
- **AC3** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the whole tree, it exits
  0, and no spec in `memory/builds/*/spec/` is newly named by check 12.
  Preconditions: the full run is minutes rather than seconds on this node, and it is the whole-tree
  form and not `--staged`, because a staged run grades only the diff and would report a green that
  means nothing here.
- **AC4** — When `wc -c` is taken over both files before and after, the growth is reported as the
  measured pair rather than as §4's estimate.
  Preconditions: the figure is DERIVED at observation time. §4's roughly 900 B is a pinned estimate
  and is not what this criterion grades.
- **AC5** — When this spec is read at close, its own §6 still carries a `Preconditions:` line on the
  criteria that need one, so `git grep -c 'Preconditions:' -- memory/builds/aJoinedCanon/spec/`
  returns a non-zero count for this file.
  Preconditions: no fixture and no permission; this is S3's observation and it is deliberately weak
  — it grades presence, exactly as the witness arm does, and claims nothing about whether the
  declarations are true.

## 7. Gates

Kept green, by name from `tools/gate-legs.json`: `memory hygiene`, `kit/dogfood doc parity`. The
whole bar is `bash tools/run-gates/run-gates.sh`; those two are the legs this diff can actually
move.

**This unit adds no gate, and the reason is the unit's own subject.** The charter binds a new arm to
an observed failing case, and there is no failing case to observe: a criterion that declares its
cost and a criterion that does not are the same bytes to a machine, because the declaration is
prose. An arm that required a `Preconditions:` line on every bullet would grade typing, not
declaration, and would be satisfied by "Preconditions: none" — the could-not-fail shape one level
up, which §7 of the charter names. §5's testing row carries the compensating manual check instead of
an arm, and that is the honest trade rather than a gap left open.

If a later unit finds a sub-shape that a machine can grade — a cost figure that must resolve, a
named fixture path that must exist in `git ls-files` — it is a separate unit with its own dated
cutoff and its own observed red. It is not smuggled in here.

## 8. Open questions

- **F1 · One `Preconditions:` line, or four named sub-fields?** Four sub-fields (`cost:`,
  `permission:`, `fixture:`, `figure:`) read as a checklist and are what a future arm would grade.
  One line is what the corpus already writes when it writes anything: `TOOL-aMouldedFolio-2` carries
  a `Cost` row and an `Entry budget` row in a §5 table, in prose, unprompted. Four fields multiply
  ceremony across a population that is 1,404 AC lines today, and three of the four are empty on most
  criteria. **Recommendation: one line, written only when something applies, with the four names
  listed in the template's PROMPT so the author is asked all four and emits only what is true.** The
  prompt is the checklist; the line is the answer. UNRESOLVED — this is a shape call for the owner.
- **F2 · Does the derived-or-pinned rule belong in §6, or in the Writing rules?** Finding 24's eight
  amendments were all acceptance criteria, which argues §6. But the Writing rules already say
  "Verify every claim about existing code against source at writing time" and a stale figure is that
  rule failing at the seam it does not cover — a spec's §4 pins stale literals too, and a §6-only
  rule leaves those unaddressed. The cost of the Writing-rules placement is that this unit then
  writes to two places in the template, which the fold rule dislikes. **Recommendation: §6 for now,
  because that is where the measured evidence sits, with a one-clause pointer added to the Writing
  rules only if a later measurement finds the class outside §6.** UNRESOLVED.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.

## 10. Reuse audit

No existing seam fits, and the evidence is that the closest candidates are all the wrong kind of
thing. `python tools/codebase-map/reuse_lookup.py "declaring the preconditions an acceptance
observation needs before it can be run"` returned 645 symbols over 20 dossiers and its ranked
candidates are code seams — `extract_declarations`, `read_declared_keys`, `load_declarations`,
`declared_in_kits_json` — every one of them a reader of a machine declaration in a conf or a
registry. There is no seam for a PROSE declaration in a template, because this unit adds no code and
extends no module. The document seam it does extend is the §6 instructional block of
`tools/memory-tree/SPEC-TEMPLATE.template.md`, which already carries two such paragraphs and is the
established home for a rule an author reads while filling the section. The recall probe found the
corpus solving this by hand, one amendment at a time: `TOOL-aMouldedFolio-2` writes an unprompted
`Cost` row in its §5 table, and `TOOL-aNamedGesture-1` AC13's repair — "The witness is now the
command, not a number" — is this unit's derived-or-pinned rule, discovered at amendment cost by a
build that had no section asking for it.

Recall terms used: `acceptance criterion cost budget minutes fixture permission derived figure stale
literal precondition witness`, passed to `python tools/memory-recall/query.py "does any spec section
already declare an acceptance criterion cost, permission or fixture precondition"` for 38 hits.
