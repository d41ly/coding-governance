**Serves:** spec-audit TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-49 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54

# dDerivedDocket — spec audit of topic group G7, the seven units promoted from the G3 bounded exit, round 1

*Node `d`, 2026-09-20. The first Tier-2 adversarial pass over the seven specs promoted out of G3's
bounded exit — the witness capture split (unit 48), the plan's next shape (49), the declared anchor
route (50), an admitted example family (51), the rotated-record ancestry (52), `--at` purity (53) and
the unsimplified exclusion walk (54). All seven specs are NEW and unreviewed, written from the G3
record's blocker and highs at that subject's bounded exit, so every word of them is unreviewed
surface and the pass was aimed at all of it rather than at a delta. This group is regrounded on
`fb07ca25`: origin/main moved 210 commits past the original BASE `abac6d59`, HEAD merges it in, and
every spec re-verified its claims there and moved its header base under a section 9 line reading
`regrounded on fb07ca25`. Code claims below are judged at HEAD. Four primed finder lenses ran and all
four returned; a skeptic stage prompted to REFUTE each finding ran in five batches and all five
returned; then this synthesis. The sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md`
with its roster and edge tables, and the previous review of this group's parent subject,
`memory/builds/dDerivedDocket/reviews/2026-09-20-review-TOOL-dDerivedDocket-15-spec-audit-g3-round2.md`.
Sibling specs outside G7 were read wherever an edge or an interface named them, because contradiction
BETWEEN specs is in scope and this build has already paid for it twice. Every finding below was
re-checked against source at HEAD before it was written down, and the sites read are named in each
entry.*

**Round: 1.** Range at base `fb07ca25`, each subject pinned at the blob it was read at:

- `memory/builds/dDerivedDocket/spec/2026-09-20-spec-TOOL-dDerivedDocket-48.md@3a564af742e5cd647c42ebe232d59ad6d5077dca`
- `memory/builds/dDerivedDocket/spec/2026-09-20-spec-TOOL-dDerivedDocket-49.md@ef36c41b7099dab21491cceba2e60acdfbb858ea`
- `memory/builds/dDerivedDocket/spec/2026-09-20-spec-TOOL-dDerivedDocket-50.md@4e6921b40d31a8fd50575d3487ed7a6cc569575d`
- `memory/builds/dDerivedDocket/spec/2026-09-20-spec-TOOL-dDerivedDocket-51.md@ea3977c7907f80745822d66ac4ee9ee9dcc767f1`
- `memory/builds/dDerivedDocket/spec/2026-09-20-spec-TOOL-dDerivedDocket-52.md@0c3d4ce394a9b750ef850531523df0b48042b47e`
- `memory/builds/dDerivedDocket/spec/2026-09-20-spec-TOOL-dDerivedDocket-53.md@43a5778d6507be3d2a98d6f5049a1f57addabad9`
- `memory/builds/dDerivedDocket/spec/2026-09-20-spec-TOOL-dDerivedDocket-54.md@661bc52b1118163441fa63be54e6054339316e70`

## Verdict: CLEAN WITH FIXES

No blocker stands. Fourteen distinct defects carried by sixteen raw confirmed findings: five HIGH,
five MEDIUM, four LOW. Every one of the fourteen has a fix entirely inside this run's authority —
not one needs an owner turn, a new mechanism, or a design decision the set does not already carry —
which is why the verdict is not BLOCKED despite five highs.

Read H2 first. Spec 48 is the unit that exists to make an unreadable refusal readable, and its S1
and AC1 direct the builder to clear `RB_OUT` on the `mktemp` refusal branch — the branch whose ONLY
diagnostic is the string it would be clearing. Built as written, a capture-file failure refuses with
an empty reason through three callers, which is the exact class the unit was promoted to close,
arriving through the unit that closes it. The value that really is stale on that path, `RB_TOOK`, is
excluded from the clearing by S1's own wording.

The other four highs share one shape and it is worth naming, because it is not the shape this build
has been paying for. H1, H4 and H5 are all a spec describing a world that has MOVED: unit 49 states
a contradiction in unit 16 in the present tense that unit 16's own fold already discharged; unit 54's
AC1 cites a row pair its own §4 contradicts two paragraphs earlier and measures the wrong subject;
unit 52 reinvents a rotation-aware first-commit resolver that unit 22 of this same build already
builds in the same file, with the opposite ruling on `--follow` and no edge in either direction. H3
is the classic instead — a route whose entire purpose is an arbitrary target root raises a foreign
exception as a traceback for exactly that input.

The mediums are the house's dominant class in five new places: four criteria that cannot fail on the
thing their scope item asks for, and one readiness row claiming coverage its spec has no mechanism to
deliver.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is COMPLETE. Every lens reported and every finding reached a skeptic, so a zero count below
is evidence rather than an artefact of a missing lens — including the statement under H5 that no
sibling spec carries a second `read_stderr_tail`, and the statement under M3 that no criterion in
spec 53 asks for a content check. Two pairs of ids describe one defect each from two addresses and
are merged: 1 and 16 into H1, 11 and 13 into L1. The pipeline's duplicate count of 0 comes from its
own exact-match dedupe, which does not see a restatement.

## Review shape

Raw 47, confirmed 16, refuted 31, unverified 0. Precision 0.34, below the ~0.5 floor charter §8
sets, and the reading is the same one the G5 and G6 rounds reached from the other direction: four
lenses over seven specs is not too wide, but a lens primed on code defects spends most of its budget
on a spec corpus. Of the 31 refuted, 19 were code-shaped claims about `tools/unattended/` that the
specs had already ruled out of scope or that HEAD simply does not say. The 31 refuted findings are
not reproduced here.

Adjudicated tally, stated both ways, because merged items and raw ids do not agree:

| Severity | Items | Raw confirmed ids |
|---|---:|---:|
| BLOCKER | 0 | 0 |
| HIGH | 5 | 6 |
| MEDIUM | 5 | 5 |
| LOW | 4 | 5 |
| Total | 14 | 16 |

**Severity is adjudicated here, not copied from the finders.** The scale is the one the G1 to G6
reports used, so the seven groups' counts compare.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  set needs a decision or a mechanism no spec in it carries.
- HIGH means a unit cannot be built or cannot pass as written. It also covers a unit that ships a
  layer which stays inert or broken while its suite reads green.
- MEDIUM covers a contradiction with a bounded consequence, a declaration a spec owes, and a rule
  whose break no criterion can see.
- LOW is the same kinds of defect where the reachable harm is small.

Against the finders' ratings, two calls move. Finding 16 came in MEDIUM and is absorbed into H1,
taking that item's HIGH, because the two findings share one fix and the merged defect is the larger
of the two. Finding 13 came in MEDIUM and is adjudicated LOW at L1: its skeptic established that
AC8's second arm already grades the fourth empty as "distinct in text from the other three", so a
builder shipping three reason lines cannot pass this unit's own criteria — the §5 sentence is false
about its own S4, which is real, but the reachable harm is a misread by a reader pricing the error
surface, not a shipped defect.

## Findings index

| Id | Severity | Entry | Spec | Address |
|---:|---|---|---:|---|
| 26 | HIGH | H2 | 48 | §2 S1; §4 the widened-refusal paragraph; §6 AC1 |
| 29 | HIGH | H3 | 50 | §4 The route; §5 error / empty / loading; §2 S2 |
| 36 | HIGH | H4 | 54 | §4 The measurement table; §6 AC1 |
| 38 | HIGH | H5 | 52 | §3 Edges and the first-commit non-goal; §8 F2; §10 |
| 1 | HIGH | H1 | 49 | §2 S6; §6 (no criterion) |
| 16 | HIGH | H1 | 49 | §1; §2 S3; §4 "Why the rung ... is pinned and not built"; §2 S6 |
| 3 | MEDIUM | M1 | 48 | §6 AC5 |
| 5 | MEDIUM | M2 | 50 | §6 AC5, against §2 S7 |
| 8 | MEDIUM | M3 | 53 | §5 error / empty / loading, against §2 S2 and §6 AC2 |
| 21 | MEDIUM | M4 | 53 | §7 Gates, against §4 Inventory |
| 30 | MEDIUM | M5 | 50 | §2 S2; §6 AC3 |
| 11 | LOW | L1 | 52 | §5 error / empty / loading |
| 13 | LOW | L1 | 52 | §5 error / empty / loading, against §2 S4, §4 step 5, §6 AC8 |
| 22 | LOW | L2 | 48 | §5 perf / scale |
| 23 | LOW | L3 | 48 | §3 Edges (units 15 and 28); §9 rev-1 |
| 47 | LOW | L4 | 49 | §10 Reuse audit, last paragraph |

Spec paths below are abbreviated to their unit number: "spec 48" is
`memory/builds/dDerivedDocket/spec/2026-09-20-spec-TOOL-dDerivedDocket-48.md` and so on through 54,
each read at the blob pinned in the range line above. Sibling specs outside this group are named in
full at first mention.

## Blockers

None. No finder rated a finding BLOCKER, and none is adjudicated one here. Every defect below has at
least one fix route the run can take without an owner turn. H5 is the nearest miss, because one of
its two routes — routing unit 22's dating through unit 52's resolver — is a real design choice across
two units; but its other route, declaring the edge and stating why `--follow` is right for a DATE and
wrong for a SHA, is a spec edit and closes the routing hole on its own.

## High

### H1 — spec 49's S6 hands unit 16 a cross-edit that is already landed, and no criterion of either kind grades it (1, 16)

**Address.** Spec 49 §2 S6; §1; §2 S3; §4 "Why the rung the promoted finding names is pinned and not
built"; §6, where no criterion reads unit 16's spec.

**What is wrong.** Two faults in one passage, and one fix closes both.

First, the obligation is already discharged. Spec 49 states the motivating contradiction in the
present tense in three places — §1 says unit 16 "adds a third shape whose position that prose pins
and whose own fixture contradicts it", and §4 says "The fixture is the half that moves, and its
replacement wording is S6". At HEAD, unit 16's AC18 already carries the folded text:
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md:480-500` asserts
"`next:` reads the MISSING shape naming `-2`" on the first run, and a second arm over the same
fixture with both MISSING units retired asserts the flip to the UNDECIDED shape. That spec's §9
records the fold at `:640-644`: "Extended on the promote close-out pass ... AC18 ... the fold of
`TOOL-dDerivedDocket-49`, which ruled §4's ordering sentence over this criterion's fixture". A
builder or reviewer following spec 49's §4 goes hunting a contradiction in unit 16 that no longer
exists.

