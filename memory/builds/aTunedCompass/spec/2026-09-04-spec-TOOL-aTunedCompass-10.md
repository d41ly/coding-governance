# TOOL-aTunedCompass-10 — the neighbour predicate selects a pool a cap can meaningfully bound

**Status:** SPECCED · rev-2 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make the reuse probe's neighbour arm select a pool small enough that a cap over it is a choice rather
than an accident. Today the `same kind` arm admits almost the whole symbol corpus, so
`TOOL-aTunedCompass-6`'s reordering changes which arbitrary names a reader gets without reducing how
many arbitrary names there are. This unit changes WHICH candidates are neighbours; unit 6 changes the
order they are ranked in. The two land in one pass.

## 2. Scope (IN)

- **S1** — the `same kind` arm in `tools/codebase-map/reuse_lookup.py` (`:237`) narrows. Measured on
  this corpus today: of 769 indexed symbols, 731 are kind `function`, so a seed of that kind admits
  95.1% of the corpus through this arm alone. A cap of 12 over a pool of 731 is not a selection.
- **S2** — the narrowing is `same kind AND same kit directory`, which the fork named and which this
  unit measured before adopting. The map's own symbol inventory groups as 156 symbols in the largest
  kit directory and roughly 100 to 150 in each of the next three, so the arm's reach falls by
  between five and seven times while staying non-empty for every kit that has one.
- **S3** — the `same file as a hit` arm at (`:235`) is UNCHANGED. It is checked first, it is already
  narrow, and it is the arm that produces the neighbours a reader actually uses.
- **S4** — the reason string each neighbour carries names the narrowed predicate, so a reader can see
  why a candidate is present. A predicate that changes while its printed reason does not is a gate
  lying quietly, which is the class this build's parent measured across three carriers.
- **S5** — arms in `tools/codebase-map/selftest.py` covering the narrowing in both directions: a
  same-kind, same-directory candidate is admitted, and a same-kind, different-directory candidate is
  refused. Each arm's red is observed before the arm is written.
- **S6** — the before-and-after is measured with the replay harness `TOOL-aTunedCompass-6` commits,
  over the same 133 graded probe phrases the parent report left behind, so the two units report on
  one instrument rather than two.

## 3. Non-goals (OUT)

- Not changing what a SEED is. The name-stem seed arm is untouched, and `TOOL-aWeighedCompass-14` on
  demoting it stays a backlog row with its own measurement to do first.
- Not changing what the symbol index ADMITS. Private symbols stay excluded and
  `TOOL-aWeighedCompass-13` stays a backlog row. This unit filters candidates that are already
  indexed; whether more should be indexed is a different question with a different cost.
- Not changing `NEIGHBOUR_CAP` itself. The cap's value only becomes a real question once the pool it
  bounds is meaningful, which is what this unit provides.
- Not reordering. That is `TOOL-aTunedCompass-6`, which this unit sequences immediately after.

## 4. Design

The arm is a two-line `elif` and the change is small; what needs care is the justification, because a
narrowing that is too aggressive silently removes the only useful candidate for some query and no
signal says so.

Same-kit-directory is the right axis for a reason particular to this corpus rather than a general
principle: this repo's product is a set of kits, each kit is a directory under the tool root, and the
reuse question a session asks is nearly always "does this behaviour already exist in the kit I am
about to edit, or in one I should be calling". A candidate in another kit is not useless, but it
reaches a reader better through the `same file` arm or through a shared-seam hit than through a kind
match that would have admitted 95% of everything.

The measured risk, stated rather than assumed away: a kit with few symbols yields a small neighbour
pool, and for a query seeded in such a kit the arm may return almost nothing. That is an improvement
over returning 12 alphabetically-first names from across the tree, but it must be VISIBLE, which is
what S4's reason string is for.

## 5. Production-readiness checklist

Observability: the reason string names the predicate, so a reader can tell a narrow pool from a
broken one. Testing: S5's two-direction arms, plus S6's corpus-level before-and-after. Migration:
none, the probe is stateless and rebuilt per run. Rollback: the arm is one condition and reverting is
one line. Cost: no measurable change to probe latency, which the parent measured at about 1.1s.

