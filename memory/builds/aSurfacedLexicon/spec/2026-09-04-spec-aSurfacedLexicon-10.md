# TOOL-aSurfacedLexicon-10 — `--expand`, the one-time widening the canon bounds

**Status:** CLOSED · rev-5 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 6 · ratified 2026-09-06

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aSurfacedLexicon-10-acceptance-ledger.md](../build/2026-09-06-build-TOOL-aSurfacedLexicon-10-acceptance-ledger.md) | journal | — |
| [2026-09-06-review-TOOL-aSurfacedLexicon-10-diff-review-round2.md](../reviews/2026-09-06-review-TOOL-aSurfacedLexicon-10-diff-review-round2.md) | diff-review | — |
| [2026-09-06-review-TOOL-aSurfacedLexicon-10-diff-review-round3.md](../reviews/2026-09-06-review-TOOL-aSurfacedLexicon-10-diff-review-round3.md) | diff-review | — |
| [2026-09-06-review-TOOL-aSurfacedLexicon-10-spec-audit.md](../reviews/2026-09-06-review-TOOL-aSurfacedLexicon-10-spec-audit.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

Give an adopted project the second and last supported declaration transition: expand the verb table
once, per its own needs, from the frozen canon and never from its own corpus. Today
`tools/lexicon/adopt-lexicon.sh:247-251` refuses outright when a declaration exists, so an adopter who
needs a concept the seed missed has no tool-supported route at all and edits by hand with nothing
bounding what they add.

## 2. Scope (IN)

- **S1** — `--expand` joins the mode allowlist at `tools/lexicon/adopt-lexicon.sh:184` and its usage
  line, beside `--scaffold`, `--check` and `--render`.
- **S2** — The guard reads `expanded=` from the conf and refuses when it is non-empty, naming the
  stamp. The read uses the same CRLF-hardened shape as the `ratified` read at
  `tools/lexicon/adopt-lexicon.sh:226` — `tr -d '\r'` FIRST, because an anchored `s/"$//` cannot strip
  a quote a carriage return follows and the residue `"\r` reads as a non-empty value, which inverts
  the refusal.
- **S3** — The candidate set is the live canon representatives minus the representatives the `VERBS`
  table already declares. Liveness is decided by the expression `live = {forms[v] for v in counts if
  v in forms}` in `tools/lexicon/scaffold_lexicon.py`, whose TEXT is unchanged and whose HOME moves:
  rev-5 lifts it out of `main` into `derive_candidates` beside it, so the one expression gains a
  second caller instead of a second copy. Cited as an expression and not a line — it was at `:146`
  when this was written and at `:184` when it was built, and rev-1 had already corrected the same
  cite once. A token in no cluster cannot enter a proposal, and that closure is the reason this unit
  is safe to build at all.
  The candidate set comes off `live` DIRECTLY and never off `canon.CLUSTERS`. Filtering through the
  shipped tuple would make the subset property true by construction at the wrong place, and AC5's
  staged break would then leave the arm green — grading its fixture rather than the closure.
- **S4** — The unruled tail prints BELOW the proposals, under a header stating in words that these are
  not proposals and that a row here would be the mirror defect the kit was rebuilt to close. It is
  evidence for an owner, never a candidate.
- **S5** — `--expand --stamp` writes `expanded="<iso-date> <sha>"` into the conf, the sha naming the
  tree the candidate set was measured against.
- **S6** — A selftest arm asserts the candidate set is a SUBSET of the canon representatives, run
  against a synthetic fixture repo whose `VERBS` table is deliberately short. This arm is the whole
  point of the unit: it is what stops an adopter legalising its own existing mess.
- **S7** — The output tells the operator that expansion moves pins and that the pins must be
  re-measured and re-pasted, so an expansion cannot land without its cost showing in the diff.
  **RE-AUTHORED AT rev-5, and the reason is this criterion's own subject.** It used to name the pins
  by hand: three scalars, one of which (`LAYER_OFFENDER_PIN`) no longer exists at all, at three line
  numbers that had moved, while insisting no `PINS:` block existed at this build order — a block that
  now exists, because the unit which introduces it landed while this one sat parked. Every clause was
  wrong in a different direction, in a criterion whose whole point is that a value written beside the
  source that owns it rots. So the output NAMES NO PIN. It says that every pasted row moves one,
  that each is a two-sided equality so an unrecorded drain reds exactly as a rise does, and it points
  at `--measure`, which prints the rows this declaration actually produces.

## 3. Non-goals (OUT)

`--expand` does not WRITE the `VERBS:` block. Proposals go to stdout and an owner pastes them, which
keeps the curation step where the whole design puts it. Only `--stamp` touches the conf, and it
touches one scalar.

It does not stop an owner clearing the stamp and expanding again. Nothing running under the owner's
own uid can, and the honest claim is bounded: the stamp makes a second expansion a visible edit in a
tracked file rather than an invisible habit.

It does not touch the canon. Adding, replacing or deleting a cluster is `TOOL-aSurfacedLexicon-11`'s
`CANON:` overlay and its unfreeze stamp. This unit's proposals are drawn from whatever
`canon.build_form_index()` resolves at run time, so the two compose without either knowing about the
other.

It does not emit a `CANON:` header. `TOOL-aSurfacedLexicon-11` asserts that on the declarations leg
with a predicate narrowed to an emitted block header, and this unit must not be the edit that breaks
it. The predicate is narrow rather than a bare grep because a bare one already matches the descriptive
comment at `tools/lexicon/scaffold_lexicon.py:181`; see AC8.

It adds no bar leg, so it owes no wall-clock ceiling and no `testsuite-count-waivers.txt` row.

## 4. Design

### Data model

Three sets. `reps` is the 20 canon representatives from `tools/lexicon/canon.py:55-81`. `live` is the
representatives with at least one site in the corpus, from the expression
`live = {forms[v] for v in counts if v in forms}` in `tools/lexicon/scaffold_lexicon.py` — cited
as an expression, never as a line, for the reason S3 gives. `declared` is the keys of the conf's
`VERBS` table, folded through the form index first. The
candidate set is `live - declared`, and `candidates ⊆ reps` holds by construction because `live ⊆ reps`
by the definition of `forms`.

The unruled tail is a different computation entirely and must never be joined to the candidate set: it
is the leading tokens with a live site that are in no cluster AND in no `VERBS` row, printed with
their counts.

**The stamp's dirty test is NAMED, and the naming is load-bearing.** `--stamp` refuses on a dirty tree,
and dirty means this repo's own tracked-only two-sided diff: `git diff --quiet` AND `git diff --cached
--quiet`, deliberately NOT `git status --porcelain`. The definition and the reasoning behind it already
live in this tree at `tools/govkit/govkit.py:4008`, `dirty_claimed_paths`. The choice decides whether
AC7 can ever be exercised: in a fixture-shaped repo the kit is copied in untracked by design, so `git
status --porcelain` is non-empty forever and a `--porcelain` refusal could never fire, while both diff
checks read clean there and the stamp writes.

### Inventory

**The candidate set on THIS corpus is empty, measured at writing time.** All 20 canon clusters are
live here and all 20 representatives are already declared, so `live - declared` is the empty set and
`--expand` on this repo would propose nothing. The three declared rows outside the canon are `arm`,
`cmd` and `seed`, which is the legal direction — a human may ratify a row the canon does not hold, per
`tools/lexicon/canon.py:48-50`.

That measurement changes this unit's acceptance criteria and the change is the point. The research
record's proposed check reads "on this corpus it proposes only canon clusters not already declared",
which resolves to the empty set here and would therefore pass with the candidate computation deleted.
That is the could-not-fail shape the build README's rule about zero populations exists to refuse. The
subset assertion in S6 must run against a synthetic fixture with a short `VERBS` table, and a second
arm must assert the candidate set is NON-EMPTY on that fixture, or the subset assertion is vacuously
true.

**EVERY `--probe` CITATION BELOW IS DEAD, struck at rev-5 rather than deleted so a later reader can
see what happened to the evidence.** `TOOL-aSurfacedLexicon-3` removed that mode at build order 1,
five orders before this unit, so the two figures this section offers as its REPRODUCIBLE alternative
— `417 definition(s) lead with a token in NO cluster and NO row`, and `would propose 20 of 20
cluster(s)` — cannot be re-derived by anyone. S3's escape hatch, "state its figure in the probe's
terms", is not available. What replaced them is the shipped verb: `python <engine> --expand` prints
the candidate count and the tail count it computed, and every load-bearing figure below reproduces
through it. Measured at rev-5 on the tree the unit was built on: 20 clusters, 20 live, 23 declared
rows of which three are outside the shipped table, candidate set EMPTY, and a tail of 493 distinct
tokens over 897 definitions — the second of which is the same number `--check` prints as `unruled=`,
because the verb now reads that classification instead of re-deriving it.

Measured by a scratchpad script over `lexicon.tracked_files(root)`, importing `canon.CLUSTERS`,
`canon.build_form_index` and the conf's `VERBS` through `lexicon_conf.load_conf`:

| Fact | Value |
|---|---|
| Canon clusters | 20 |
| Clusters with a live site here | 20 |
| Representatives already declared | 20 |
| Candidate set on this tree | 0 |
| Declared rows outside the canon | 3 |
| Distinct unruled tokens in the tail | 267 |

The tail figure moved and the figure it replaced was wrong for this rev. Re-running that scratchpad
script at the run's base `6c670b02` returns 267 distinct unruled tokens; the `258` this table carried
at rev-2 was measured at `d0a18683` and is stale, because the commit between them added tracked
Python. **THAT FIGURE IS NOT REPRODUCIBLE FROM THIS DOCUMENT and the implementer must not treat it
as one.** The script is uncommitted and this spec gives no invocation, so `267` carries no command,
which this build's own rules forbid. An independent reconstruction over the same corpus returned
255 distinct tokens across 437 definitions, so the two do not even agree. What IS reproducible is
the shipped probe's own adjacent measurement: `python tools/lexicon/lexicon.py --probe` at
`6c670b02` prints `417 definition(s) lead with a token in NO cluster and NO row`, a DEFINITION
count rather than a distinct-token one. S3 must either commit its derivation or state its figure in
the probe's terms; until it does, no acceptance criterion may depend on `267`. Every load-bearing figure above it — 20 clusters, 20 live, 20 declared, candidate set 0 —
reproduces unchanged at the new base, and `python tools/lexicon/lexicon.py --probe` independently
prints `would propose 20 of 20 cluster(s)`.

The unruled tail's top rows at that base are `a` at 18 sites, `git` at 12, `demand` at 10, `signal` at
8, `kit` at 8 and `bounded` at 5. Those are the names S4's header exists to keep out of the proposal
list, and their presence at the top of the tail is what makes the header a live warning rather than a
decoration.

**A correction to the research record, verified against source at writing time.** That record cites
the anti-mirror closure at `tools/lexicon/scaffold_lexicon.py:143`. At `cd8ab0d2` line 143 is
`suffix_offenders = _measure_suffix_offenders(root, files)` and the closure was three lines below
it. The expression is byte-identical to the one the record quotes; only the line moved — and it
has moved twice more since, once inside this build. CITE THE EXPRESSION,
`live = {forms[v] for v in counts if v in forms}`. Every number in this paragraph is a frozen
quotation of what the research record said at `cd8ab0d2`, not a live instruction: rev-5's first
cut left the imperative `Cite 146` standing, and by then line 146 was a comment ABOUT the fix.

**A second measured absence.** `.lexicon.conf` carries no `expanded=` key today and no
`canon_unfrozen=` key either; the only stamp in the file is `ratified="2026-08-24 node d"` at line 183.
So S2's guard also has an empty population on this tree and its refusal cannot be observed here
without a fixture conf. Both arms of this unit are fixture-only, and the spec says so rather than
letting a green selftest imply otherwise.

### Migration

`TOOL-aSurfacedLexicon-12`'s conf rewrite introduces the `expanded=""` key. Until it lands, an absent
key reads as empty and `--expand` proceeds, which is the correct reading of "never expanded". The
guard must distinguish absent from empty only in its message, not in its verdict.

The SAME timing hazard applies to the pins S7 names, and rev-2 handled it here for `expanded=` only.
That unit also introduces the `PINS:` block, at order 7, one order after this one — so at this unit's
own build order there is no block to re-paste, only the three `*_OFFENDER_PIN` scalars at
`.lexicon.conf:164-166`. S7 is worded against the scalars for that reason, and re-wording it to name
the block is an edit that belongs to whichever unit lands after 12, not to this one.

### Rollout

`--expand` is additive: an adopter who never runs it sees no change, and `--scaffold`, `--check` and
`--render` keep their BEHAVIOUR byte for byte. **Not their code, and rev-5 corrects that claim.** The
mode allowlist edit is one change to an existing path; the build made FOUR more, and the fourth is
the one that matters.

Three are behaviour-preserving refactors. `--check`'s two scalar reads now route through
`read_conf_scalar`, which is one function where there were two verbatim copies of a pipeline whose
correctness is entirely in the order of its stages — the third copy was this unit's, which is what
forced the extraction. `--scaffold` reads its vocabulary through `derive_candidates` rather than
computing it inline. And the engine's measurement pass returns its own scan so this mode does not
walk the corpus a second time.

**The fourth is not behaviour-preserving and rev-5's first cut omitted it, which is round-2's F10
re-earned one item short.** `OPTIONAL_SIBLINGS` PERMANENTLY WIDENS `check_self_containment`: before
it, that predicate would have flagged the engine's own `import scaffold_lexicon` in a kit copy
installed without the scaffolder; after it, it never can. That refusal is printed on `--check`, the
leg that binds at the merge. The allowance is one name, its own comment states what it does not buy —
nothing about HOW the import is written — and the property it assumes is armed at runtime on both
modes plus a staged break, because a name added there without those arms is the hole it is written
not to be. Round-2 F10, corrected at round-3 M3.

### Files touched (estimate)

`tools/lexicon/adopt-lexicon.sh` (the mode, the guard, the stamp write),
`tools/lexicon/scaffold_lexicon.py` (a second entry point for the candidate computation, reusing
the closure expression rather than copying it), `tools/lexicon/selftest.py` (the fixture and its
arms), and
`tools/lexicon/README.md`. ESTIMATE on size; nothing comparable ships to measure against.

### Alternatives rejected

Proposing off-table tokens the canon does not map elsewhere. Rejected on the measurement above: seven
of this corpus's top unruled tokens are among the ten non-verbs the original frequency-ranking defect
produced, per `tools/lexicon/canon.py:40-47`. An expansion that offered them would reinstate exactly
the defect the canon closed.

Writing the proposals straight into the conf. Rejected because the gate's structural brake depends on
a human writing the negative: `tools/lexicon/lexicon.py:503-511` reds any `VERBS` row carrying no
negative, so a hand-pasted tail row is born failing the gate while a canon-rendered row parses green
unaided. Auto-writing would hand back a green file nobody read.

## 5. Production-readiness checklist

- security — N/A. Reads tracked files and the conf, writes at most one scalar, no network.
- perf / scale — one corpus walk, the same one `--scaffold` already pays for. `lexicon wiring`'s
  ceiling of 330 s in `tools/gate-legs.json` is untouched because `--expand` is not on any leg.
- a11y — N/A. A stdout report on a CLI has no rendered surface.
- i18n — N/A beyond the kit-wide ASCII limit of `subtokens.py`, which this unit inherits and does not
  widen.
- error / empty / loading states — the empty candidate set is the NORMAL case on a well-adopted repo
  and must print as such, naming that the table already declares every live cluster. A blank run reads
  as a broken tool.
- observability — the run prints the candidate count, the tail count and the stamp it would write, so
  an operator can read the cost before pasting anything.
- risks — the stamp is a single mutable scalar in a shared tracked file, so two nodes expanding
  concurrently conflict on one line and cannot reconcile additively. That is the same hazard owner
  ruling Q2 created for the pins, and unlike the pins this scalar is written once in a project's life,
  so the row-shaped mitigation does not apply and the collision is accepted rather than engineered
  away. The sha widens that collision rather than narrowing it, which is a cost the F2 pick carries
  knowingly.
- risks, second — the dirty refusal blocks the operator exactly when they have done the work the
  design asks for. §3 has them pasting proposals by hand and S7 has them re-pasting pins, both into
  the same `.lexicon.conf` the candidate set reads, and nothing today enforces the ordering that
  would let the measuring run start clean. Path-scoping the refusal to the files the measurement
  actually read is the mitigation this repo already shapes elsewhere, in `dirty_claimed_paths`, and
  it is not built here.
- testing + left-shift gates — the synthetic fixture plus a non-emptiness arm and a subset arm; the
  observed-RED criterion is AC5.
- migration / rollback — additive, single-commit revert; a written stamp is one line to delete.
- user docs — `tools/lexicon/README.md` gains the transition, and the rendered Skill is untouched
  because `--expand` is an owner action rather than an authoring one.

## 6. Acceptance criteria

- **AC1** — When `bash tools/lexicon/adopt-lexicon.sh --expand` runs against a fixture conf carrying a
  non-empty `expanded=`, it refuses, names the stamp, and exits non-zero.
- **AC2** — When that same fixture conf is rewritten with CRLF line endings, the refusal still fires.
  The residue `"\r` must not read as a non-empty value in the opposite direction either, so the arm
  asserts the verdict and not just the exit code.
- **AC3** — When `--expand` runs against a synthetic fixture repo whose `VERBS` table declares only
  `build` and `read`, the proposal list is NON-EMPTY and every entry is a representative of
  `canon.CLUSTERS`. Both halves are asserted, because a subset assertion over an empty set is
  vacuously true.
- **AC4** — When that same `bash tools/lexicon/adopt-lexicon.sh --expand` fixture run prints its
  unruled tail, no token in the tail appears in the proposal list, and the header above the tail
  states in words that these are not proposals.
- **AC5** — When the expression `live = {forms[v] for v in counts if v in forms}` in
  `tools/lexicon/scaffold_lexicon.py` — cite the EXPRESSION and not a line; it was `:146` when this
  was written, `:184` when it was built, and `:143` one revision before that — is staged as
  `live = {forms.get(v, v) for v in counts}`, so that `live` admits a token in no cluster, the subset
  arm in `tools/lexicon/selftest.py` goes RED; unstaging returns it to green. The RED is observed before this
  unit is called done, and it is the only proof that the arm grades the closure rather than the
  fixture. The break this criterion named at rev-2 — deleting `if v in forms` from the comprehension —
  does NOT grade the closure and must not be used: building the form index and evaluating `{forms[v]
  for v in Counter({'build': 3, 'git': 2})}` raises `KeyError: 'git'`, so the arm would red BY
  EXCEPTION and certify nothing about the subset predicate. The `forms.get(v, v)` form yields
  `{'build', 'git'}` and is the break that grades it.
- **AC6** — When `bash tools/lexicon/adopt-lexicon.sh --expand` runs on THIS repo unmodified, it
  proposes nothing and says so in words, naming that all 20 canon clusters are already declared. The
  empty case is asserted as a message, not as silence.
- **AC7** — When `--expand --stamp` runs on the fixture, `expanded=` is written with a date and a sha,
  the file keeps LF endings, and a second `--expand` on the result hits AC1's refusal. The dirty test
  the arm exercises is the tracked-only two-sided diff, `git diff --quiet` and `git diff --cached
  --quiet`, and never `git status --porcelain`: with the kit copied in untracked the porcelain form is
  non-empty forever, so a refusal built on it could not be exercised and this criterion would be
  unobservable for the life of the kit. The fixture needs one added line to satisfy the rest. The
  bespoke scaffold fixture runs `git init -q` plus `git add` and stops, so `git rev-parse HEAD` exits
  128 on an unborn branch and there is no sha to write. Committing the already-staged files does not
  contaminate the graded corpus — the warning at `tools/lexicon/selftest.py:95-99` is against staging
  `-A`, not against committing — and after that commit `git ls-files` in the fixture still returns the
  fixture sources alone, with the copied-in `kit/` still reported `??` by `git status --porcelain`. The
  LF clause is the one with a reproduced failure behind it: a CRLF conf INVERTS the unratified-seed
  refusal, recorded at `tools/lexicon/scaffold_lexicon.py:218-222` and
  `tools/lexicon/adopt-lexicon.sh:223-225`, so the stamp write must not be the edit that reintroduces
  CRLF.
- **AC8** — When `python tools/lexicon/lexicon.py` runs after this unit lands,
  `TOOL-aSurfacedLexicon-11`'s structural guard against a `CANON:` header emitted by
  `tools/lexicon/scaffold_lexicon.py` is still green, so this unit has not opened the path by which the
  mirror returns through the proposal body. The predicate is that unit's NARROWED one, matching only an
  emitted block header. It is NOT `grep -c CANON tools/lexicon/scaffold_lexicon.py` equal to 0: that
  command returns **1** on this worktree, matching the one descriptive line the scaffold carries
  (`# PROPOSED from the SHIPPED CANON`, at `:181` when this was written and `:217` when it was built),
  so the research record's bare-grep form would red the tree it ships against.
  **AND THE COUNT IS RATIONED, which rev-5 found the hard way.** A landed arm asserts the LOOSE form
  matches EXACTLY ONE line of that file, so the caps substring is spent and no new code or comment in
  it may use the word. That arm reds before the narrow one this criterion watches, and it is the arm
  an implementer actually trips. Re-measured for this spec; `TOOL-aSurfacedLexicon-11`'s AC8 and F1 own the predicate.

## 7. Gates

`lexicon wiring` (guard `[]`, ceiling 330) runs `adopt-lexicon.sh --check` on every bar and must stay
green across the mode-allowlist edit. `lexicon selftest` (chunk `selftests`, subject `kit`, ceiling
880) carries the fixture and both arms, and it is invisible to the push boundary unless
`GATE_SELFTESTS=1` is set, which no boundary sets — so the subset assertion is on-demand coverage and
this spec states that rather than implying a push-time guarantee. `lexicon naming predicates` (chunk
`declarations`, ceiling 300) must stay green: this unit moves no pin. `memory-tree hygiene` grades this
spec. No new leg, so no new ceiling and no `testsuite-count-waivers.txt` row is owed.

## 8. Open questions

**F1 CAME BACK FROM THE OWNER TURN AND IS RESOLVED; THIS UNIT IS BUILT.** It was parked at rev-3
because both LISTED options fell to the veto ladder, which left no resolver the standing mandate
delegates. The owner took the route the park had measured and flagged as unlistable under M3 — an
importable `derive_candidates`, beside the closure, reached from the engine's dispatcher — and that
is what rev-5 builds. F2 was already resolved and its ruling is written into §4, §5 and AC7 above;
it now has something to be built into.

- **F1 — Where does the candidate computation live?**
  The refusal PREDICATE is at `tools/lexicon/scaffold_lexicon.py:98`, `if len(argv) != 2 or
  argv[1].startswith("-")`. The `:100-104` this fork cited at rev-2 is the message and the `return 2`
  below it, and the distinction matters because the predicate line is the one a veto turns on. It
  refuses any flag with the message that the script takes one conf PATH and has no options of its own,
  so a second mode there means reversing a deliberate refusal. The alternative is computing candidates
  in `tools/lexicon/lexicon.py` and leaving the scaffold untouched. The claim written here at rev-2 —
  that this would CREATE the two-readers-of-one-fact class — is REFUTED. `lexicon.py` already holds a
  second independent reader in `run_probe` at `:1053-1136`, with its own corpus walk at `:1075-1092`,
  its own `canon.build_form_index()` at `:1065` and its own live-cluster set at `:1101-1105`. The class
  exists today, with two members. The refutation is itself qualified: `TOOL-aSurfacedLexicon-3` deletes
  `run_probe` at build order 1, five orders before this unit needs it, and neither spec cross-referenced
  the other until this rev.
  Recommendation as first written: a second entry point in `scaffold_lexicon.py`, an importable function
  the shell calls through a mode flag, so line 146 keeps exactly one reader. THAT RECOMMENDATION DID NOT
  SURVIVE ADJUDICATION — see the park below.

- **F2 — What sha does `--stamp` write when the worktree is dirty?**
  The design's justification for the sha is reproducibility: it names the tree the candidate set was
  measured against. A dirty worktree has no such sha, and `HEAD` names a tree the measurement did not
  read. Options are refusing to stamp on a dirty tree, stamping `HEAD` with a dirty marker, or dropping
  the sha and keeping the date. Recommendation: refuse on a dirty tree and say why. A stamp that names
  a tree the run did not measure is worse than no sha, and expansion is a once-per-project action where
  demanding a clean tree costs an operator nothing.

**PARKED (agent, 2026-09-04, delegated): F1 — NO RESOLVER; the fork is PARKED, not resolved.**

Both listed options are vetoed and M3 does not license a repaired version of a vetoed option, so
this mark records a park rather than a pick.

Option B — compute the candidates in `tools/lexicon/lexicon.py` — falls to veto 1. AC5 names the
staged line BY PATH: "When `tools/lexicon/scaffold_lexicon.py:146` is staged with the cluster filter
removed … the subset arm in `tools/lexicon/selftest.py` goes RED". Under B the arm grades a
`lexicon.py` copy, so breaking `scaffold_lexicon.py:146` leaves it GREEN and AC5 is unsatisfiable
without re-authoring it. The spec calls AC5 "the only proof that the arm grades the closure rather
than the fixture", so that re-authoring removes the unit's only observed-RED criterion.

Option A — a second entry point in `scaffold_lexicon.py` REACHED THROUGH A MODE FLAG, reversing the
no-options refusal — falls to veto 3, widening a write surface beyond what the unit risk tier
priced. §5 prices this unit at "writes at most one scalar". The guard being reversed is at
`scaffold_lexicon.py:98` (`if len(argv) != 2 or argv[1].startswith("-")`; the spec's `:100-104` cite
covers the message and the return, not the predicate) and its ten-line header states why it exists:
`scaffold_lexicon.py --help` is a well-formed one-argument call, so `--help` became the WRITE
DESTINATION and a real adopter (incms/main, 2026-08-23) committed and pushed a file literally named
`--help` through a 62-leg bar. Its own words: "this script is the one that WRITES, so the refusal has
to be here too". The mode flag is part of how §8 NAMES option A, so vetoing the mechanism vetoes the
option; §3's read-only non-goal is the only thing holding the new mode harmless, and a non-goal is
not a guard.

With rung 1 discarding B and rung 3 discarding A, only vetoed options stand. A veto is not a licence
to take the vetoed option, so the fork is parked.

**RESOLVED (owner, 2026-09-06): F1 — the importable `derive_candidates`, which was the route the park
measured and could not itself ratify.**

The park's own closing paragraph named it: "second entry point" and "mode flag" are separable, and
`scaffold_lexicon.py` imports cleanly, so a function beside the closure reached from the engine's
existing dispatcher keeps AC5's locus exactly and touches no guard. That is not a listed option and
M3 does not license one, which is why the fork went to an owner turn rather than being resolved
against the ladder. The owner ruled it in, and the ladder's two vetoes are both satisfied rather than
waived: the closure keeps ONE home in `scaffold_lexicon.py`, so AC5's staged break at that expression
reds the arm as written; and `scaffold_lexicon.py:112`'s flag-arity guard is untouched, because the
module is IMPORTED and its `argv` never sees a flag at all.

Three facts the build measured that the ladder's reasoning had assumed otherwise, recorded because
they change what the resolution costs rather than whether it holds:

- The import must be LAZY and function-local, not merely deferred by taste. `scaffold_lexicon` reads
  `lex.KNOWN_EXTS` in its module BODY, above which the engine's own definition sits, so a top-level
  `import scaffold_lexicon` in the engine raises `AttributeError` out of the sibling and the engine
  stops importing at all. A landed arm also runs `--check` against a kit copy with the scaffolder
  DELETED and asserts it is green, so the import must not exist on the default path either.
- Reaching the closure through an import loads a SECOND copy of the engine at run time: run as a
  script the engine is `__main__`, so the sibling's `import lexicon` finds nothing in `sys.modules`
  and imports it again under its own name. Harmless — that module's body is assignments and a path
  insert — but nothing may be compared by identity across the boundary, and the suite already
  asserts one such identity elsewhere.
- The park's refutation that "the two-readers class exists today, with two members" is now FALSE
  rather than merely qualified: `TOOL-aSurfacedLexicon-3` deleted `run_probe` at build order 1, so
  the engine holds no second corpus reader. That strengthens the ruling instead of weakening it —
  computing candidates in the engine would have RE-CREATED the class the deletion had just closed.

WHAT THE OWNER TURN SHOULD DECIDE, stated because it is cheap and measured, not because it is
ratified here. "Second entry point" and "mode flag" are separable: `scaffold_lexicon.py` imports
cleanly with no side effects, so an importable `derive_candidates(...)` beside line 146, reached
from `lexicon.py`'s existing six-mode dispatcher, keeps AC5's locus exactly and touches no guard.
That is not a listed option and cannot be ratified under M3. A third route also exists and nobody
listed it: `run_probe` in `lexicon.py`, as it stood at BASE, already implements S3's candidate computation and
S4's unruled tail with S4's own framing — but `TOOL-aSurfacedLexicon-3` deletes `run_probe` at build
order 1, five orders before this unit needs it, and neither spec cross-references the other.

AC5's staged break is wrong for either option and must be fixed before any observed-RED is run:
removing `if v in forms` from `{forms[v] for v in counts if v in forms}` raises `KeyError`, so the
arm would red by exception, certifying nothing. The break that actually grades the closure is
`forms.get(v, v)`.

**RESOLVED (agent, 2026-09-04, delegated): F2 — refuse to stamp on a dirty tree and say why, with
the dirty predicate NAMED as this repo's own tracked-only two-sided diff (`git diff --quiet` AND
`git diff --cached --quiet`), deliberately NOT `git status --porcelain`.**