Second, the cross-edit is ungraded in a set whose siblings grade exactly this class. S6 closes "NOT
OBSERVED by a criterion of this unit", and the stated reason covers only the runtime FLIP — "the flip
needs the ask rung's predicate, which unit 16 builds" — never the fact that the textual edit was
made. No criterion in §6 reads unit 16's spec at all: AC1 to AC6 are driver, source and output, AC7
is a byte-size comparison of the dossier and the two protocol copies, AC8 is the arms floor. §4's
Files-touched says the criterion text "is not written from here". So nothing in this unit's commit or
its criteria makes the correction land, and nothing detects it being un-landed.

The sibling contrast is exact and local to this spec. Unit 51's AC5 (spec 51:250) reads "When unit
15's spec is read at this unit's commit, its AC13 carries a `new arm:` clause ... and that spec's §9
carries a new rev entry", and unit 50's AC7 (spec 50:385) reads "When unit 15's spec is read at this
unit's commit, `RECALL_CLI` occurs zero times in it outside its §9 revision log". Both were written
in the same promotion pass as spec 49, both grade a textual cross-edit at their own commit, and spec
49 is the one that does not.

**Why it bites, concretely.** The two faults compound rather than cancel. Because the edit has
landed, the run's real remaining obligation is not to make it — it is to keep unit 16's AC18 and this
unit's rung table in step, so a later fold of unit 16 cannot silently re-open the rung order this
unit was promoted to pin. That obligation is stated nowhere in either spec. Meanwhile S6 as written
asks the build pass to spend a cross-edit on text that is already there, and if it declines to (which
is correct, the text is there) nothing reds.

**Fix.** One edit closes both halves.

- Restate §1, S3 and §4 in the past tense against HEAD: unit 16's AC18 already carries the two-arm
  replacement wording, folded on the promote close-out pass, and cite
  `2026-09-14-spec-TOOL-dDerivedDocket-16.md:480-500` with its §9 entry at `:640-644`.
- Replace S6's cross-edit with a criterion in unit 51's AC5 shape: when unit 16's spec is read at
  this unit's commit, AC18's first run asserts the MISSING shape naming `-2`, a second arm over the
  same fixture with both MISSING units retired asserts the flip to UNDECIDED, and that spec's §9
  carries the rev entry naming AC18. Red when: unit 16's AC18 names one shape only, so the rung order
  this unit declares has no failing case in the spec that consumes it.
- Keep S6's existing sentence about the runtime flip being unit 16's own second arm at its own pass.
  That part is right and stays right.

**Left-shift.** This is the third cross-edit-without-an-observer in this build and the class is worth
a mechanical check rather than a reviewer's eye. The candidate predicate: every §2 scope item whose
text contains a sibling unit id AND a verb of modification must be answered by a §6 criterion whose
text contains the same unit id. Both populations are already parsed by
`tools/check-spec-tokens.py`, so it mints no new reader. Its header would have to state what it does
not check: that the criterion grades the RIGHT text, only that one exists naming the same unit.

**This predicate was NOT run over the tree, and charter §7 forbids wiring it until it has been.** The
population it would scan is 46 spec files under `memory/builds/dDerivedDocket/spec/`, holding 606 §6
criteria; this review confirmed by hand that specs 50 and 51 carry a cross-edit criterion and spec 49
does not, which is three data points, not a measurement. Whoever promotes this must run the candidate
and print hits AND near-misses first, because the near-misses are where a scope item that merely
MENTIONS a sibling would red innocently. Treat the gate as unpriced until that run exists.

### H2 — spec 48's refusal branch clears the one value that carries the diagnostic, and keeps the one that is actually stale (26)

**Address.** Spec 48 §2 S1; §4 "The capture after", the widened-refusal paragraph at `:144-145`; §6
AC1 at `:251-255`.

**What is wrong.** The spec's premise about the `mktemp` refusal branch is false at HEAD, and the
instruction built on it deletes a message three callers print.

HEAD's `run_bounded` is `tools/unattended/unattended.sh:183-200`. Its refusal branch is one line:

