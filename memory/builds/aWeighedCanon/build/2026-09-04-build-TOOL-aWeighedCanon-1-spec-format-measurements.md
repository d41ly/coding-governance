# What the spec corpus measures about the format that produced it

**Serves:** none — this is the measurement half of a research build that precedes any spec. The
findings half is a sibling record; anything either recommends becomes its own unit in its own build.

Taken 2026-09-04 on node `a`, at base `6c670b02`, over all 479 spec files under
`memory/builds/*/spec/**`. Every figure below is derived by a script, none is authored. The three
scripts are reproduced at the end so the numbers can be re-derived rather than trusted.

## The population

| | |
|---|---|
| Spec files | 479 |
| Total bytes | 8,430,496 |
| Median spec | 14,570 B |
| Mean spec | 17,600 B |
| Builds holding at least one spec | 89 |
| Status spread | 414 CLOSED · 24 SPECCED · 20 WONTDO · 9 DEFERRED · 6 INPROGRESS · 1 OPEN · 5 unparseable |
| Section canon | 436 carry ten numbered sections · 18 carry nine · 15 carry seven · 5 carry none |

The five with no parseable status header are all legitimately grandfathered — two are dated before
`SPEC_FORMAT_CUTOFF` (2026-07-15) and three carry no filename date at all, so check 5's recording
name does not select them. This was checked rather than assumed, and it is a clean negative result:
the grandfathering works as documented.

## 1. Right-first-time is rare, and rarer under the heavier profile

| Population | n | at rev-1 | mean rev | max rev |
|---|---|---|---|---|
| All parseable | 474 | 12.0% | 3.51 | 13 |
| Tier-1, light profile | 117 | 27.4% | 2.52 | 6 |
| Tier-2, full ten-section canon | 357 | 7.0% | 3.83 | 13 |

Nine specs in ten need at least one revision. Under the full canon it is more than nine in ten.

**This does not by itself indict the format**, and the report's findings half must not let it. Two
readings fit: the heavier profile attracts the harder problems, which would make the churn a
property of the work; or the heavier profile costs more to get right, which would make it a property
of the format. The tier split cannot separate them, because tier is assigned by risk and risk
correlates with difficulty. What follows is the part that *can* be separated.

## 2. The largest single driver of spec growth is the spec's account of its own growth

Median section bytes, bucketed by the spec's rev high-water. `growth` is the rev-6+ median over the
rev-1 median.

| Section | rev-1 | rev-2 | rev-3/4 | rev-5 | rev-6+ | growth |
|---|---|---|---|---|---|---|
| 1 Goal | 348 | 364 | 380 | 489 | 450 | 1.3x |
| 2 Scope | 923 | 1,261 | 2,037 | 3,158 | 4,821 | 5.2x |
| 3 Non-goals | 578 | 714 | 756 | 811 | 1,173 | 2.0x |
| 4 Design | 1,408 | 2,722 | 2,905 | 3,256 | 5,178 | 3.7x |
| 5 Production-readiness | 945 | 1,020 | 1,098 | 1,168 | 1,485 | 1.6x |
| 6 Acceptance | 788 | 1,303 | 1,618 | 2,121 | 3,540 | 4.5x |
| 7 Gates | 192 | 239 | 271 | 396 | 517 | 2.7x |
| 8 Open questions | 247 | 482 | 782 | 964 | 1,703 | 6.9x |
| **9 Revision log** | **190** | **722** | **1,341** | **2,729** | **4,866** | **25.6x** |
| 10 Reuse audit | 725 | 892 | 1,006 | 1,071 | 1,189 | 1.6x |
| TOTAL | 6,345 | 9,720 | 12,194 | 16,163 | 24,922 | 3.9x |
| n | 57 | 102 | 213 | 39 | 63 | |

Share of the rev-1 → rev-6+ median growth, by section:

| Section | added | share of growth |
|---|---|---|
| 9 Revision log | +4,676 B | 25.2% |
| 2 Scope | +3,897 B | 21.0% |
| 4 Design | +3,769 B | 20.3% |
| 6 Acceptance | +2,751 B | 14.8% |
| 8 Open questions | +1,456 B | 7.8% |
| 3 Non-goals | +595 B | 3.2% |
| 5 Production-readiness | +540 B | 2.9% |
| 10 Reuse audit | +464 B | 2.5% |
| 7 Gates | +325 B | 1.7% |
| 1 Goal | +102 B | 0.5% |

