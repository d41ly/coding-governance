# TOOL-aSurfacedLexicon-10 — `--expand`, the one-time widening the canon bounds

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

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
  table already declares. Liveness is decided by the expression at
  `tools/lexicon/scaffold_lexicon.py:146`, `live = {forms[v] for v in counts if v in forms}`, which is
  READ and not edited. A token in no cluster cannot enter a proposal, and that closure is the reason
  this unit is safe to build at all.
- **S4** — The unruled tail prints BELOW the proposals, under a header stating in words that these are
  not proposals and that a row here would be the mirror defect the kit was rebuilt to close. It is
  evidence for an owner, never a candidate.
- **S5** — `--expand --stamp` writes `expanded="<iso-date> <sha>"` into the conf, the sha naming the
  tree the candidate set was measured against.
- **S6** — A selftest arm asserts the candidate set is a SUBSET of the canon representatives, run
  against a synthetic fixture repo whose `VERBS` table is deliberately short. This arm is the whole
  point of the unit: it is what stops an adopter legalising its own existing mess.
- **S7** — The output tells the operator that expansion moves pins and that the `PINS:` block must be
  re-measured and re-pasted, so an expansion cannot land without its cost showing in the diff.

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
representatives with at least one site in the corpus, from the untouched expression at
`tools/lexicon/scaffold_lexicon.py:146`. `declared` is the keys of the conf's `VERBS` table. The
candidate set is `live - declared`, and `candidates ⊆ reps` holds by construction because `live ⊆ reps`
by the definition of `forms`.

The unruled tail is a different computation entirely and must never be joined to the candidate set: it
is the leading tokens with a live site that are in no cluster AND in no `VERBS` row, printed with
their counts.

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

Measured by a scratchpad script over `lexicon.tracked_files(root)`, importing `canon.CLUSTERS`,
`canon.build_form_index` and the conf's `VERBS` through `lexicon_conf.load_conf`:

| Fact | Value |
|---|---|
| Canon clusters | 20 |
| Clusters with a live site here | 20 |
| Representatives already declared | 20 |
| Candidate set on this tree | 0 |
| Declared rows outside the canon | 3 |
| Distinct unruled tokens in the tail | 258 |

The unruled tail's top rows here are `a` at 18 sites, `git` at 13, `demand` at 10, `signal` at 8,
`bounded` at 7 and `kit` at 7. Those are the names S4's header exists to keep out of the proposal
list, and their presence at the top of the tail is what makes the header a live warning rather than a
decoration.

**A correction to the research record, verified against source at writing time.** That record cites
the anti-mirror closure at `tools/lexicon/scaffold_lexicon.py:143`. At `cd8ab0d2` line 143 is
`suffix_offenders = _measure_suffix_offenders(root, files)` and the closure is at line 146. The
expression is byte-identical to the one the record quotes; only the line moved. Cite 146.

**A second measured absence.** `.lexicon.conf` carries no `expanded=` key today and no
`canon_unfrozen=` key either; the only stamp in the file is `ratified="2026-08-24 node d"` at line 183.
So S2's guard also has an empty population on this tree and its refusal cannot be observed here
without a fixture conf. Both arms of this unit are fixture-only, and the spec says so rather than
letting a green selftest imply otherwise.

### Migration

`TOOL-aSurfacedLexicon-12`'s conf rewrite introduces the `expanded=""` key. Until it lands, an absent
key reads as empty and `--expand` proceeds, which is the correct reading of "never expanded". The
guard must distinguish absent from empty only in its message, not in its verdict.

### Rollout

`--expand` is additive: an adopter who never runs it sees no change, and `--scaffold`, `--check` and
`--render` keep their behaviour byte for byte. The mode allowlist edit at
`tools/lexicon/adopt-lexicon.sh:184` is the only change to an existing code path.

### Files touched (estimate)

