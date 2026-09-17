# cMendedVintage — the acceptance ledger for unit 23

**Serves:** journal DEPL-cMendedVintage-23

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh`
suite ran in this pass. Every criterion below was answered by replaying its own command against a
scratch fixture target under this run's scratchpad, or by calling the committed predicate directly;
the command is stated per criterion.*

## The one thing worth reading twice

**The escape was observed LANDING, on both branches, before the guard was believed.** An exit code
proves nothing here and neither does a diff of the target: the whole defect is bytes arriving in a
tree nobody diffed. With the one containment call staged out of this engine and everything else
identical, `update --write` against a fixture whose `attributes` row reads `../ESCAPED-23-a` exited
**0** and created `ESCAPED-23-a` in the fixture's PARENT directory, holding gov's real lf-pin block
— `# govkit:lf-pins`, the GENERATED banner, and the pin rows. The read-only preview of the same
fixture also exited 0 and printed `pins-moved`, a confident verdict computed from a file in another
tree, which is exactly what AC2 was written for.

**The withdrawal branch destroys rather than creates, and that was observed separately.** A file
planted OUTSIDE the fixture at `ESCAPED-23-c`, carrying gov's marker pair plus a `SENTINEL` line,
came back as `SENTINEL\n` alone after the staged-out run: gov spliced its marked region out of a
file in a repository the operator never named, at exit 0. That is the branch a guard written at the
join would never have reached, and it is why the call sits above the empty-pin exit.

**The candidate predicate was run over the real tree before it was wired, and its first draft was
wrong.** Not in the way `DEPL-cMendedVintage-21`'s was, but in the same class: crediting every
mutating call in a function to every binding of a name reported three read-only probes as unguarded
writes, because one function binds `dp` five times across as many loops. Both lists are below.

## The predicate, measured over `tools/govkit/govkit.py` before wiring

Every figure re-derived on this tree at this unit's tip. Widths 1 and 2 were run to price the
alternatives the review's wording admits; only width 3 is wired.

| Width | Population | Would red | False reds |
|-------|-----------|-----------|------------|
| 1 — any `target /` join with a non-literal operand | 33 | 33 | 31 |
| 2 — operand is a mapping subscript | 10 | 9 | 7 |
| 3 — subscript operand whose bound name reaches a write | 4 | 2 | 0 |

**Width 3, the wired one — the complete population, hits AND near-misses, all four rows.**

| Site (pre-fix) | Binding | Reaches | Verdict |
|---|---|---|---|
| the runner-file join in the leg writer | `rf = target / gr["file"]` | `write_atomic` | PASS — operand graded in the pre-write pass |
| the lf-pin rewrite | `_pw_path = target / _pw_row["path"]` | `write_text` | **HIT** — this finding |
| the lf-pin withdrawal | `_pd_path = target / pins_drop["path"]` | `write_text` | **HIT** — this finding |
| the write loop's own row | `dp = (target / row["path"]).resolve()` | `unlink` | PASS — inline resolve-and-compare |

**The near-misses that width 3 deliberately drops**, four more subscript joins that bind a name and
reach no write at all: the two read-only probes in `check` (`row["path"]`, `order["path"]`), the
rendered-destination existence probe in `apply` (`row["path"]`), and the classification read in
`update` (`row["path"]`). Refusing any of them buys nothing, because nothing is written. Three
further subscript joins are never bound to a name at all — two existence probes and one `is_file`
— and leave at width 2.

**What width 2 would have cost, named rather than asserted.** Seven of its ten are false reds, and
the one that matters is the write loop's own containment: it is spelled INLINE, with `.resolve()`
and `.relative_to()` under `except ValueError`, so a predicate written against the helper's NAME
reds the one join in this verb that already does the right thing. That is the outcome that gets a
structural arm waived rather than obeyed, which is why both spellings count.

