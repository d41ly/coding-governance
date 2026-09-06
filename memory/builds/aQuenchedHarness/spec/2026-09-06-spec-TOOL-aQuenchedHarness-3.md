# TOOL-aQuenchedHarness-3 — a self-test never reaches an adopter, as a leg or as a file

**Status:** OPEN · rev-2 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-5 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |

<!-- /gen:spec-records -->

## 1. Goal

Stop shipping this repo's kit self-tests into adopter repositories. Thirty `[[gate_leg]]` rows across
the kit descriptors name a `*.test.sh`, a `test_*.py` or a `--selftest` verb, and `govkit`'s emit
copies them into a target's `gate-legs.json` — while `chunk`, half of the predicate that HOLDS them
here, reaches no adopter manifest. An adopter therefore runs suites that grade kit source they never
edit, on every bar.

## 2. Scope (IN)

- **S1** — at EMIT time, `govkit` drops a descriptor `[[gate_leg]]` row whose gov-manifest twin
  satisfies the runner's own hold predicate, `subject == kit OR chunk == selftests`. The decision is
  made in gov, where BOTH fields exist, and the row simply never leaves. `chunk` therefore never has
  to travel and no predicate is derived from a filename.
- **S2** — the join is the one already built. `tools/govkit/govkit.py` constructs `manifest_subject`
  and `manifest_chunk` by leg NAME at `:1500-1508`, and already REFUSES a descriptor leg that is in
  no row of `tools/gate-legs.json`. S1 reads those two maps; it does not add a reader, a key or a
  second spelling of the predicate.
- **S3** — the self-test FILES stop shipping too. Each kit descriptor's file claims drop that kit's
  `*.test.sh`, `test_*.py`, `selftest.py` and their fixtures, and the descriptor records that they
  are gov-internal, with the public repository named as where to read them.
- **S4** — the emit REPORTS what it dropped, per target: every leg by name and every file by path. An
  emit that silently ships less is indistinguishable from an emit that failed, and a drop count of
  zero is printed as a zero rather than as silence.
- **S5** — a gate leg asserting BOTH directions over a freshly emitted fixture manifest: no emitted
  leg satisfies the hold predicate against gov's manifest, and no emitted file claim names a
  self-test file. The second direction is what stops a filter that matches nothing from reporting
  clean.
- **S6** — `tools/run-gates/run-gates.sh` is NOT touched. The local hold predicate, the set of legs it
  holds, and `GATE_SELFTESTS` are all exactly as they are today.
- **S7** — arms staging: a descriptor leg whose twin is `subject = kit`, one whose twin is
  `chunk = selftests`, one whose twin is neither, a descriptor file claim naming a `.test.sh`, and an
  emitted manifest hand-edited to contain a self-test leg.

## 3. Non-goals (OUT)

- Not adding `chunk` to the descriptor schema. `TOOL-aScouredKit-27` records why that is a
  five-declaration act against a PINNED key set the `run-gates canary` asserts, and warns that
  half-building it is worse than the gap. S1 makes it unnecessary rather than doing it.
- Not deriving anything from a filename. Rev-1 did, and the audit measured the cost: that predicate
  selects 53 of 94 legs and four of them are `subject = repo, chunk = declarations` on purpose —
  `kit/dogfood doc parity`, `review-protocol parity (kit vs dogfood)`, `codebase-map coverage +
  freshness` and `marker contracts`. The third is a leg `AGENTS.md` §5 and §7 forbid exempting.
- Not changing which legs run in THIS repo. S6 states it and AC5 measures it as an EQUALITY.
- Not the on-demand runner, which is `TOOL-aQuenchedHarness-4`.
- Not removing an adopter's ability to obtain the suites. They are in the public repository and S3
  records where; what stops is the automatic copy and the bar leg.

## 4. Design

### Data model

No new key anywhere, and — after rev-2 — no new predicate either. The fields that decide are
`subject` and `chunk`, both already in `tools/gate-legs.json`, both already read by `govkit` at emit
time through a name join it already performs. The change is a filter over a mapping that exists.

Rev-1 placed the predicate "beside the manifest reader that both consumers already share". The audit
opened both readers: `run-gates.sh` parses the manifest in a python heredoc and holds in BASH at
`:947`; `govkit.py` does its own `json.loads` at `:1360` and `:1497`. There is no shared reader and
this unit no longer needs one, because only ONE consumer changes.

### Rollout

An adopter's next `govkit` emit produces a manifest with fewer rows and a file set with fewer files.
Nothing in their tree breaks: the removed legs graded files they do not edit, and files already on
disk are not deleted by an emit. S4's report is how they see it rather than discovering it from a
shorter bar.

### Inventory

- `no self-test reaches an adopter` — the new gate leg's name in `tools/gate-legs.json`.
- The drop report's two counts, printed per target by the emit.

### Files touched (estimate)

`tools/govkit/govkit.py` · every `tools/*/kit.toml` carrying a self-test file claim ·
`tools/gate-legs.json` · `tools/govkit/selftest.py` · `WIRE-INTO-PROJECT.md`.

### Alternatives rejected

**A filename-derived predicate** — rev-1's design — was rejected by measurement, not by taste: run
over `tools/gate-legs.json` at HEAD it selects 53 legs and holds four repository checks off every
bar, one of them a leg the charter forbids exempting. It also re-decides by filename the population
`tools/run-gates/run-gates.sh:875-885` records as decided by what a FAILURE MEANS, which
`TOOL-dUnstalledConvoy-30` says "decided four legs wrongly" the last time it was tried.

