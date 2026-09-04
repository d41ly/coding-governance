---
slug: aWeighedCanon
node: a
opened: 2026-09-04
status: OPEN
streams: tooling
roster: TOOL
ids: TOOL-aWeighedCanon-1
---

# aWeighedCanon — is the spec format earning what it costs?

Node `a` · opened 2026-09-04 · streams tooling.

This build authors no product change. It carries ONE question, asked by the owner and answered from
this repo's own corpus: does `memory/TEMPLATE-SPEC.md` produce specs that help the builder session
which later has to build from them, and what is missing from it?

**Why it is a build folder and not a loose file.** The layout rule is that reports live under a
build's own folder. The report under `build/` is the deliverable; anything it recommends becomes
its own unit, with its own spec, in its own build.

**Scope, as ratified at kickoff.** Research only. No edit to `memory/TEMPLATE-SPEC.md`, to
`tools/memory-tree/SPEC-TEMPLATE.template.md`, or to check 12 of `check-memory-hygiene.sh`. No new
gate leg and no spec set. The owner decides from the report what becomes a build.

## Why the question is worth asking

The format is load-bearing twice over. Every build in this repo starts from a spec written to it,
and every repo adopting the memory-tree kit receives it as
`tools/memory-tree/SPEC-TEMPLATE.template.md`. It is graded by check 12, which is a STRUCTURAL
check: it grades whether the ten sections are present, ordered, non-empty and free of skeleton
placeholders. Nothing anywhere grades whether a conforming spec was any use to the agent that built
from it.

That gap is the build's subject. A format can be perfectly conformant and still fail its reader.

## The measurement that opened it

Taken 2026-09-04 at base `6c670b02`, over all 479 spec files under `memory/builds/*/spec/**`.
Reproduce with the script this build's report names.

| Population | n | at rev-1 | mean rev | max rev |
|---|---|---|---|---|
| All parseable specs | 474 | 12.0% | 3.51 | 13 |
| Tier-1 (light profile) | 117 | 27.4% | 2.52 | 6 |
| Tier-2 (full ten-section canon) | 357 | 7.0% | 3.83 | 13 |

Specs also GROW through revision. Median bytes by rev high-water: rev-1 7,724 · rev-2 11,684 ·
rev-3 13,119 · rev-4 15,375 · rev-5 19,938 · rev-6+ 29,968. A spec that reaches rev-6 is roughly
four times the size of one that never needed a second pass.

Two readings fit those numbers and the report's job is to separate them. Either the heavier format
attracts the harder problems, which would make the churn a property of the work; or the heavier
format costs more to get right, which would make it a property of the format. The tier split alone
cannot tell them apart.

## Method

Five disjoint evidence lenses over the corpus, then an adversarial verify pass, then synthesis.
The lenses were: the template's rules against what check 12 actually enforces; the 52 `spec-audit`
review records, as direct evidence of what the format lets authors get wrong; the 74 acceptance
ledgers, compared against the section 6 they answer; the builder-side `AMEND`/`RETIRE`/`SUPERSEDE`
acts, as evidence of what speccing could not see; and the cost of the ceremony itself.

Fan-out was bounded per `memory/guides/REVIEW-PROTOCOL.md` and the `agent-cap` hook: ten agents,
1.64M tokens, 422 tool calls, 23.5 minutes. 34 findings raised, **29 confirmed and 5 refuted —
precision 0.85**, against the charter's 0.5 retune threshold. Twenty-six of the 29 survivors were
narrowed by the skeptic that checked them, several with their headline numbers corrected downward.

## What the two records hold

- **`…-1-spec-format-measurements.md`** — the derived figures: population, rev distribution by tier,
  per-section mass, growth by section, the builder's per-build read cost, and two clean negative
  results. Carries one superseded table, marked in place.
- **`…-2-what-the-spec-format-is-missing.md`** — the findings, every one in its post-skeptic form,
  grouped into three themes, with what the format does well, what this pass could NOT determine, and
  a ranked build order for anything acted on.

## The answer in one paragraph

The format is a shape contract that is enforced hardest where specs least often fail. Its largest
gap is not a missing section: it is that the format specifies documents and never joins them — scope
to acceptance, criterion to ledger answer, unit to sibling, criterion to the failure that would turn
it red. Its largest cost is a revision loop that 88% of specs enter, that five builds independently
measured as the source of 60–89% of the next round's defects, and for which the template's entire
instruction is one clause. What it is NOT is expensive ceremony — that hypothesis was tested
directly and refuted.

## Ratified findings that touch other live work

`TOOL-aStagedLane-3` on the `spec-writing-harness` branch fans spec WRITING over per-unit briefs.
This build measured the same problem on the READING side — a median 61,908 bytes of spec per build,
476,860 at the top — which has no equivalent mitigation. The two are complementary, not overlapping.

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aWeighedCanon-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
