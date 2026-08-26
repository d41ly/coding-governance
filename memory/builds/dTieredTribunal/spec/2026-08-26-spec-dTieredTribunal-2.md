# TOOL-dTieredTribunal-2 — the fold writes text nobody reviews, and that class is not in the catalogue

**Status:** CLOSED · rev-4 · 2026-08-26 · node a · Tier-1 · base da9e4cd2 · order 1 · streams tooling · ratified 2026-08-26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-build-TOOL-dTieredTribunal-1-acceptance-ledger.md](../build/2026-08-26-build-TOOL-dTieredTribunal-1-acceptance-ledger.md) | journal | TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-3 |
| [2026-08-26-review-TOOL-dTieredTribunal-1-closing-diff.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-closing-diff.md) | diff-review | TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-3 |
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-3 |
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md) | spec-audit | TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-3 |
| [2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round3.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round3.md) | spec-audit | TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-3 |

<!-- /gen:spec-records -->

## 1. Goal

`python tools/memory-tree/gotchas.py --for-diff` is the recurring-bug-class checklist the build
method hands every reviewer, and it can only emit classes that exist as records under
`memory/gotchas/`. The highest-value class measured on a recent build is not one of them, so the
checklist cannot select it. Add the record.

The record also has to fire on the diff a FOLD round actually produces. That diff is the spec files a
build keeps under its own `spec/` directory, rather than the fold rule or the harness that primes a
round. An anchor set reaching only those two reaches governance work and never a fold, which ships
the record inert — the ships-inert class already in this repo's catalogue.

## 2. Scope (IN)

- **S1** — a new record at `memory/gotchas/fold-text-is-unreviewed-surface.md`, carrying the front
  matter the existing records use and the sections the hygiene gate's record checks require.
- **S2** — the record's anchors are `/spec/`, `memory/guides/BUILD-METHOD.md` and
  `tools/workflows/tier2-review.js`. The `/spec/` token is the one that reaches a fold round's own
  write surface; the other two reach a diff that edits the fold rule or the harness that primes a
  fold round. The measurement behind that choice, and the arm refused for it, are in §7 F1. Anchors
  are DERIVED and not declared: `gotchas.py` reads the backtick-quoted path-like tokens out of the
  record body, so the record earns each of the three by citing it, and its derived set is whatever
  the finished body contains rather than only the three named here.
- **S3** — `python tools/memory-tree/gotchas.py --write` re-renders `memory/gotchas/INDEX.md` in the
  same commit as the record.
- **S4** — the new `gotcha-classes` inventory key is claimed by `memory/map/features/build-method.md`
  in the same commit, so the codebase-map coverage gate stays green. That dossier already claims
  `memory/guides/BUILD-METHOD.md`, it owns the fold rule this class is about, and its
  `gotcha-classes` list is empty today.
- **S5** — the record's evidence cites a TRACKED file. The measurement is at
  `memory/builds/dFramedEntrypoint/reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md`,
  which states the by-kind split of that round's surviving findings.
- **S6** — `python tools/codebase-map/gen_map.py --write` re-renders `memory/map/generated/` in the
  same commit as the S4 claim edit. `tools/codebase-map/test_codebase_map.py` byte-compares the
  committed artifacts against a live re-render, so a claim landed without a render reds the very bar
  AC5 asserts is green.

## 3. Non-goals (OUT)

- **Any change to the fold RULE.** The build method's fold-and-stop text stays exactly as written.
  Editing it is a governance-carrier change this build's rules withhold.
- **Extending the harness's fold priming.** The research names two fold instructions that reach no
  prompt today. Adding them is a prompt change to `tools/workflows/tier2-review.js` and belongs
  wherever a kind profile lands, which is the parked proposal.
- **A new gate.** The existing record checks over `memory/gotchas/` already grade the file, and the
  index-freshness check already grades the render.
- **Retrofitting the class onto past review records.**

## 4. Design

The class, stated once so the record can be written against it. A review round finds defects. The
fixes are FOLDED into the spec or the code. That fold is fresh text that nobody has reviewed, and on
the one build that ran the loop to completion it was where most of the next round's findings came
from. The tracked round-2 record splits its 62 surviving findings by kind as 25 the fold created, 17
the fold misreading its own finding, and 20 that round 1 missed. So the fold produced more findings
than the review it was answering had missed.