```
_f=$(mktemp) || { RB_OUT="run_bounded: cannot create a capture file"; return 1; }
```

That branch SETS `RB_OUT` to its only diagnostic and returns at `:185`, before `RB_TOOK` is assigned
at `:195`. So `RB_OUT` is not stale on that path — it is the freshest and only thing the caller gets.
`RB_TOOK` is the value that genuinely carries over from the previous call.

Spec 48 §4 asserts the opposite: "Today a failed `mktemp` leaves the other values holding whatever
the previous call left in them, which is the stale-value class; all three are cleared on that path."
AC1 makes it a graded requirement: "When `mktemp` is made to fail on the same stub, all three values
are cleared and the function returns 1." The three, per S1, are `RB_STDOUT`, `RB_ERR` and `RB_OUT`,
with `RB_TOOK` excluded by S1's own wording.

**Why it bites, concretely.** An arm written to AC1 asserts `RB_OUT` is empty after a failed
`mktemp`. Ship that and the capture-file failure refuses with no reason at all through every caller
that prints it: `check_wiring` indents `$wout` under its refusal (`unattended.sh:1208` and `:1214`),
`gates-green` carries it in `DOD_OUT` (`:3285`), and `--dispatch` falls back to `head -1` of it
(`:4974`). An unreadable refusal on a failed capture is precisely the class spec 48 exists to close —
its §1 names "a healthy producer reads as a DEAD PROBE" as the defect — so the unit would ship its
own defect on the one path it touches deliberately. Meanwhile `--dispatch`'s refusal at `:4975` goes
on printing a `${RB_TOOK}s` inherited from the previous call, because S1 excluded the one value that
needed clearing.

The finding as filed slightly overstates the blast radius — only `:4975` prints `RB_TOOK` on that
path — and the report keeps the narrower claim.

**Fix.** Rewrite the §4 paragraph and AC1 so the refusal branch:

- sets `RB_STDOUT` and `RB_ERR` empty, which is correct and is what the split newly requires;
- KEEPS `RB_OUT` carrying the existing `run_bounded: cannot create a capture file` sentence
  byte-for-byte, and says in §4 why: it is the branch's only diagnostic and three callers print it;
- adds `RB_TOOK=0` on that path, which S1 must now name.

AC1 then asserts that the message survives the refusal and that the elapsed figure does not carry
over from the previous call. Red when: the refusal branch empties `RB_OUT`, so a failed capture
refuses with no reason; or leaves `RB_TOOK` holding the previous call's figure, so a refusal reports
an elapsed time it never measured.

**Left-shift.** The class is "a spec asserts the current behaviour of a branch it is about to
rewrite, and the assertion is wrong". It does not gate as a predicate over specs, but it gates
cheaply one level down, in the suite: add an arm to `tools/unattended/unattended.test.sh` asserting
that after a forced `mktemp` failure `RB_OUT` is NON-empty and matches the diagnostic. That arm reds
today only if someone empties it, which makes it the regression gate for this exact defect and costs
one `arm` call. The review half — that a spec's "today the code does X" sentence was read at HEAD
rather than remembered — belongs beside
`memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md` as its sibling form: a spec
premise asserting current behaviour, verified by nobody.

### H3 — spec 50's one public route raises a foreign exception as a traceback for exactly the input it was built to accept (29)

**Address.** Spec 50 §4 "The route"; §5 error / empty / loading states at `:306-308`; §2 S2.

**What is wrong.** The route's three named states assume `grammar(root)` fails only when the sibling
kit is absent. It has a second failure mode that fires on the unit's own headline input.

`grammar()` returns `extract.grammar_for(root)` (`tools/memory-tree/corpus_ids.py:284`). With a
non-None root, `grammar_for` calls `recall_conf.resolve(pathlib.Path(root))`
(`tools/memory-recall/extract.py:492`), and that raises `ConfError` when the TARGET root carries no
`.memory-tree.conf`, declares no `MEMORY_ROOT`, or declares no usable `FAMILIES`
(`tools/memory-recall/recall_conf.py:246-264`, with `CONF_NAME = ".memory-tree.conf"` at `:41`).

`ConfError` subclasses `RuntimeError` (`recall_conf.py:46`), not `corpus_ids.Problem`. Measured at
HEAD: the string `ConfError` occurs zero times in `tools/memory-tree/corpus_ids.py`, so none of that
module's three `except Problem` handlers (`:699`, `:835`, `:1253`) catches it.

**Why it bites, concretely.** `resolve_anchor` is this unit's ONE public root-to-anchor route and its
whole point is accepting an arbitrary target root. A scratch root with no `.memory-tree.conf` is not
an exotic input — it is the first call a fixture-root caller makes, including unit 51's, and unit 51
is in this same group at order 14, one order after this unit. The result is a raw traceback out of a
module whose own docstring forbids a foreign exception past `main`'s `except Problem` (the note at
`corpus_ids.py:239`), and a gate reading that traceback learns neither which root nor which
declaration was missing. §5 enumerates three states and none of them is this one, for a route whose
entire purpose is the input that produces it.

**Fix.** Add a scope item mapping `recall_conf.ConfError` onto the kit's own `Problem` inside
`resolve_anchor`, with a message naming the root and the missing declaration — the three cases
`recall_conf.resolve` distinguishes are already distinct, so the mapping can name which. Add a
criterion over a scratch root holding no `.memory-tree.conf`, asserting the named refusal rather than
an unexpected exception. Then extend §5's error row from three states to four, and correct §4's
pricing of `grammar(root)`: it raises when the sibling kit is absent OR when the TARGET root is not a
declared memory tree.

**Left-shift.** The class is "a module's public entry point lets a foreign exception type escape past
its own `except`". It gates as a test, not as a scan: add an arm to the corpus-ids self-test that
calls every public entry point of `corpus_ids.py` over a scratch root with no `.memory-tree.conf` and
asserts the process exits with the module's own named refusal rather than a traceback. State in its
header what it does not check: that the refusal's TEXT is useful, only that the type is the kit's
own.

**Not run.** `resolve_anchor` does not exist yet, so the arm lands with this unit; whether the same
arm passes over today's existing entry points is UNMEASURED, and it should be run before the unit is
built, because a second escape on an existing path would change this unit's scope. What IS measured
is the escape itself: `ConfError` occurs zero times in `corpus_ids.py`, and its three `except Problem`
handlers are at `:699`, `:835` and `:1253`.

### H4 — spec 54's arm cites a row pair its own §4 contradicts, and measures a subject the caller never passes (36)

**Address.** Spec 54 §4 "The measurement" table, rows 1 to 4, and the paragraph at `:103`; §6 AC1 at
`:248-252`; §4 `:158`.

**What is wrong.** Three statements in one spec about which rows the arm asserts, and they do not
agree; underneath the disagreement is a subject mismatch that leaves the unit's premise unproven.

The caller's subject is a PARENT. §3's Edges bullet quotes unit 19's spelling as
`git rev-list -1 <parent> ^<BASE> -- <run-state path>`, and §4 at `:158` says "The caller asks it once
per parent of a merge". AC1 is written with that subject: it "answers YES for the parent from which
the run's touching commit is reachable, and the arm asserts the simplified spelling answers nothing
for that same parent". But AC1 then cites "rows 1 and 2 of §4's measurement table", and rows 1 and 2
measure THE MERGE as the subject. §4's own row 3 measures the parent subject and reports the
opposite: "simplified, from the run-branch parent | the run commit" — the simplified spelling ANSWERS
for that subject. And §4 at `:103` names a third row-set for the same arm: "Rows 2 and 4 together are
the pair the arm asserts".