`tools/lexicon/adopt-lexicon.sh` (the mode, the guard, the stamp write),
`tools/lexicon/scaffold_lexicon.py` (a second entry point for the candidate computation, reusing line
146's expression), `tools/lexicon/selftest.py` (the fixture and its two arms), and
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
  away.
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
- **AC5** — When `tools/lexicon/scaffold_lexicon.py:146` is staged with the cluster filter removed, so
  that `live` admits a token in no cluster, the subset arm in `tools/lexicon/selftest.py` goes RED;
  unstaging returns it to green. The RED is observed before this unit is called done, and it is the
  only proof that the arm grades the closure rather than the fixture.
- **AC6** — When `bash tools/lexicon/adopt-lexicon.sh --expand` runs on THIS repo unmodified, it
  proposes nothing and says so in words, naming that all 20 canon clusters are already declared. The
  empty case is asserted as a message, not as silence.
- **AC7** — When `--expand --stamp` runs on the fixture, `expanded=` is written with a date and a sha,
  the file keeps LF endings, and a second `--expand` on the result hits AC1's refusal.
- **AC8** — When `python tools/lexicon/lexicon.py` runs after this unit lands,
  `TOOL-aSurfacedLexicon-11`'s structural guard against a `CANON:` header emitted by
  `tools/lexicon/scaffold_lexicon.py` is still green, so this unit has not opened the path by which the
  mirror returns through the proposal body. The predicate is that unit's NARROWED one, matching only an
  emitted block header. It is NOT `grep -c CANON tools/lexicon/scaffold_lexicon.py` equal to 0: that
  command returns **1** on this worktree, matching the descriptive comment at
  `tools/lexicon/scaffold_lexicon.py:181`, so the research record's bare-grep form would red the tree it
  ships against. Re-measured for this spec; `TOOL-aSurfacedLexicon-11`'s AC8 and F1 own the predicate.

## 7. Gates

`lexicon wiring` (guard `[]`, ceiling 330) runs `adopt-lexicon.sh --check` on every bar and must stay
green across the mode-allowlist edit. `lexicon selftest` (chunk `selftests`, subject `kit`, ceiling
880) carries the fixture and both arms, and it is invisible to the push boundary unless
`GATE_SELFTESTS=1` is set, which no boundary sets — so the subset assertion is on-demand coverage and
this spec states that rather than implying a push-time guarantee. `lexicon naming predicates` (chunk
`declarations`, ceiling 300) must stay green: this unit moves no pin. `memory-tree hygiene` grades this
spec. No new leg, so no new ceiling and no `testsuite-count-waivers.txt` row is owed.

## 8. Open questions

- **F1 — Where does the candidate computation live?**
  `tools/lexicon/scaffold_lexicon.py:100-104` refuses any flag with the message that the script takes
  one conf PATH and has no options of its own, so a second mode there means reversing a deliberate
  refusal. The alternative is computing candidates in `tools/lexicon/lexicon.py` and leaving the
  scaffold untouched, which duplicates the `live` expression and creates the two-readers-of-one-fact
  class the research record already counts three instances of in this kit. Recommendation: a second
  entry point in `scaffold_lexicon.py` — an importable function the shell calls through a mode flag —
  so line 146 keeps exactly one reader. Reversing that refusal is cheap and duplicating the closure is
  not.

- **F2 — What sha does `--stamp` write when the worktree is dirty?**
  The design's justification for the sha is reproducibility: it names the tree the candidate set was
  measured against. A dirty worktree has no such sha, and `HEAD` names a tree the measurement did not
  read. Options are refusing to stamp on a dirty tree, stamping `HEAD` with a dirty marker, or dropping
  the sha and keeping the date. Recommendation: refuse on a dirty tree and say why. A stamp that names
  a tree the run did not measure is worse than no sha, and expansion is a once-per-project action where
  demanding a clean tree costs an operator nothing.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The candidate set was measured on this worktree and came back
  EMPTY, which moved the acceptance criteria onto a synthetic fixture and added the non-emptiness arm
  the research record's proposed check did not have. The anti-mirror closure's line number was
  corrected from 143 to 146 against source.
- rev-2 · 2026-09-04 · cross-spec audit: AC8 asserted `grep -c CANON tools/lexicon/scaffold_lexicon.py`
  equal to 0 and that command returns 1 on this tree, which contradicted
  `TOOL-aSurfacedLexicon-11`'s own AC8 and F1. AC8 and the §3 non-goal now defer to that unit's
  narrowed predicate rather than restating a count this tree refutes.

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
therefore `tools/lexicon/scaffold_lexicon.py:146` by path,
plus `canon.build_form_index` at `tools/lexicon/canon.py:84-95`, which the earlier probe for
`TOOL-aSurfacedLexicon-7` returned as a `fan-in 3 | SEAM`.

Recall terms used: `python tools/memory-recall/query.py "what stops an expansion of the verb table
legalising the corpus's own commonest spellings" --terms "lexicon expand scaffold canon cluster live
site anti-mirror proposal unruled tail stamp expanded once"` — 40 hits, the binding one being
`TOOL-dScaffoldedMirror-8`, which records that the corpus votes to EXCLUDE and never to select and
that the dominance-table alternative was refuted.