The consequence for a reader is the useful half. A fold is not bookkeeping and a round that treats it
as bookkeeping will pay for it in the next round. The two mitigations the same record names are
concrete: verify a did-not-land claim by reading the body at HEAD rather than the revision log, and
fold a DELETION rather than appending a negation beside the text it contradicts.

Both mitigations are recorded in the record and neither is imposed as a rule here, because the
record is a checklist entry and not a carrier of obligations.

## 5. Acceptance criteria

- **AC1** — When `ls memory/gotchas/ | grep -i fold` runs, it returns the new record, where today it
  exits non-zero with no output.
- **AC2** — When `python tools/memory-tree/gotchas.py --check` runs, it exits zero, which covers both
  the record's own shape checks and `INDEX.md` freshness.
- **AC3** — When
  `python tools/memory-tree/gotchas.py --for-paths memory/builds/dFramedEntrypoint/spec/2026-08-24-spec-dFramedEntrypoint-1.md`
  runs, the new class name appears in its stdout and the summary line counts it as anchor-selected.
  Today that same command prints `0 class(es) selected by an anchor + 4 universal`, which is how the
  criterion can fail. The argument is a FILE and must stay one. `normalise_paths` strips a trailing
  slash, so a directory argument arrives as a slashless string that none of `selectable()`'s three
  arms can match against a `/spec/` anchor. Proven by importing the shipped module: the anchor
  returns the empty set against `memory/builds/dFramedEntrypoint/spec` and returns the path itself
  against the file above. A directory argument would make this criterion's pass output byte-identical
  to its failure output, which is the could-not-fail shape this whole unit is about.
- **AC3b** — The positive arm, widened. When
  `python tools/memory-tree/gotchas.py --for-paths memory/builds/dHonouredPark/spec/2026-08-25-spec-dHonouredPark-1.md`
  runs, the class is selected there too. One file could be selected by accident; two under different
  builds is the anchor working.
- **AC3c** — The negative, and it is what makes F1's width argument observable rather than asserted.
  When `python tools/memory-tree/gotchas.py --for-paths memory/builds/dTieredTribunal/README.md`
  runs, the new class is NOT selected. That path is the discriminating case: it is a build record and
  not a fold surface, the REFUSED anchor `memory/builds/` selects it, and the TAKEN anchor `/spec/`
  does not. Re-derived with the shipped `selectable()` before this criterion was written, because an
  earlier revision named `memory/DECISIONS.md` here, which NEITHER anchor selects — so it could not
  fail under either arm and the reason given for it was false. A negative that both arms pass
  discriminates nothing, which is this unit's own subject turned on its own acceptance set.
- **AC4** — Three observations, because one command does not make all three. First, when
  `python tools/codebase-map/test_codebase_map.py` runs it exits zero, which is the
  `codebase-map coverage + freshness` leg and which fails on any inventory key that is neither
  claimed by a dossier nor present in the baseline. Second, when
  `grep -n fold-text-is-unreviewed-surface memory/map/features/build-method.md` runs it returns the
  claim. Third, when the same grep runs over `memory/map/baseline.toml` it returns nothing. The
  baseline half is stated as an ABSENCE and not as a removal: a key created by this unit was never in
  that file, so nothing can stop sitting there, and the header of `memory/map/baseline.toml` reserves
  it for the initial backfill in as many words.
- **AC5** — When the full bar runs with the record staged, the `memory hygiene` leg and the
  `codebase-map coverage + freshness` leg are both green.
- **AC6** — When `grep -n 'dFramedEntrypoint' memory/gotchas/fold-text-is-unreviewed-surface.md`
  runs, it returns the citation S5 requires, and the file it names resolves under `git ls-files`.
  S5's whole point is that the evidence is TRACKED, and no other criterion here reads the record's
  body: AC1 is a filename test, AC2 grades shape and index freshness, and AC3 grades selection.
  Numbered last rather than inserted, because one live sentence in section 2 and one revision-log
  line already cite AC5, and renumbering would strand both.