The third option, drop the sha and keep the date, falls to veto 1: AC7 requires `expanded=` "written
with a date AND a sha", and it writes no sha. §3's non-goal is the honest case for it — if the
stamp's whole declared value is that a second expansion becomes a visible edit in a tracked file,
then a date alone makes it exactly as visible, and a date-only stamp also narrows §5's accepted
merge collision to one value per day. That is not enough: re-authoring an AC to rescue an option is
the owner's edit, not this adjudication's.

A fourth route was measured and rejected before it reached the ballot: stamping
`tools/run-gates/gate-fingerprint.sh`'s working-tree digest, which is well-defined on a dirty tree
and is already how `.githooks/pre-push` asks whether a recorded green still describes the commit it
names. It dies on veto 2 — a `tools/run-gates/` literal inside `tools/lexicon/` trips the
name-nothing-outside-itself ban, needing a carried-prefix registry row — and on `.lexicon.conf`'s own
LAYERS reasoning that the kit must ship self-contained.

That leaves refuse-on-dirty and stamp-HEAD-with-a-dirty-marker, and the refusal is the richer
survivor. It satisfies AC7 in full — date, sha, LF, and the second-run refusal — and it is the only
survivor that keeps S5's justification intact, because a clean tree's worktree IS its HEAD tree, so
the sha honestly names the tree the candidate set was measured against. The dirty-marked HEAD sha
names a tree the measurement did not read and cannot be re-derived from, so it satisfies AC7's
letter while forcing §4's reproducibility rationale to be rewritten — strictly more follow-ups, for
the same criteria.