**Why it bites, concretely.** Built against the fixture §4 describes, AC1's control assertion is
false by the spec's own measurement: the simplified-versus-unsimplified contrast exists only when the
merge itself is the subject, and the arm fails on its control. Worse, the defect shape the caller
actually meets is never measured at all. The caller hands over a PARENT; the case that hurts is a
parent that is ITSELF a merge, TREESAME to one of its own parents for the run-state path, because
that is when simplification prunes the side the run commit is on. No row in the table measures that
commit, so the unit's premise — that the unsimplified walk is needed for the caller's real question —
is unproven for the only call shape the predicate serves. A unit whose measurement section does not
measure its own motivating case is a unit that can land with its arm green and its reason unestablished.

**Fix.** Three edits, in order.

- State in §4 that the subject is any commit the caller hands over, INCLUDING a parent that is itself
  a merge, and say why that is the hard case.
- Extend the fixture so the GRADED PARENT is a nested merge TREESAME to one of its parents for the
  run-state path, and re-measure both spellings at that subject, adding the rows. The existing rows
  stay as the simpler illustration.
- Make AC1 cite the same row pair §4 names, once §4 names one pair rather than two, and assert the
  contrast at the nested-merge parent rather than at the merge.

**Left-shift.** The tempting mechanical half is a same-spec join: every "rows N and M" style citation
in a §6 criterion must name rows that exist in a §4 table of the same spec, and the spec must not
name two different row-sets for one criterion. **It was not priced over the tree, and it should not
be wired on this report's say-so** — row-citation prose is varied enough that the false-positive rate
is the whole question and nobody has measured it. The honest left-shift is documented instead: add to
the gotchas tree the class "a criterion cites a measurement whose SUBJECT differs from the caller's",
with this spec as its worked instance, and run it at spec-audit time by reading each criterion's
cited evidence back against the caller's argument list. That is what found this one. The specific
defect is closed by the fix above, not by a gate.

### H5 — two rotation-aware first-commit resolvers land in one build, in one file, with opposite rulings and no edge either way (38)

**Address.** Spec 52 §3 Edges and the non-goal "Retrofitting the leg's two existing first-commit
reads"; §8 F2; §10 Reuse audit at `:458-459`.

**What is wrong.** Spec 52 builds a resolver for a record's introducing commit across the rotation
rename, and never names `TOOL-dDerivedDocket-22`, which in this same build already does the same
work in the same file with the opposite tool ruling.

Measured at HEAD. Unit 22 resolves a record's first commit with `git log --follow --diff-filter=A` in
four places (`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-22.md:79`, `:84`,
`:302`, `:440`), and its §4 "The fact-set arm" states the tenancy floor in the same words spec 52
presents as its own new mechanism: the date is FLOORED at the newest ADD of an archived sibling in
the same directory, which is where that record's tenancy of the path begins. Spec 52's F2 REJECTS
`--follow` as a heuristic. Both units write `tools/unattended/check-unattended.sh`, unit 52 at order
17 and unit 22 at order 22.

The coupling is recorded on exactly one side. `grep` over spec 52 returns zero hits for
`dDerivedDocket-22`. Unit 22's §9 names "`TOOL-dDerivedDocket-52`'s close-out" twice, at `:759-760`,
recording the cross-edit spec 52's own close-out pushed into it.

**Why it bites, concretely.** A change to either resolver is routed to neither. The kit gets two
functions answering one question with different tools, and the tenancy floor is implemented twice.
Spec 52's §3 non-goal names "the leg's two existing first-commit reads" by line at the base, and that
count is already stale — unit 22 adds two more in the same file, and unit 22's §7 flags
`check-unattended.sh:1313` as a live hit at check 15's `LANDED_ANCHOR_CUTOFF` site. A builder reading
§3 believes there are two and leaves two more unconverted.

The cause is visible in spec 52's own §10, and it is the interesting part. The reuse audit concludes
"no seam" solely from `python tools/codebase-map/reuse_lookup.py` reporting `.sh` unscanned
(`:83`, `:458-459`). It never looked at its own build's sibling specs. A reuse audit that consults
only a tool which cannot see the language in question, and treats that blindness as a negative
result, is a probe with no liveness assertion — charter §7's exact rule, applied to a spec section
rather than to a gate.

**Fix.** Three edits, and a fourth if the routing choice goes the other way.

- Add an Edges bullet to spec 52 naming `TOOL-dDerivedDocket-22` as hands-off, since 22 is at a later
  order, describing what that unit's dating reads and why this resolver does not change it.
- Restate §3's non-goal to name unit 22's two new `--follow --diff-filter=A` reads as the third and
  fourth first-commit reads in the same file, so the count is not stale on landing day.
- Add one sentence to F2 stating why `--follow` stays right for a DATE and wrong for a SHA — a
  heuristic that picks the wrong commit still yields the right day in the rotation case, which is the
  whole reason the two units can legitimately differ. Without that sentence the two specs simply
  contradict each other.
- OR, if the run prefers one mechanism: route unit 22's dating through this resolver and say so in
  both specs. That is the larger change and it is a real choice, which is why the first three edits
  are the recommended route.

**Left-shift.** The mechanical gate is the one spec 52's §10 should have been, and it is charter §7's
liveness rule applied to a probe that currently reports a reassuring nothing: a reuse audit that
reports `.sh` unscanned must say so as a LIMIT rather than as a result. Add to
`tools/codebase-map/reuse_lookup.py` a non-zero exit or an explicit `UNSCANNED: <ext>` banner
whenever the query's subject files are in a language the map does not scan, so a spec author cannot
quote "no seam" from a probe that could not look.

**Not run.** `reuse_lookup.py` was not executed for this report; that the tool states its `.sh`
limitation is taken from spec 52's own §10 quoting it (`:83`, `:458-459`), which is the spec's word
and not a measurement. Run the tool and read its current output before changing its exit behaviour,
since a non-zero exit would reach every existing caller. The second half needs no tool at all: at
spec-audit time, grep the build's own spec folder for the mechanism's distinguishing command before
accepting a "no seam" conclusion. That is what found this defect — `grep -c dDerivedDocket-22` over
spec 52 returns 0, and unit 22's §9 names spec 52 twice — and it belongs in the gotchas tree as "a
reuse audit that consulted only a tool blind to the language".

## Medium

### M1 — spec 48's AC5 grades a verdict no subject in this unit emits (3)

**Address.** Spec 48 §6 AC5 at `:295-300`, against §2 S5, §3 and §4 Rollout.

**What is wrong.** AC5 grades what "the caller" reports for three stdout-empty verdicts — that the
producer wrote only to stderr, a DEAD PROBE, and that the command never answered — and names no
caller, no file, no line and no fixture. Every caller this spec names reads `RB_OUT`, not the split.