## 6. Gates

Two legs adjudicate this unit. Both are unguarded in `tools/gate-legs.json`, so both arm on every
bar.

- `memory hygiene`, which runs `bash tools/memory-tree/check-memory-hygiene.sh`. It carries the
  record's own shape checks and `INDEX.md` freshness. Index freshness is check 17 inside
  `gotchas.py --check` and is not a leg with a name of its own.
- `codebase-map coverage + freshness`, which runs `python3 tools/codebase-map/test_codebase_map.py`.
  It carries the S4 claim and the byte-comparison of the committed `memory/map/generated/` artifacts.

The kit self-tests `gotchas selftest` and `memory-hygiene self-test` are guarded on
`tools/memory-tree/` and `tools/lib/`. This unit's diff touches neither, so neither can arm for it.
This unit adds no leg.

## 7. Open questions

- **F1 — what makes the class selectable on a fold diff.** RESOLVED (agent, 2026-08-26, delegated).

Round 1 of this build's spec audit measured that the record as first scoped could never be selected
on the one diff class §1 says it exists to serve. Two arms were available, and only one survives.

*The anchor arm, taken.* Add a backticked `/spec/` token to the record body. Measured with the
shipped predicate, `selectable()` in `tools/memory-tree/gotchas.py`, over the tracked path set:
`/spec/` selects only paths that sit under a spec directory, and it selects every one of them. The
arm therefore buys the fold surface and no noise. The spelling refused alongside it is
`memory/builds/`, which selects roughly two thirds of the tree, most of it outside any spec
directory. That is near-universal selection bought under an anchor's name, and noise on a checklist
is how reviewers learn to skip the checklist.

NO ABSOLUTE COUNT IS WRITTEN IN THIS PARAGRAPH, and the reason is the same rule the rest of this
corpus follows: every one of them is derived from the tracked path set, all three moved between the
measurement and the commit that recorded them, and a number typed beside a source that owns it is
wrong on the next commit. The WIDTH claim is therefore stated as a ratio and OBSERVED by AC3c, which
names a path the refused anchor selects and the taken one does not. An earlier revision of this
paragraph deleted three such absolutes, asserted that none remained, and left a fourth standing two
sentences above the assertion.

*The `universal: true` arm, refused on two independent grounds.* It is semantically wrong first: the
flag marks the always-emitted core, and this class binds a FOLD pass rather than every diff, so the
flag would overstate the population by design. It also trips M3 veto 2: `.memory-tree.conf` declares
`UNIVERSAL_BUDGET="4"`, and `python tools/memory-tree/gotchas.py --report` prints
`universal : 4 (budget 4)`, so the arm needs a same-commit budget raise. A budget raise is an owner
call and not a text fix, and this run cannot ratify one.

Either ground alone would have parked this fork. Neither has to, because the anchor arm clears both
vetoes on its own evidence, so the fork resolves here rather than waiting on an owner turn.

## 8. Revision log

- rev-1 · 2026-08-26 · initial draft, authored by the unattended run under the standing mandate.
- rev-2 · 2026-08-26 · folded spec-audit round 1, the record at
  `memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round1.md`.
  Eight findings folded and one refused. The blocker trio 1, 13 and 31 is one defect and took one
  fix: §1 now names the fold diff as the population, S2 adds the `/spec/` anchor, AC3 observes a real
  fold range, and §7 F1 records the fork RESOLVED with both arms and their evidence. The trio's own
  proposed anchor was `memory/builds/`; the fold took `/spec/` instead, because re-measuring the
  proposal with the shipped predicate showed the non-spec majority, and the finding's parenthetical did
  not price that. 2 replaced AC4's `reuse_lookup.py` with `test_codebase_map.py`, which is the leg
  that actually adjudicates claim coverage — `reuse_lookup.py` takes a required query positional and
  returns 0 unconditionally, so it could not answer AC4 as written. 10 and 51 are one defect and
  added S6, the same-commit map render; 10 proposed `review-harnesses.md` as the claiming dossier and
  the fold used `memory/map/features/build-method.md` instead, which owns the fold rule and carries
  an empty `gotcha-classes` list. S6 names the generated DIRECTORY rather than listing its files,
  because `gen_map.py --write` owns which artifacts it renders and a file list beside it would be a
  second copy. 11 and 52 are one defect and one edit: `memory-tree hygiene` is not a leg, and both
  §6 and AC5 now read `memory hygiene`, with the `gotchas index freshness` hedge deleted rather than
  annotated, since index freshness is check 17 inside the hygiene leg. §6 also now names the guards
  that keep the two kit self-tests dark for this diff. The header carries `ratified 2026-08-26`
  because F1 resolved under the mandate. Refused: finding 27, the `node a` header token, which is
  true — this run authored the spec on node a while the build folder is node d's — so the difference
  belongs in the build README, not in a falsified header.