Section 9 as a share of the whole document, by bucket: 3.0% at rev-1 · 7.4% at rev-2 · 11.0% at
rev-3/4 · 16.9% at rev-5 · **19.5% at rev-6+**.

> **SUPERSEDED IN PART — read this before using the 25.2% figure.** The share-of-growth column
> above is CROSS-SECTIONAL: it compares different specs sitting at different rev bands, not one spec
> over time. The findings record measured the same thing by replaying git history over all 411
> multi-commit specs and got **§9 at 33.5% of growth against §4's 15.9%**. That is the stronger
> instrument and its numbers supersede this table's. Both agree on direction and on §9 being the
> largest single sink; only the replay carries the argument. The table stays because the per-section
> shape is still informative and because the weaker method should be visible next to the number that
> replaced it.

**A mature spec is one fifth changelog.** Section 9 grows 25.6x while the mechanism the builder
needs — section 4 — grows 3.7x, and section 9 contributes more of the total growth than section 4
does. The template's stated justification for the log is that "§9 is the rev high-water a resumed
session reads", which is a real need; but a high-water is one number, and what the corpus carries is
a full narrative history that every later reader pays for on every read.

The rest of the growth pattern is healthier and worth stating so the finding is not overread.
Section 1 is nearly flat at 1.3x, which is exactly right — a goal that keeps being rewritten would
be the alarming result. Sections 5 and 10 are near-flat at 1.6x, so the mandated sweeps are written
once and left alone. Sections 2, 4 and 6 growing together is what genuine design refinement looks
like.

## 3. Where a spec's mass actually sits

Per-section mass across all 479 specs. `N/A` counts sections opening with the sanctioned
`N/A — <why>` form; `<200B` counts near-empty bodies.

| § | Section | present | median B | % of all section mass | N/A | <200B |
|---|---|---|---|---|---|---|
| 1 | Goal | 474 | 390 | 3.1% | 0 | 19 |
| 2 | Scope (IN) | 471 | 1,921 | 16.8% | 0 | 3 |
| 3 | Non-goals (OUT) | 471 | 773 | 5.6% | 0 | 7 |
| 4 | Design | 458 | 2,930 | 25.5% | 0 | 0 |
| 5 | Production-readiness | 453 | 1,145 | 7.5% | 2 | 4 |
| 6 | Acceptance criteria | 471 | 1,632 | 13.2% | 0 | 2 |
| 7 | Gates | 469 | 285 | 2.9% | 0 | 167 |
| 8 | Open questions | 474 | 820 | 6.6% | 0 | 98 |
| 9 | Revision log | 472 | 1,281 | 12.8% | 0 | 30 |
| 10 | Reuse audit | 439 | 994 | 6.1% | 0 | 12 |

Three things fall out.

**Section 4 is a quarter of the document.** The mechanism a builder needs to build from is 25.5% of
the mass; 74.5% is everything else. That is not automatically wrong — scope and acceptance are how a
builder knows when to stop — but it bounds how much of the format's cost is buying build guidance.

**Section 7 is near-vestigial as written.** 167 of 469 gate sections (36%) are under 200 bytes, with
a 285-byte median, and the section carries 2.9% of total mass. In practice it names one gate command
and stops. It is not clear the section earns a heading rather than a header field.

**Section 8 is `none` about a fifth of the time.** 98 of 474 (21%) are under 200 bytes. That is the
honest and correct outcome for a spec with no forks, and it is worth noting only because it means
the section's real cost is concentrated in the specs that do have forks.

## 4. Section 5 mostly earns its place — against expectation

The production-readiness checklist mandates ten cross-cutting lines. Across the corpus its bullets
number 4,107, of which 1,105 carry `N/A` — **26.9%**.

This was measured expecting a much higher number, on the theory that a mandated ten-line sweep over
a tooling repo would be overwhelmingly inapplicable. It is not. Roughly three bullets in four say
something. The section is doing work, and any proposal to trim it should be argued on other grounds.

## 5. One advisory rule is dead letter

The writing rules require: *"Verify every claim about existing code against source at writing time;
mark the rest `UNVERIFIED`."*

`UNVERIFIED` appears 35 times, in **17 of 479 specs — 3.5%**.

Either authors verify essentially every claim they write about existing code, across 8.4 MB of
specs; or the marker is not being used. The corpus itself settles which: the 52 `spec-audit` review
records exist precisely because specs assert things about code that turn out to be wrong, and
`TOOL-aBoundedVerdict-32` records a case where a spec's own acceptance criterion was false on the
day it was written. The rule is stated, unenforced, and unused. It is exactly the shape the charter
names as its own recurring failure: a rule that is a documented check nobody performs reads as
coverage.