The subject does not exist at this unit's order. §3 assigns the parse and its refusals to unit 16
("The `ASKS_CMD` key, its call shapes, the pinned mandate and the parse are unit 16's"), S3 repeats
it, and §4's Rollout says the change is dark for the witness because `ASKS_CMD` is blank until unit
35. The §4 Inventory names only `RB_STDOUT`, `RB_ERR` and `read_stderr_tail`, and `read_stderr_tail`
returns a bounded tail — it decides nothing. Measured at HEAD: `ASKS_CMD` occurs nowhere in `tools/`,
`read_stderr_tail` appears in no other spec in the folder, and the driver emits no DEAD PROBE verdict
from any bounded call (only the never-answered wording at `unattended.sh:3286-3291`).

**Why it matters.** S5 is the liveness split, which §1 names as this unit's point, and it is the one
scope item in the spec with no gradeable subject in its own pass. AC5 therefore cannot fail — the
could-not-fail shape, in the criterion covering the unit's headline deliverable. Every other
criterion in this spec names its actor and often its file and line; AC1 even names the extraction
idiom at `tools/unattended/unattended.test.sh:5348`. AC5 names "the caller".

It is MEDIUM and not HIGH because the layer itself is not broken: §4's Rollout already declares the
change dark for the witness, so nothing ships inert that was meant to be live. What ships is a scope
item with no observer.

**Fix.** Name AC5's subject, by one of two routes.

- Add a helper beside `read_stderr_tail` that maps the three stdout-empty states to their three
  distinct verdict strings, and have the arm call it directly over a stub — the shape AC1 already
  uses for `run_bounded`. AC5 then grades the three strings and their distinctness at this unit's
  commit.
- Or move S5's verdict wording to a declared cross-edit on unit 16, with a criterion here that reads
  that spec's text at this unit's commit, the way unit 50's AC7 does. If this route is taken, see H1:
  the cross-edit needs its own observer.

**Left-shift.** The gate is the one H1 proposes from the other side, and this finding is why it
should also grade criteria: every §6 criterion must name at least one file path, command or sibling
unit id in its "When" clause. Its header must state what it does not check: that the named subject
EXISTS at the unit's order, which is the half that caught this one and stays a review check.

**This predicate was NOT run either.** The population is 606 §6 criteria across the 46 specs, counted
for this report; how many of them would red is unmeasured, and the number matters, because a criterion
legitimately phrased around a behaviour rather than a file would red innocently. Run it and print
near-misses before wiring it.

### M2 — spec 50's AC5 grades a comparison that is true by construction, on the one thing S7 asks for (5)

**Address.** Spec 50 §6 AC5 at `:368-373`, against §2 S7 at `:72` and §4 step 6 at `:265`.

**What is wrong.** S7 requires `FLOOR_ASSERTIONS` in the memory-hygiene self-test to be RAISED "to
the count the suite's PASS line prints at that commit". AC5's observation is that the PASS line
"prints an assertion count at or above `FLOOR_ASSERTIONS` as that constant reads in the same commit".

This unit adds arms, so the printed count strictly rises. The `>=` therefore holds whether the
constant moves or not. The criterion cannot fail on the raise S7 asks for, and AC5's own Red-when is
about a stale exemption, not about the floor at all.

**Why it matters.** The floor exists so a later deletion of these arms reds something. Left at its
old value it catches nothing this unit adds, and the criterion that was supposed to notice reads
green. This is the same class as M1 — a criterion that cannot fail — reached by arithmetic rather
than by a missing subject.

The sibling contrast is exact, and both siblings were written in this same promotion pass. Unit 52's
AC5 (spec 52:357-361) and unit 54's AC5 (spec 54:289-293) both read: the floor "reads a higher armed
count at this unit's commit than at its parent, read with `git show` at both", with Red-when "arms
land and the floor holds, so a later deletion of them is invisible".

**Fix.** Restate AC5's floor half in the sibling shape: `FLOOR_ASSERTIONS` in
`tools/memory-tree/check-memory-hygiene.test.sh` reads a higher number at this unit's commit than at
its parent, read with `git show` at both, and equals the count the suite's PASS line prints at this
unit's commit. Keep the derived-figure note — the count is re-read, never predicted — and keep AC5's
existing exemption-list assertions and their Red-when unchanged.

**Left-shift.** The mechanical form is a spec-side lint over §6: a criterion grading an assertion
floor must compare with EQUALITY at the unit's commit, or with a strict increase against the parent,
and never with `>=` against the floor as it reads in the same commit. The population is small and
the three instances are in this group — specs 50, 52 and 54 — with 52 and 54 already correct, so the
lint has one red and two controls, which is the minimum shape a gate needs.

**Not run beyond those three.** Whether other specs in the build grade a floor this way is
unmeasured. The stronger and cheaper alternative, which also was not measured, is to move the
assertion out of the specs entirely: have the suite refuse a floor strictly below its own printed
count at a commit that moves the suite. Before wiring that, read every `ARMS_FLOORS` row in
`.memory-tree.conf` against its suite's printed count at HEAD — a floor deliberately left trailing
would red, and this report does not know whether one exists. State in the header what it does not
check: it cannot tell a deliberately trailing floor from a forgotten one.

### M3 — spec 53's readiness row promises three refusals where S2 declares one, and one of the three has no mechanism (8)

**Address.** Spec 53 §5 error / empty / loading states at `:192-193`, against §2 S2 at `:37-38` and
§6 AC2; §8 F2.

**What is wrong.** §5 reads: "S2's named refusal is the whole of this row: absent blob, absent rev
and unparseable bytes each name themselves rather than degrading to the working tree." S2 declares
one refusal — "A rev whose tree carries no `.memory-tree.conf` blob is a NAMED refusal that prints
the rev and the path" — AC2 observes that one, and §8 F2 ruled on that one.

The third of the three is not merely unbuilt, it is unbuildable through the mechanism S1 mandates. S1
requires the read go through `parse_conf`, the kit's one conf parser, and through no second grammar.
`parse_conf` (`tools/memory-tree/corpus_ids.py:170`) cannot fail: it walks lines, keeps whatever
`parse_conf_line` yields, and silently ignores the rest. So "unparseable bytes name themselves"
cannot happen. A garbage blob parses to a near-empty dict, the caller grades on defaults, and the
answer still reads as pinned — the exact defect S2 exists to close, arriving through the input §5
claims is covered.

**Why it matters.** This is a readiness row asserting coverage the spec has no mechanism to deliver,
which is a claim with no mechanism rather than a missing nicety. An unresolvable rev surfaces as
whatever `git` raises through the caller; unparseable bytes parse to a partial conf. Both grade with
declarations nobody read while the answer still reads as pinned.

**Fix.** Pick one and say which.

- Widen S2 to all three inputs — a rev that does not resolve, a rev whose tree carries no
  `.memory-tree.conf` blob, and bytes `parse_conf` cannot read are each a NAMED refusal printing the
  rev and the path — and widen AC2 to a fixture per input. This route needs a content check that S1's
  "no second grammar" rule must be amended to permit: a sanity assertion that the blob yielded at
  least one declaration is enough, and is not a second grammar.
- Or narrow §5's row to the one state S2 actually declares, and say the other two are out of scope
  with their reason. If this route is taken, the reason for the unparseable case must be the real one
  — `parse_conf` cannot fail by design — not silence.

