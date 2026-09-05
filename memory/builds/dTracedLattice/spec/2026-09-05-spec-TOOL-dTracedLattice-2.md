# TOOL-dTracedLattice-2 — the freshness gate announces a tier it did not compare

**Status:** SPECCED · rev-4 · 2026-09-05 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md) | research | TOOL-dTracedLattice-1 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round1.md) | spec-audit | TOOL-dTracedLattice-1 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |
| [2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-dTracedLattice-1-spec-audit-round2.md) | spec-audit | TOOL-dTracedLattice-1 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5 |

<!-- /gen:spec-records -->

## 1. Goal

`test_generated_artifacts_are_fresh` compares `symbols.json` only when the extracted symbol
population is non-empty, and says nothing when it is empty. A gate that passes while comparing
nothing is indistinguishable from a gate that compared and agreed.

## 2. Scope (IN)

- **S1** The symbol tier announces itself when it does not run, naming the tier and the reason, per
  `AGENTS.md` §7's rule that a skip must announce itself.
- **S2** The announcement is a REFUSAL rather than a note when the committed artifact EXISTS and the
  live population is empty, because that pairing means the extractor went dark under a committed file
  it can no longer justify.
- **S3** Every other conditional tier in the same function gets the same treatment, found by reading
  the function rather than by fixing the one instance — the class, not the instance.
- **S4** The gate's own header states what it does not check, per `AGENTS.md` §7.
- **S5** `tools/codebase-map/test_codebase_map.template.py` is an explicit write target. It is
  byte-identical to the installed gate today and no leg compares the pair, so editing one without the
  other ships a divergence silently.

## 3. Non-goals (OUT)

- No change to what freshness MEANS, to the byte-compare, or to the artifacts compared.
- No change to `map_extractors.py`; an empty population is a legitimate state for an adopter and this
  unit makes it loud, not illegal.
- Not the adopter-side staleness of the gate file itself — `TOOL-dTracedLattice-4` owns that.

## 4. Design

### Data model

The freshness map is built tier by tier. Each tier becomes an explicit record carrying its name,
whether it ran, and why not when it did not. The reporter walks every record, so a tier cannot be
absent from the output by being absent from the map.

### Alternatives rejected

Asserting the population is non-empty unconditionally. That reds every adopter whose project layer
declares no symbol extractor, which is a legal configuration the kit ships support for.

### Rollout

S1 and S3 together, since S3 is what makes S1 a class fix. S2 after, because it changes an exit code
and needs its failing case observed on a fixture that has a committed artifact and no live population.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — no new scan; the change is reporting.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the empty population IS the state this unit is about.
- observability — the skip line is the deliverable.
- risks — S2 turns a silent pass into a failure, so an adopter mid-migration could red. That is the
  intent, and the message must name the repair.
- testing + left-shift gates — a staged-break arm that observes the skip, and a second that observes
  S2's refusal, both RED before the fix.
- migration / rollback — revert restores silence.
- user docs — the gate header, per S4.

## 6. Acceptance criteria

- **AC1** — When the symbol population is empty and no committed `symbols.json` exists, the gate
  passes and its output names the symbol tier as `skipped` with the reason.
- **AC2** — When the symbol population is empty and a committed `symbols.json` DOES exist, the gate
  FAILS naming the tier, and this arm is observed RED before the fix lands.
- **AC3** — When `tools/codebase-map/test_codebase_map.py` is read, its header states which staleness
  classes it does not detect.
- **AC4** — When a tier is ADDED to `test_generated_artifacts_are_fresh` with a conditional
  population, it reports run-or-skipped without its author writing a reporting line, verified by an
  arm that introduces a second conditional tier in a fixture and asserts the output names it. The
  criterion is written this way deliberately: `test_codebase_map.py:141` is the ONLY conditional tier
  today, so an enumeration criterion would grade a population of one and could not fail.
- **AC5** — When `tools/codebase-map/test_codebase_map.py` and `test_codebase_map.template.py` are
  compared after this unit lands, they are byte-identical, asserted by a selftest arm — gov is not an
  adopter here, since its `GATE_FILE` points inside the kit directory.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map kit selftest` ·
`harness arms (fail branches armed or pinned)`.

Both `codebase-map kit selftest` and `codebase-map coverage + freshness` are kit-subject legs and are HELD on a plain bar; a builder verifying this unit needs `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. The runner names every held leg, so they are announced rather than silent.

## 8. Open questions

- **Q1 — does the template copy move too?** `test_codebase_map.template.py` is byte-identical to the
  installed gate today, and an adopter never re-copies it. Editing one and not the other ships a
  divergence. RESOLVED (agent, 2026-09-05, delegated): both files change in the same commit, and the
  general problem — that adopters never receive the update — is `TOOL-dTracedLattice-4` and not this
  unit.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the dTracedLattice skeptic round, which staged the break
  and observed the gate pass with the symbol tier absent.
- rev-4 · 2026-09-05 · moved to order 3; the owner's lexicon-rescue ruling inserted a unit ahead of
  the set and nothing else in this spec changed.
- rev-3 · 2026-09-05 · folded the round-2 spec audit: M1 (§7 discloses that the kit legs are held,
  which round 1's M2 asked for in every spec and rev-2 landed in unit 4 only).
- rev-2 · 2026-09-05 · folded the round-1 spec audit: H2 (AC4 graded a population of one and could not
  fail; restated as an added-tier criterion) and M1 (S5 and AC5 make the template twin a write target
  with an arm comparing the pair, which Q1 assumed and nothing enforced).

## 10. Reuse audit

No existing seam fits: the skip-announcement pattern has no shared implementation in this tree.
`python tools/codebase-map/reuse_lookup.py "a gate announces the tier it did not compare"` returns
`check` and `cmd_check` variants ranked by a fan-in this build has separately measured at 7.2%
precision in that band, and none of them is a reporting seam. The evidence that nothing fits is that
the tiers are local variables inside one function, so the change is confined to
`tools/codebase-map/test_codebase_map.py` and its template twin.

Recall terms used: freshness gate byte-compare skip announce liveness tier symbols.json extractor
population adopter selftest arm staged red