- rev-3 · 2026-08-26 · folded spec-audit round 2, the record at
  `memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round2.md`.
  Six findings folded, five of them created by the rev-2 fold itself. The BLOCKER, findings 1 and 10,
  is one line: AC3's `--for-paths` argument was the DIRECTORY `memory/builds/dFramedEntrypoint/spec/`,
  and `normalise_paths` strips the trailing slash, so none of `selectable()`'s three arms could match
  the `/spec/` anchor against the result. The criterion's pass output was byte-identical to its
  failure output. Re-derived by importing the shipped module before fixing: the anchor returns the
  empty set against the slashless directory and returns the path against the file. AC3 now names a
  FILE and says why it must stay one. AC3b is new and is the negative F1's noise argument owed —
  a decision log must NOT select. 25 and 37 are one rewrite: AC4 claimed the coverage leg adjudicates
  a baseline REMOVAL, but a key this unit creates was never in `baseline.toml`, so the claim is now
  three direct observations and the baseline half is stated as an absence. 16 added AC6, the only
  criterion that reads the record's own body for the tracked citation S5 requires. 9 and 14 deleted
  three derived counts from §7 F1 prose — 1024, 689 and 373 were all stale at HEAD, staled by the very
  commit that wrote them, so the argument now names the ratio and lets AC3b observe it.

- rev-4 · 2026-08-26 · folded spec-audit round 3, the record at
  `memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round3.md`.
  Round 3 CONVERGED at zero blockers. Three edits here, closing round-3 findings 3, 8, 12, 13, 16,
  20, 23, 25, 30 and 33. Counted from that enumeration and not beside it: three edits, ten findings.
  20 is the third: AC6's own justification claimed two live sentences cite AC5 where one does, which
  is the same narrate-your-own-history class spec-1 carried three instances of.
  23 with 3, 12, 16 and 30 is one defect and it is this unit's own subject turned on its acceptance
  set. AC3b's negative named `memory/DECISIONS.md`, which NEITHER anchor selects, so it could not
  fail under either arm and the stated reason for it was false. The predicate was re-run before the
  fix rather than after: `memory/builds/` HITS a build README and a review record and MISSES a
  decision log, and `/spec/` misses all three. The negative is now a build README, split out as AC3c
  so the positive arm keeps its own criterion, and AC3b's positive arm gained the backticked file it
  never named. Round-2 finding 14's width half, which rev-3 recorded as folded and did not fold,
  lands here as AC3c.
  8, 13, 25 and 33: the rev-3 fold deleted three absolute counts from section 7 F1 and then wrote
  that neither figure was written as an absolute, while one still stood two sentences above. The
  width claim is a ratio now and AC3c observes it.

## 9. Reuse audit

The seam is the memory-tree kit's own gotchas catalogue, `memory/gotchas/`, read by
`tools/memory-tree/gotchas.py`. Nothing is built: a record is authored into an existing catalogue
and an existing generator re-renders its index. `tools/codebase-map/reuse_lookup.py` returned
`gotcha-classes` inventory keys among its candidates for the review-harness phrase, which is the
same catalogue.

Recall terms used with `tools/memory-recall/query.py`: `tier2-review harness lens skeptic verdict
spec-audit diff-review blockers convergence trust counters unverified fan-out`. The query surfaced no
existing record of the fold class, which agrees with the direct probe over the catalogue directory.