## 6. Acceptance criteria

1. `python tools/codebase-map/reuse_lookup.py "<a phrase seeded in one kit>"` returns no neighbour
   from another kit directory through the same-kind arm, verified by reading the printed reasons.
2. The narrowed arm is non-empty for a seed in each kit directory that has more than one symbol,
   checked by a loop over the kit dirs and recorded in the unit's journal.
3. `bash tools/codebase-map/selftest.py` or the kit's declared self-test entrypoint passes with S5's
   two new arms, and each arm was observed RED before it was written.
4. The replay harness from `TOOL-aTunedCompass-6` reports hit rate and median rank over the 133
   graded phrases before and after, and the record states both. A narrowing that lowers the hit rate
   is a finding to report, not a result to bury.
5. `python tools/codebase-map/gen_map.py --check` exits 0, and the `codebase-map` dossier under
   `memory/map/features/` is refreshed in the same commit, since this changes how the kit behaves.
6. `bash tools/check-kit-versions.sh` exits 0 with the codebase-map kit version moved.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `codebase-map coverage + freshness` and `kit version
markers` the legs that bind. The kit's own self-test is `subject = kit` and held by default, so S5's
arms need `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` and the record must say so.

## 8. Open questions

**F1 RESOLVED (agent, 2026-09-05, delegated): accept the empty pool, and let S4's reason string make it
legible.** Both alternatives are vetoed on the spec's own text rather than on preference. AC1 requires
that the same-kind arm return no neighbour from another kit directory; the unnarrowed fallback and the
widen-to-tool-root variant each return exactly that, in exactly the case they fire, so both fail an
acceptance criterion already written here. AC2 confirms the survivor was the shape this unit was
specced around — it asks for non-emptiness only where a kit directory holds more than one symbol,
which is the one-symbol case conceded. The fork's own argument stands unaltered: a fallback that
reinstates a 95%-of-corpus pool whenever the good predicate returns nothing makes the narrowing
untestable.

- **F1 — what happens to a seed in a kit directory with one symbol?** Its narrowed neighbour pool is
  empty, so the probe returns seeds and shared-seam hits only. Options: accept it, since an empty
  neighbour list is honest where the old one was noise; fall back to the unnarrowed arm when the
  narrowed one is empty, which restores the old behaviour exactly where it was least useful; or widen
  the axis to the tool root when a kit is below a size threshold.
  Recommendation: accept it, and let S4's reason string make the emptiness legible. A fallback that
  reinstates a 95%-of-corpus pool whenever the good predicate returns nothing is the shape that makes
  a narrowing untestable. Left open because it is a real behaviour change for small kits and the
  owner may prefer the fallback.

## 9. Revision log

- rev-1 · 2026-09-05 · first draft. Added by the restructure recorded in the build README: the owner
  chose to narrow the predicate rather than ship unit 6's reorder alone, then chose to split the
  narrowing into its own unit so M2's one-mechanism rule holds.
- rev-2 · 2026-09-05 · F1 resolved under the standing mandate, M3's rule. Both fallback options fail
  AC1, which forbids a cross-kit neighbour through this arm, so only the fork's recommendation
  survived the first veto. No scope, acceptance or gate text moved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "which candidates count as a neighbour of a seed symbol"`
returned `render_symbols_json` and `python_symbols` in `tools/codebase-map/map_lib.py` and
`seed_affordances` in `tools/codebase-map/reuse_lookup.py`. None is the seam: the first two build the
index and the third seeds affordances, while the arm this unit changes is the inline `elif` in
`shortlist`. The probe demonstrated its own subject — the candidates it returned were selected by the
name stem `symbol`, and the function actually being changed was not among them. The seam was found by
reading `reuse_lookup.py` around the neighbour construction, which is recorded here rather than
claimed as a probe hit.

Recall terms used: reuse_lookup neighbour predicate seed same-kind cap alphabetical fan-in shortlist
codebase-map symbol corpus precision