**Left-shift.** The class is "a §5 readiness row claims a state no scope item declares". The
mechanical form would be a same-spec join: every state enumerated in a §5 error/empty row must appear
in a §2 scope item or a §6 criterion of the same spec, matched on the row's own nouns. **It was not
priced, and the prose shape of §5 rows makes the false-positive rate the entire question** — this
build already recorded exactly that verdict for the S-item citation proxy, which is reason to expect
noise, not evidence of it.

So it stays a REVIEW check until someone measures it: at spec-audit time, read each §5 row's
enumerated states back against §2 and §6 and count them. That check finds this defect and L1 below in
one pass, by hand, which is how both were found here.

**The other half of M3 does not gate at all and should not be made to.** That `parse_conf` cannot
fail is a property of the parser, not of the spec, and the only durable record of it is a sentence in
the spec or the parser's own docstring saying so. `tools/memory-tree/corpus_ids.py:170` currently
says what `parse_conf` does and not what it will never do; adding that one clause is the cheapest
real left-shift here, and it is charter §7's gate-header rule applied to a parser.

### M4 — spec 53's declared bar omits the one leg that grades the verdict its §4 defers to (21)

**Address.** Spec 53 §7 Gates at `:242`, against §4 Inventory.

**What is wrong.** §4's Inventory adds one new python function, takes its name from
`lexicon.py --suggest`, and says "the row that grades it is the python cell". §7 then lists
`build-index selftest`, `memory hygiene`, `codebase-map coverage + freshness` and
`spec tokens (a spec's own names resolve)`. `lexicon naming predicates` is absent.

Measured at HEAD: `.lexicon.conf` declares `py:python-ast:parser` and a live `py.function snake` cell
(`.lexicon.conf:418`), and the `lexicon naming predicates` leg (`tools/gate-legs.json:1052`) is
guarded on `tools/`, so it DOES run on a commit touching
`tools/memory-tree/gen_build_index.py`. Every sibling making the same kind of change lists it: unit
51, same file and one order away, at spec 51:281; unit 50 at spec 50:404; units 48 and 49 at their
own §7. Spec 53 is the one that does not.

**Why it matters.** The leg runs regardless, because it is guarded on the path and not on the spec's
declaration, so nothing breaks at the bar. What breaks is the declaration: §4 defers a naming verdict
to a leg the unit does not claim, and §4's Inventory does not name the chosen identifier either, so
neither that leg nor `spec tokens` has a concrete name to grade before the build pass invents one.

**Fix.** Add `lexicon naming predicates` to §7, and name the chosen identifier in §4's Inventory —
the `--suggest` answer, recorded, the way unit 37's fold recorded its own. Then both legs have a name
to grade and §7 describes the bar the unit actually meets.

**Left-shift.** This one is the best gate candidate in the report, because both sides are
machine-readable. Add to `tools/check-spec-tokens.py` a join: a spec whose §4 or §2 names a new
function, method or CLI subcommand in a language `.lexicon.conf` declares a non-dark coverage mode
for must list `lexicon naming predicates` in its §7. Its header must state what it does not check:
that the identifier named actually passes the cell, which is the leg's own job, and that a spec
adding an identifier in a `dark` language is exempt by construction.

**Partly measured, and the measurement is not the gate's.** Of the 46 specs in this build's folder,
19 list `lexicon naming predicates` in §7 and 27 do not — counted for this report. That is NOT the
predicate's red count, because most of those 27 add no identifier at all and are correctly silent.
The predicate itself was not run, and the honest expectation is that it reds more than spec 53: the
identifier-detecting half is the hard half and will need its near-misses printed before anyone wires
it.

### M5 — spec 50's hoist claims one raise site where the function has two, and its criterion cannot reach the second (30)

**Address.** Spec 50 §2 S2; §6 AC3.

**What is wrong.** S2 says the installed-check hoists into one helper "holding the ONE raise site".
`grammar()` has two. The absent-`extract.py` raise is at `tools/memory-tree/corpus_ids.py:271-276`;
the outdated-kit raise is at `:281-283` and its message still reads "the installed memory-recall kit
predates `grammar_for(root)`; update it, or blank the pins to turn checks 13-15 off".

S2's stated purpose is "the refusal, named, reachable, and TRUE for the caller that receives it". The
pin cure is a no-op for a `resolve_anchor` caller — blanking `DEAD_PATH_PIN` or `ORPHAN_ID_PIN` turns
off checks 13-15 and does nothing for the anchor route. So a caller hitting an installed-but-old
memory-recall kit still receives a cure that does not apply, which is precisely the defect S2
declares it is closing, surviving on the second of the two paths.

AC3 certifies the half that was rewritten. Its fixture points `GRAMMAR_DIR` at a directory that does
not exist, which can only reach the first raise, so the criterion never reaches the message that
still carries the wrong cure. No non-goal covers this: §3's "other verbs' inherited cause" bullet is
about the CAUSE for `--report` and `--measure`, not about the outdated-kit message's cure.

**Fix.** Name both raise sites in S2. Route the version refusal through the same cause-and-cure
helper, so the cure is chosen by the caller rather than fixed in the message. Extend AC3 with a
second fixture whose `GRAMMAR_DIR` holds an `extract.py` WITHOUT `grammar_for`, asserting that the
new caller's message names neither pin, and that the `--report` and `--measure` callers still receive
theirs.

**Left-shift.** The mechanical form is an arm, not a scan: add an arm to the corpus-ids self-test
that drives `resolve_anchor` into each of `grammar()`'s two failure paths and asserts the pin names
are absent from the refusal the new caller receives. Its header states what it does not check: that
the cure the message DOES name is the right one, which only the caller's author knows.

**One correction to the tempting grep form, measured.** A repo-wide ban on the pin names near
`resolve_anchor` would be wrong: `DEAD_PATH_PIN` and `ORPHAN_ID_PIN` occur 22 times in
`tools/memory-tree/corpus_ids.py` at HEAD, and only ONE of those (`:275`) is inside a `grammar()`
refusal message. The rest are conf defaults, pin reads and self-test fixtures, all legitimate. So the
assertion has to be scoped to the refusal text a call actually emits, which is why it is an arm over
the failure path rather than a grep over the file. The arm itself was not written or run for this
report.

## Low

### L1 — spec 52's readiness row counts three named empties where its own S4 declares four (11, 13)

**Address.** Spec 52 §5 error / empty / loading states at `:304-305`, against §2 S4 at `:42`, §4 step
5, and §6 AC8 at `:388-393`.

**What is wrong.** §5 reads "the three named empties of S4 are the whole of this row" and lists an
unknown answer, an absent one and an unresolvable range. S4 states verbatim "Four reasons are
distinguished by name", §4 step 5 enumerates four, and AC8's second arm grades the fourth. The
missing one is the unresolvable tenancy floor, which the same-day close-out added — the rev-1 log
records the floor arriving late, which is why §5 was never restated.

**Why the harm is small, and why it is still a finding.** A builder implementing from §5 alone would
ship three reason lines, but cannot pass this unit's own criteria while doing so: AC8's second arm
asserts the floor empty is "distinct in text from the other three", so the defect is caught one
section later. The finding as filed claimed AC8 would have nothing to assert and that AC6's
two-string comparison was undercounted; neither holds — AC6's two strings are truncation versus
no-candidate by design. What remains is real: the §5 sentence is false about its own S4, in a spec
whose charter bans exactly this shape of authored count, sitting in the one row whose job is to
enumerate the failure states completely.