## 6. The builder's read cost, per build

A builder does not read one spec. It reads its build's whole set.

| | |
|---|---|
| Builds with specs | 89 |
| Median build's spec set | 61,908 B (~15K tokens) |
| Largest | 476,860 B (~119K tokens), `aBoundedVerdict`, 16 units |
| Builds exceeding 200 KB of spec | 14 of 89 |

| Build | units | bytes | ~tokens |
|---|---|---|---|
| aBoundedVerdict | 16 | 476,860 | 119,215 |
| aMendedLedger | 8 | 392,657 | 98,164 |
| dCarriedReceipt | 15 | 365,634 | 91,408 |
| aPacedTurnstile | 8 | 334,233 | 83,558 |
| dRetiredFork | 30 | 323,583 | 80,895 |
| dUnstalledConvoy | 24 | 317,149 | 79,287 |

At the top of that distribution the spec set alone is a substantial fraction of a context window
before any source file is opened. This is the problem `TOOL-aStagedLane-3` on the
`spec-writing-harness` branch is aimed at from the writing side — per-slice briefs so each writer
holds only its own unit. The same measurement says the READING side has the same problem and no
equivalent mitigation.

## 7. What the format does well, measured

Two results run against the direction of the rest of this record, and are reported because a
research pass that only finds faults has selected for them.

**Acceptance ledgers are real coverage.** Of 154 CLOSED Tier-2 unit ids dated on or after
`ACCEPTANCE_LEDGER_CUTOFF` (2026-08-20), **147 — 95.5% — are evidenced by a journal-kind record**.
Check 22 is doing what it claims. The seven unevidenced ids were not investigated further: the bar
is green, so the gate's own cutoff logic evidently covers them in a way this crude re-derivation
does not model, and reporting them as defects would be asserting a conclusion from a predicate
weaker than the gate's.

That figure is stated only after a first attempt got it wrong. Selecting ledgers by the filename
substring `acceptance-ledger` returned 11 builds apparently owing a ledger and carrying none — a
false positive, because ledgers are also named `-acceptance.md`. The correct population is the
journal-kind `**Serves:**` records, which is the gate's own selector. Recorded here because it is a
live instance of `vacuous-selector-empty-population` caught inside the very pass that measures such
things, and because the wrong number was persuasive.

**Section 1 does not churn.** 1.3x growth from rev-1 to rev-6+ across 474 specs. Whatever else
revision does to these documents, it is not relitigating what the unit is for.

## 8. A defect in the template's own prose

`memory/TEMPLATE-SPEC.md:16` states that `SPEC10_CUTOFF` is *"DECLARED in `.memory-tree.conf`
beside the three other cutoffs and shipped at `2026-08-04`."*

Both halves of that sentence are wrong about the tree as it stands.

- `.memory-tree.conf` declares **six** cutoffs, not three: `SPEC_FORMAT_CUTOFF`, `STREAMS_CUTOFF`,
  `REVIEW_VERDICT_CUTOFF`, `FORK_MARK_CUTOFF`, `SPEC_WITNESS_CUTOFF`, `ACCEPTANCE_LEDGER_CUTOFF`.
- `SPEC10_CUTOFF` is **not among them**. It is declared in the checker, at
  `tools/memory-tree/check-memory-hygiene.sh:42`, and reaches a blank conf by the forward
  resolution at `:90`.

Nothing is broken — the value resolves to the documented `2026-08-04` either way. The defect is
that a reader following the template to the conf to find the knob finds nothing, and the count
beside it is stale. It is the charter's own rule broken by the document that teaches the format:
*a value stated in prose beside the source that owns it rots*, and *no count of a derived population
is written in prose*. Verified by `grep -nE '^[A-Z_]+CUTOFF=' .memory-tree.conf`.

## Reproducing these figures

Three stdlib-only scripts, written for this pass and not installed anywhere:

- `measure_specs.py` — the population, rev distribution by tier, size-by-rev buckets.
- `measure_sections.py` — per-section mass, `N/A` counts, the section-5 bullet split, `UNVERIFIED`.
- `measure_growth.py` — per-section median bytes bucketed by rev high-water, and growth shares.

They are throwaway measurement code, not a kit. If any figure here becomes load-bearing for a
later unit, that unit owes it a derived check rather than a citation of this record — which is the
same rule this record's own section 8 finding is about.