**The first draft's own false reds, recorded because the brief asked for them.** Draft one reported
`dp = target / row["path"]` in `apply` as an unguarded write, crediting it with two `dp.write_text`
and `dp.write_bytes` calls that belong to two EARLIER bindings of the same name in the same
function. Draft one also over-counted widths 1 and 2 by meeting a wrapped join twice while walking
the syntax tree. Fixing the first needed a window that ends at the next rebinding; fixing the second
needed a dedupe on the join's own position. Both corrections are in the committed predicate and both
figures are corrected in the spec at rev-2.

**Evidences:** DEPL-cMendedVintage-23

- AC1 — `python tools/govkit/govkit.py update --target <fixture> --write` against a scratch target
  whose receipt's `attributes` row reads `../ESCAPED-23-a`. Exit 2, stderr
  `the resolved destination '../ESCAPED-23-a' leaves the target repository (normalises to
  '../ESCAPED-23-a') -- refusing the whole run`, and the escaped path does NOT exist afterwards. The
  criterion's red-when was closed by observing the same run with the call staged out: exit 0, and
  the file present outside the fixture carrying gov's block. The assertion is on the file, never on
  the exit code.
- AC2 — `python tools/govkit/govkit.py update --target <fixture>` over the same fixture, no
  `--write`. Exit 2 with the same refusal, and `pins-moved` never printed. With the call staged out
  the same preview exits 0 and prints `pins-moved` — a verdict derived from a file outside the
  fixture, on the run an operator approves. The refusal's `Source:` field reads `the `attributes`
  row of the target's own receipt`, which is the part this unit controls; the helper's own trailing
  sentence still blames a `prefix` in the target's deploy.toml and is false for this caller, noted
  in section 5 of the spec and left alone as the helper is out of scope.
- AC3 — `python tools/govkit/govkit.py update --target <fixture> --write` over a fixture whose
  receipt names the escaping path AND drops the pinning kit, so the arm takes its withdrawal branch.
  Exit 2, the same refusal, `pins-withdrawn` never printed, and a marker-carrying file planted
  outside the fixture is byte-identical afterwards. Staged out: exit 0, `pins-withdrawn` printed,
  and that outside file comes back as `SENTINEL\n` with gov's region spliced away. This is the
  criterion that grades the guard's PLACEMENT rather than its presence.
- AC4 — `python tools/govkit/govkit.py selfcheck` over this repository. Exit 0, and the new note
  reads `root-join writes on receipt-supplied values: 0 ungraded`. The failing case was observed:
  feeding the committed predicate this engine's source with the two deleted joins staged back in
  returns exactly two rows, `_pw_row["path"]` and `pins_drop["path"]`, at the two write sites the
  review cited. Both halves are permanent arms in the suite.
- AC4 — `python tools/govkit/govkit.py selfcheck` over this repository, red-when half. The write
  loop's own `dp` is in the graded population and is NOT reported, so the inline spelling counts as
  a containment check and the arm does not red correct code. Asserted positively by a committed arm
  rather than left as an absence.

## What is OWED

- The permanent arms added to the suite — fourteen `check` calls under the `[-23]` label — were
  replayed OUTSIDE the suite in this pass, in their committed order, against fixtures built by the
  same recipe: 14 ok, 0 failures. Replaying them rather than reading them is the point; the ordering
  was changed mid-build so the staged-break run comes LAST on each fixture, and the replay is what
  proved the real refusals still refuse on a fixture the break has not yet touched.
- Their verdicts INSIDE the suite are OWED to the main loop's single bar. The suite run reported in
  this unit's summary was launched before that reordering, so it graded a different sequence, and a
  fresh full run did not fit this pass's bound.
- Nothing else. No criterion here needed a gate, a merge bar or a `*.test.sh` to observe.

## What this unit did NOT fix, deliberately

The dirty-path carve-out on this same `attributes` row is the closing review's third blocker and is
specced by its own unit. `demand_contained_dest`'s own trailing sentence, which blames a `prefix`
this caller does not read, is left standing: four other callers depend on that text and rewriting it
is a change to a shared refusal message that no criterion here grades. The structural arm proves one
shape and says so in its own docstring; it does not assert that this engine contains every write.