**Fix.** Rewrite the row as four — an unknown answer at the cap, an absent one after a completed
walk, an unresolvable range, and an unresolvable tenancy floor, each printing its own reason — or
state the count by pointing at S4 rather than restating it. The second option is the one the charter
prefers and is one word shorter.

**Left-shift.** This is the authored-count-beside-its-source class, and it takes the same review
check M3 proposes: at spec-audit time, read each §5 row's enumerated states back against §2 and §6
and count them. The narrow mechanical sliver worth considering is a spelled-cardinal join — a spec
may not write "three" in a §5 row when the scope item it names writes "four" — **and it was not run
over the tree**, so its hit count and its false-positive surface are both unknown. Given that the
charter already bans authored counts in prose and this is a single known instance, the recommendation
is the gotchas tree rather than the bar, recorded beside the existing no-authored-counts note, unless
someone runs the join and finds a population worth gating.

### L2 — spec 48's perf row is wrong on both of its figures and omits the teardown change (22)

**Address.** Spec 48 §5 perf / scale at `:234`, against §4 and `tools/unattended/unattended.sh:185`
and `:196`.

**What is wrong.** §5 prices the change at "one extra `mktemp -d` and one extra `cat` per bounded
call". Both figures are wrong against §4's own design.

Measured at HEAD: `run_bounded` makes exactly one `mktemp` (`:185`) and one `cat` (`:196`). §4
mandates two capture paths under ONE scratch directory and forbids joining the values, which requires
three reads — `RB_STDOUT`, `RB_ERR`, and one substitution over both files. So the `mktemp` is
SWAPPED, not added (zero extra), and reads go from one to three (two extra).

The spec also never states the cleanup change. Today's branch ends `rm -f "$_f"`; a directory needs a
recursive removal. `grep` finds no `rm` anywhere in spec 48.

**Fix.** Restate §5's perf row against §4's design — one `mktemp -d` in place of one `mktemp`, three
reads in place of one — and add the directory teardown to S1, so the swap from a file to a directory
is spelled in the same scope item that owns the refusal branch. That also puts the teardown beside
H2's fix, which touches the same branch.

**Left-shift.** No gate. A numeric claim in a §5 row about a change the same spec designs is exactly
the class charter §7 addresses with "NO count of a derived population is written in prose", but these
are costs rather than populations and there is nothing to derive them from before the code exists.
The documented check is the one that found it: at spec-audit time, re-derive every §5 numeric claim
from §4 and from the cited lines at HEAD. Record it beside the authored-count note.

### L3 — spec 48's Edges block reports a reciprocity obligation both siblings have already met (23)

**Address.** Spec 48 §3 Edges, the `TOOL-dDerivedDocket-15` bullet at `:82-85` and the
`TOOL-dDerivedDocket-28` bullet at `:96-99`; §9 rev-1 at `:363`.