WHICH DIRTY PREDICATE IS CHOSEN DECIDES WHETHER AC7 IS OBSERVABLE AT ALL, and neither §8 nor the
measurement pass named one. In a fixture-shaped repo `git status --porcelain` is NON-EMPTY forever,
because the kit is copied in untracked by design, so a `--porcelain` refusal can never be exercised;
the two-sided tracked-only diff reads CLEAN there, stamps date and sha, and AC7 runs end to end.
This repo already owns that definition and wrote down why, at `tools/govkit/govkit.py:4008
dirty_claimed_paths`. The fixture also needs one added line: the bespoke scaffold fixture does `git
init` + `git add` and stops, so there is no HEAD and no sha to write. Committing the already-staged
files does not contaminate the corpus — the comment at `selftest.py:95-99` warns against staging
`-A`, not against committing — and with an untracked `kit/` present `git ls-files` still returns the
fixture sources alone.

Residuals. A whole-tree refusal blocks the operator exactly when they have done the work the design
asks for, since §3 has them pasting proposals by hand and S7 has them re-pasting pins into the same
`.lexicon.conf` the candidate set reads; path-scoping the refusal to the files the measurement
actually read is the govkit-shaped mitigation, and nothing today enforces the one-run ordering that
makes a clean start possible. The sha also widens §5's accepted merge collision. And AC7's surviving
clause across every option — "the file keeps LF endings" — is the one with a reproduced failure
behind it: a CRLF conf INVERTS the unratified-seed refusal, so the stamp write must not be the edit
that reintroduces CRLF.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The candidate set was measured on this worktree and came back
  EMPTY, which moved the acceptance criteria onto a synthetic fixture and added the non-emptiness arm
  the research record's proposed check did not have. The anti-mirror closure's line number was
  corrected from 143 to 146 against source.
