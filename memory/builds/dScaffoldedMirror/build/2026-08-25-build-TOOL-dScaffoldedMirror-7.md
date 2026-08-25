# TOOL-dScaffoldedMirror-7 — build record

**Serves:** journal TOOL-dScaffoldedMirror-7

Node `d`, 2026-08-25, base `500a5db6`, unattended run `dScaffoldedMirror`. Spec:
`../spec/2026-08-24-spec-dScaffoldedMirror-7.md`, built at rev-4. The first standing measurement of
the thing this kit is for.

## Result

`build_lexicon_marginal_offense_rate` derives offenders-added per definition-added between the commit
that adopted `.lexicon.conf` and HEAD, both operands produced by the lexicon's own `extract_text` at
both shas, through one batched `git cat-file --batch` per sha.

| scope | definitions added | offenders | rate |
|---|---|---|---|
| all armed files | 243 | 50 | 20.9% |
| files written FRESH in the window | 117 | 5 | **4.3%** |
| files that predate the declaration | 126 | 45 | 36.9% |

**The 4.3% is reading ONE of the two that abandon the pressure chain.** The docstring carries the
rule: if the fresh-file rate stays at or below roughly 5% across two further readings,
`TOOL-dScaffoldedMirror-4`, `-9` and `-11`'s cut fourth pin should be abandoned rather than deferred.
A second reading is owed before anyone acts on it, and this record is the first.

## Four of the spec's own claims did not survive being built

Recorded here rather than only in the revision log, because the pattern is the finding: every one was
a statement about the tree that nobody had measured.

1. **rev-1's pin move rested on a false premise.** It asserted every signal leads with `signal_` and
   proposed raising `VERB_OFFENDER_PIN` 463 → 464 to fit. Two already lead with `build`, and
   `build_live_backlog_rows` carries an in-tree comment making exactly the argument rev-1 needed and
   did not find. Pin unchanged.
2. **rev-2's shallow-clone trigger is unreachable.** `git log --diff-filter=A` in a `--depth 1` clone
   does not fail — it returns the shallow ROOT as the adding commit and that sha resolves. Observed:
   derived base `37bfdd19` against a true adoption commit of `b0626152`. The liveness assertion was
   armed against a case it could never see, inside the field that exists to refuse exactly that.
3. **S7's cache was sized against a cost the implementation removed.** 0.957 s cold against the
   2.774 s per-file read it was priced for. Cut.
4. **AC7 required the one edit shape this repo forbids** — it demanded the word `unmeasurable`
   vanish, where the convention is to supersede by quoting the dead claim beside its supersession.

## And two gates caught earlier passes of this same run

The lexicon leg was red at 466 for two commits: three helpers led with `lex` and `pct`. Renamed to
`build`, `read` and `measure`; the pin never moved. The drift ratchet caught a `READ_PATH_CEILING`
raise whose justification was written but sat 16 lines above the key, outside the 14-line window —
so the ratchet correctly saw a raise with no reason. Both were caused by running memory-hygiene on a
pass and not the leg whose subject the pass had touched.

**Evidences:** TOOL-dScaffoldedMirror-7
- AC1 — `python tools/drift-audit/drift_report.py` — reports `lexicon_marginal_offense_rate` at 50 of 243, `gateable: False`, base `b0626152`, with both operands and the three-way split in `detail`
- AC2 — amended rev-3 — the trigger changed from an unresolvable base to a SHALLOW REPOSITORY, because the original case is unreachable (§4, §9 rev-3); the amended criterion was then observed in a `--depth 1` clone, `live: False`
- AC3 — `python tools/drift-audit/selftest.py` — `empty window: NOT ASKED rather than a rate of 0`, asserting `not_asked` rather than `value == 0`, and observed RED under a staged rate-of-0 break
- AC4 — `python tools/drift-audit/selftest.py` — `no .lexicon.conf: the rate is NOT ASKED, not a clean zero`
- AC5 — amended rev-4 — S7's cache was cut on a measurement, so the criterion re-points from the cache key to the property F2 resolved; armed as `admitting a verb lowers the rate` (§9 rev-4)
- AC6 — amended rev-2 — inverted from `VERB_OFFENDER_PIN` at 464 to 463 UNCHANGED, the pin move having rested on a false premise; observed by `python tools/lexicon/lexicon.py --measure` printing 463
- AC7 — amended rev-3 — reworded from an absence grep to a supersession assertion, because this repo supersedes by quoting (§9 rev-3); observed by `grep -c "dScaffoldedMirror-17"` returning non-zero on both carriers
- AC8 — `grep -c "pressure chain" tools/drift-audit/drift_report.py` — returns 1, so the kill-reading ships in the docstring rather than living only in a spec