**Emitting `chunk` into a target's manifest** was rejected on `TOOL-aScouredKit-27`'s own warning, as
in §3.

**Shipping the files while dropping the legs** — rev-1's F1 answer — was rejected once
`TOOL-aQuenchedHarness-5` needed a shared harness: a suite that ships while the library it sources
does not is a file that breaks on first invocation in an adopter tree, which
`tools/run-gates/kit.toml`'s header records this repo already doing once.

## 5. Production-readiness checklist

- security — an adopter receiving fewer executable legs and fewer executable files is a narrowing.
  No new path executes anything new.
- perf / scale — two dictionary lookups per descriptor leg at emit time.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a descriptor leg with no manifest twin already refuses; a drop of
  zero legs is printed as zero; an emit whose manifest is unreadable fails rather than shipping
  everything.
- observability — S4's per-target report, both counts and both name lists.
- risks — the predicate is now the manifest's own two fields, so a false positive requires a leg to
  be MIS-DECLARED in `tools/gate-legs.json`, which the `run-gates canary` and `govkit selfcheck`
  already grade. The residual risk is a leg correctly held here that an adopter genuinely wants; S3
  names where to get it.
- testing + left-shift gates — S7's arms, each observed RED before landing, plus S5's both-direction
  leg.
- migration / rollback — reverting the filter restores today's emit. No adopter state is written that
  needs undoing.
- user docs — `WIRE-INTO-PROJECT.md` gains one sentence saying adopters receive neither the self-test
  legs nor the self-test files, and where the files live.

## 6. Acceptance criteria

- **AC1** — When `govkit` emits a manifest for a fixture target, no emitted row's gov-manifest twin
  satisfies `subject == kit OR chunk == selftests`, and the emit prints the names it dropped.
- **AC2** — When the `no self-test reaches an adopter` leg runs against a hand-edited emitted manifest
  carrying a held leg's name, it reds.
- **AC3** — When an emitted file claim names a `*.test.sh`, the same leg reds — the second direction,
  so a filter matching nothing cannot report clean.
- **AC4** — When the filter is made vacuous, the arm in `tools/govkit/selftest.py` reds, so a
  selector that drops nothing is caught rather than reported green.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs without `GATE_SELFTESTS`, the set of legs it
  holds is EQUAL to today's set, compared name-for-name against a set captured before the change.
  Equality, not superset: a superset assertion cannot see a leg wrongly added to the hold.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `no self-test reaches an adopter` leg ·
`govkit selfcheck`, which carries no guard and runs on every bar · `govkit acceptance matrix` and
`govkit refusal join`, which run when their `tools/govkit/` guard fires, as this unit's edits make it
· `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for `govkit selftest` and the
`run-gates canary` at the Definition of Done.

## 8. Open questions

- **F1 — the owner's own either/or.** The prompt says self-checks must "NOT ship to the repo adopters
  (or ship strictly OPT-IN and do not execute on a full bar by default)". RESOLVED (agent,
  2026-09-06, delegated), REVISED at rev-2: take the FIRST clause. Neither the legs nor the files
  ship. Rev-1 took a middle position — files ship, legs do not — and the audit showed it creates a
  suite that sources a library an adopter's tree cannot contain. The owner's own sentence gives the
  reason to prefer the simple half: "adopters do not need to modify this kit, so self-checks are not
  required there." Fewest follow-ups open, no acceptance criterion lost.
- **F2 — does a kit descriptor need a way to mark a file gov-internal?** RESOLVED (agent, 2026-09-06,
  delegated): no new marker. S3 removes the claim, and a file a descriptor does not claim is a file
  the emit does not copy — which is the existing contract, used as it stands.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.
- rev-2 · 2026-09-06 · folded spec-audit round 1. B1: the filename predicate is GONE — it selected 53
  of 94 legs and held four `subject = repo` checks off every bar, including one the charter forbids
  exempting; the emit now filters on the manifest's own `subject`/`chunk` through the name join
  `govkit.py:1500-1508` already builds. B6: §4 and §10 no longer claim a shared manifest reader,
  because there is none and only one consumer now changes. B3, inherited from unit 5: F1 re-decided
  so the files stop shipping too, which removes the broken-source failure entirely. U1: §7 no longer
  says `govkit acceptance matrix` runs on every bar — it carries a four-path guard. AC5 changed from
  superset to EQUALITY.

## 10. Reuse audit

The seam is `tools/govkit/govkit.py`'s existing emit path and the leg-name join it already performs
at `:1497-1510`, where `manifest_subject` and `manifest_chunk` are built and a descriptor leg absent
from `tools/gate-legs.json` is already refused. This unit adds a filter over maps that exist; it
introduces no reader, no key and no second spelling of the hold predicate.
`tools/codebase-map/reuse_lookup.py` returned `registry.toml` [govkit] and
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seams. The prior record that
scopes the gap is `TOOL-aScouredKit-27`, read in full, and its warning is why the descriptor-key
route is a rejected alternative rather than the design. `TOOL-dUnstalledConvoy-30`, surfaced by the
audit, is why the filename route is now rejected as well: it records that asking what a leg TESTS
"decided four legs wrongly", and the same four are the ones rev-1's predicate would have taken.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