- rev-2 · 2026-09-04 · cross-spec audit: AC8 asserted `grep -c CANON tools/lexicon/scaffold_lexicon.py`
  equal to 0 and that command returns 1 on this tree, which contradicted
  `TOOL-aSurfacedLexicon-11`'s own AC8 and F1. AC8 and the §3 non-goal now defer to that unit's
  narrowed predicate rather than restating a count this tree refutes.
- rev-3 · 2026-09-04 · F1 PARKED, not resolved, so this unit is NOT built by this run and the status
  header stays SPECCED. Option B fails AC5 as written, which names `scaffold_lexicon.py:146` by path
  and is this unit's only observed-RED criterion; option A, as §8 names it, reverses the flag-arity
  guard at `scaffold_lexicon.py:98`, whose documented purpose is keeping a flag from becoming the write
  destination, and that is a widening past §5's "writes at most one scalar". Only vetoed options stand,
  so there is no resolver to delegate. Folded for the owner turn: the guard cite corrected from
  `:100-104` to `:98`, and the "computing candidates in `lexicon.py` would CREATE the
  two-readers-of-one-fact class" claim struck — `lexicon.py` already holds a second reader in
  `run_probe`, which `TOOL-aSurfacedLexicon-3` deletes at build order 1. AC5's staged break rewritten:
  deleting the cluster filter raises `KeyError` and would red by exception, so the break that grades
  the closure is `forms.get(v, v)`, and the criterion now cites the expression rather than a line
  number unit 3 will move. F2 ratified as refuse-on-dirty, with the dirty predicate NAMED in §4 and in
  AC7 as the tracked-only two-sided diff and explicitly not `git status --porcelain`, which is
  permanently non-empty in a kit fixture and would leave AC7 unobservable forever; AC7 also gains the
  fixture commit without which there is no HEAD and no sha to write. §5 records F2's two residuals. S7
  and §4's Migration paragraph now name the three `*_OFFENDER_PIN` scalars the conf carries at this
  unit's order instead of a `PINS:` block that arrives with `TOOL-aSurfacedLexicon-12` at order 7, and
  say plainly that this unit does not move. §10 records the probe-blindness finding behind its own "no
  seam fits" conclusion. Base re-pinned from `d0a18683` to `6c670b02`, and the §4 unruled-tail figure
  re-measured there at 267, replacing a stale 258.