**What is wrong.** Both bullets close "That unit's spec owes the matching line", and §9 repeats it:
"four siblings that route the same call, of which units 15 and 28 owe a matching bullet". Both
reciprocals exist at HEAD. `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md:106`
declares `hands-off TOOL-dDerivedDocket-48`, and
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-28.md:97` declares
`consumes-from TOOL-dDerivedDocket-48`.

**Why the harm is small.** Nothing breaks: check 12's edge arm would grade both satisfied. The cost
is a build pass spending a cross-edit on text that is there, and a reviewer reading a reciprocity gap
that does not exist. It is the same "describes the moment the draft was written, not HEAD" shape as
H1, one severity down because no criterion hangs on it.

**Fix.** Strike "owes the matching line" from both bullets and from the §9 entry, replacing it with
the line each sibling already carries, so the Edges block describes HEAD.

**Left-shift.** This one gates, the gate half exists already, and it is the ONE predicate in this
report that was actually run over the tree. Check 12's edge arm reads both sides of a declared edge;
extend it to refuse an owes-the-matching-line clause in an edge bullet whose reciprocal is already
present in the named sibling. Its header states what it does not check: that the reciprocal bullet
says the RIGHT thing, only that it exists.

**Measured over the 46 specs at HEAD, hits and near-misses both.** Five owes-the-line clauses exist,
across four specs: `2026-09-14-spec-TOOL-dDerivedDocket-19.md:448`,
`2026-09-14-spec-TOOL-dDerivedDocket-20.md:146`, `2026-09-14-spec-TOOL-dDerivedDocket-21.md:465`, and
spec 48's two (`:99` and the §9 restatement at `:363`). Four are edge-bullet shaped and ALL FOUR have
live reciprocals — unit 16 declares `hands-off TOOL-dDerivedDocket-19`
(`2026-09-14-spec-TOOL-dDerivedDocket-16.md:159`), unit 19 declares `hands-off TOOL-dDerivedDocket-20`
(`:115`), and units 15 and 28 declare theirs to 48 as L3's body records. So the predicate reds four
clauses across three specs, with zero innocent reds in the population. The fifth, spec 21's, is a
"version criterion" rather than an edge bullet and falls outside the predicate, which is the
near-miss the run was for.

**That measurement widens the finding.** L3 is not local to spec 48 — the stale-reciprocity claim is
in three specs of this build, two of them outside G7. The two outside this group are out of scope for
this record and should be raised wherever their own group is folded.

### L4 — spec 49's strongest piece of prior art cites the wrong review record (47)

**Address.** Spec 49 §10 Reuse audit, last paragraph, at `:352`.

**What is wrong.** §10 attributes the phantom-`MISSING` prior instance to "the `cBriefedPilot`
round-1 review record". Measured: `grep -n phantom memory/builds/cBriefedPilot/reviews/*.md` returns
exactly one hit, in the round-TWO record at
`memory/builds/cBriefedPilot/reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md:309` — "once as a
phantom `MISSING` row for the roster id. With every earlier spec terminal that phantom becomes
`next: <id> (MISSING - spec it first)`", which is precisely the rung boundary spec 49's §10 describes
and AC2 grades. The round-1 record, `2026-08-15-review-TOOL-cBriefedPilot-1-1.md`, mentions MISSING
only as a stale master-overview count.

**Why it matters at all.** A reader following the citation lands on an unrelated finding and
concludes the prior art was mis-remembered, which costs the one boundary AC2 grades its strongest
supporting evidence.

**Fix.** Name the file and line:
`memory/builds/cBriefedPilot/reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md:309`, and drop the
round number or correct it to that record's own sequence.

**Left-shift.** The tempting gate is: a spec citing a review record by build and round must name the
record's path, and the path must exist. `tools/check-spec-tokens.py` already resolves path-shaped
tokens, so the second half is the existing check and the first half is a requirement that the
citation BE a path.

**Measured, and the measurement kills the gate as stated.** Round-phrase citations of the form
"round-1 record" or "round-1 review record" occur 28 times across the 46 specs at HEAD. Most are
correct prose referring to a record the same sentence or a neighbouring line addresses by path, so a
ratchet demanding a path at every occurrence would red a large correct population — the same verdict
this build already recorded for the S-item citation proxy, and for the same reason. It stays a REVIEW
check: at spec-audit time, resolve every round-phrase citation in a §10 to an actual file before
accepting the prior art. That check finds this defect in one grep, which is how it was found.

## What this round means for the group

**No round-1 fixes to judge.** These seven specs are new. The instruction to judge whether each prior
finding's fix holds applies to the G3 record's blocker and highs, which is what these units were
promoted to close, and on that question the answer is good: each of the seven does close the G3
finding that promoted it, and not one of the sixteen findings above says otherwise. Every defect here
is in the units' own new text. That is a different pattern from this build's norm, where the fold text
carried most of the defects, and the reason is structural — there is no fold text yet.

**The dominant class has shifted.** Round 2 of G3 confirmed 107 findings nearly all in round-1 fold
text, and the class was "the fold rewrote one half of a pair". Here the class is "the spec describes
a world that has moved": H1, H4, H5 and L3 are all a spec asserting a state of a sibling, a table or
the tree that was true when the draft was written and is not true at the blob it was pinned at. Four
of fourteen defects, including two of five highs. The promotion pass wrote seven specs from one
record in one sitting, and the siblings moved underneath them while it did. Whoever folds should
re-read every cross-spec assertion in all seven against HEAD, not only the four named here — this
report checked the assertions its lenses reached, and a zero elsewhere is not a measurement.

**Precision and fan shape.** At 0.34 over seven fresh specs, the read is that the fan was correctly
sized for coverage and badly primed for corpus. Nineteen of the 31 refutations were code claims about
`tools/unattended/` that the specs had already ruled out of scope. The cheap fix for the next
multi-spec group is priming, not agent count: hand each lens the set's own §3 non-goals up front.

## Disposition

**Under `memory/guides/BUILD-METHOD.md` M4's severity rule**, and this is round 1 of this group, so
convergence is not yet measurable — there is no prior count for this subject to fall from.

- The five HIGH defects (H1 to H5) take M4's PROMOTE disposition on their face. Three of them should
  not: H1, H4 and L3 are spec edits with no new mechanism, and H2's fix is a paragraph rewrite plus
  one line in S1. Only H3 and H5 carry anything unit-shaped, and in both cases what is unit-shaped is
  the LEFT-SHIFT rather than the fix. The orchestrator should decide whether H1, H2 and H4 take the
  FOLD disposition despite their severity, and record the decision; this record does not make that
  call for it. The recommendation is FOLD for H1, H2 and H4, FOLD for H5's three-edit route, and FOLD
  for H3 with its scope item and criterion added in place.
- The five MEDIUM and four LOW defects FOLD into their specs as rev-2 bumps with §9 lines. All nine
  are paragraph-sized.

**Ordering for whoever folds.** Fold H2 before L2: both touch spec 48's refusal branch, and L2's
teardown sentence belongs in the S1 that H2 rewrites. Fold H1 before nothing — it is self-contained,
but it changes which sibling spec unit 49's criteria read, so run it before any re-read of unit 16.
Fold H5 before M-anything in spec 52, because its Edges bullet changes §3, which L1's row sits two
sections from. M4's §7 line in spec 53 should land in the same commit as M3's §5 row, since both are
that spec's readiness text.

**On the gate proposals, one thing must be said plainly, because this report grades specs for exactly
this.** Charter §7 requires a candidate gate predicate to be run over the real tree, printing hits
AND near-misses, before it is wired. **Only ONE of the eleven candidates below was actually run:
L3's reciprocity predicate, measured at four reds across three specs with its one near-miss named.**
Two more carry partial real measurements that are NOT the predicate's red count (M4's 19-of-46 leg
listing, M5's 22 pin occurrences of which one is in a refusal). The remaining eight are UNRUN, and
each says so in its own entry. Nobody should wire any of them on this report's authority; the
predicate goes over the tree first. An earlier draft of this report stated hit counts for those
eight as if they had been measured. They had not been, and the counts were wrong where they could be
checked — which is the finding this report makes about other people's specs, arriving in the report
itself.

## Left-shift, by class

Each entry carries its measurement status, because an unrun predicate is a proposal and not a gate.
MEASURED means it was run over the tree for this report with hits and near-misses printed. UNRUN
means it was not, and charter §7 blocks wiring it until it is.

1. **A cross-edit into a sibling spec with no observer** (H1, and M1's second route). Candidate: a §2
   scope item naming a sibling unit id and a verb of modification must be answered by a §6 criterion
   naming the same unit id. **UNRUN.** Population 46 specs, 606 criteria. Unit-shaped if it prices out.
2. **A criterion naming no subject at all** (M1). Candidate: every §6 "When" clause names a file
   path, a command or a unit id. **UNRUN** over the 606 criteria. Same unit as class 1.
3. **A spec premise asserting current behaviour that HEAD contradicts** (H2, and H4, H5, L3 in their
   describes-a-moved-world form). Does not gate over specs. The regression half gates one level down,
   per H2: an arm asserting `RB_OUT` survives the refusal branch — **UNRUN, but exact**, since the
   branch is one line at `tools/unattended/unattended.sh:185`. The review half is a documented check,
   every "today the code does X" sentence re-read at HEAD at spec-audit time, and belongs beside
   `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`. This class produced four
   of the fourteen defects and is the round's dominant one.
4. **A public entry point letting a foreign exception type escape** (H3). Candidate: a self-test arm
   over every public entry point with a scratch root, asserting the kit's own named refusal.
   **UNRUN** against today's existing entry points; the escape itself is measured.
5. **A criterion whose comparison is true by construction** (M2). Candidate: a floor graded by
   equality at the commit or by increase against the parent, never by `>=` against itself. **UNRUN**
   beyond the three known instances (specs 50, 52, 54), of which two are already correct.
6. **A reuse audit quoting a probe that could not see the language** (H5). Candidate:
   `reuse_lookup.py` reports an unscanned extension as a REFUSAL rather than a footnote. **UNRUN** —
   the tool was not executed for this report, and a non-zero exit reaches every caller. The review
   half needs no tool: grep the build's own spec folder before accepting "no seam".
7. **A declared bar omitting a leg the spec's own text defers to** (M4). Candidate: a spec naming a
   new identifier in a non-dark language must list `lexicon naming predicates` in §7. **PARTIAL** —
   19 of 46 specs list the leg, which is a population count and not a red count. The
   identifier-detecting half is unrun and is the hard half.
8. **A refusal whose cure is false for the caller that receives it** (M5). Candidate: an arm
   asserting the pin names are absent from the refusal `resolve_anchor` emits. **MEASURED as a
   correction**: a file-wide grep would be wrong, since `DEAD_PATH_PIN` and `ORPHAN_ID_PIN` occur 22
   times in `corpus_ids.py` and only `:275` is in a refusal message. The arm itself is unrun.
9. **An authored count or figure beside the source that owns it** (L1, L2). **UNRUN**, and the
   charter already bans the shape in prose. Documented check at spec-audit time: re-derive every §5
   count and cost from §2, §4 and HEAD.
10. **A stale reciprocity claim in an Edges block** (L3). Candidate: check 12's edge arm refuses an
    owes-the-line clause whose reciprocal is already present. **MEASURED — the only one.** Five
    clauses across four specs; four are edge-bullet shaped and all four red; the fifth (spec 21's
    version criterion) is the near-miss and falls outside. Zero innocent reds. Two of the three red
    specs are outside G7 and belong to another group's fold.
11. **A citation to a record that is not a path** (L4). **MEASURED and REJECTED as a gate**: 28
    round-phrase citations across the 46 specs, most of them correct prose. Stays a documented
    spec-audit check.