- rev-4 · 2026-09-05 · two line citations into `tools/lexicon/lexicon.py` symbol-anchored, for the reason the
  order-1 sibling records — the build rewrites that file and the `spec tokens` leg caught the drift.
- rev-5 · 2026-09-06 · F1 RESOLVED by the owner and the unit BUILT, twelve units after the rest of
  this build landed. The ruling is the route the park had measured and could not ratify: an
  importable `derive_candidates` beside the closure, reached from the engine's dispatcher, with the
  scaffold's flag-arity guard untouched because the module is imported rather than invoked. Every
  line citation in this spec is STALE by construction — the twelve landed units moved all of them —
  so the numbers are STRUCK AND NOT REPLACED, and the expressions are cited instead. The first cut of
  this entry replaced them with re-measured numbers and the round-2 review caught it: five of the six
  were measured at the PRE-BUILD tree and were stale in the very commit that shipped them, moved by
  this unit's own insertions above them. Cite `live = {forms[v] for v in counts if v in forms}`,
  `if len(argv) != 2 or argv[1].startswith("-")`, `# PROPOSED from the SHIPPED CANON`,
  `already exists — refusing to overwrite`, and `read_conf_scalar ratified`. The one figure that
  holds is `.lexicon.conf:113` for `ratified`, whose VALUE also changed. §4's three `--probe` citations are struck outright: that mode was
  deleted at build order 1, so every figure resting on it is unreproducible rather than merely
  stale. S7 is re-authored — it named three pin scalars where the conf carries two, `LAYER_OFFENDER_PIN`
  no longer exists, and the `PINS:` block it insisted could not exist at this order does exist,
  because unit 12 landed. The output names no pin at all now and points at `--measure`, which is the
  same rule that removed the figures. S4's tail is taken from the engine's own `unruled`
  classification rather than a second predicate in the scaffold.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "propose additional declaration rows once from the frozen
canon without mirroring the corpus"` and a second run at `"scaffold seed candidate selection from live
canon clusters"` both returned no seam for this behaviour. The ranked candidates are
`load_corpus` and `seed_affordances`, both in `tools/codebase-map/reuse_lookup.py`, plus
`classify_row [tools/govkit/govkit.py]`, none of which selects declaration candidates. No existing
seam fits in the map's index — and the evidence for why is that the behaviour lives inside
`scaffold_lexicon.main()`, a `fan-in 0` entry point the map does not surface as a seam, rather than in
a named helper. That is itself the finding: the closure this unit depends on is one line inside a
141-line `main` (lines 87 to 227, measured by an AST span at writing time), so the unit's first job is
to give it a caller other than `main` without moving the expression. The seam this unit extends is
therefore the closure expression in `tools/lexicon/scaffold_lexicon.py`,
plus `canon.build_form_index` at `tools/lexicon/canon.py:84-95`, which the earlier probe for
`TOOL-aSurfacedLexicon-7` returned as a `fan-in 3 | SEAM`.

**This audit's conclusion is corrected at rev-3, and the correction is a finding about the probe.** The
ranking above has drifted — re-running the query puts `corpus_files [tools/memory-recall/extract.py |
fan-in 2]` on top and `seed_affordances` no longer appears — and "no seam fits" is true of the MAP but
false of the TREE. `python tools/codebase-map/reuse_lookup.py "run_probe"` returns `run_probe` at
fan-in 0, and `run_probe` in `tools/lexicon/lexicon.py`, as it stood at BASE, is the closest existing
implementation of S3 and S4 that exists anywhere in this repo. The semantic query could not
STRUCTURALLY have returned it: a zero-fan-in entry point is not ranked as a seam, so an audit that gets
"no seam" back over one is reporting the index's shape rather than the tree's. Read that as
probe blindness, not as an absence of prior art — and note that `TOOL-aSurfacedLexicon-3` deletes
`run_probe` at build order 1, five orders before this unit would want it.

Recall terms used: `python tools/memory-recall/query.py "what stops an expansion of the verb table
legalising the corpus's own commonest spellings" --terms "lexicon expand scaffold canon cluster live
site anti-mirror proposal unruled tail stamp expanded once"` — 40 hits, the binding one being
`TOOL-dScaffoldedMirror-8`, which records that the corpus votes to EXCLUDE and never to select and
that the dominance-table alternative was refuted.
