# Measuring unit 5's scanner before committing to it

**Serves:** research TOOL-aDeclaredBound-5

The round-1 spec audit named unit 5's gate as the build's largest unmeasured risk: nobody had
written the pattern, so its false-positive rate was unknown, and a rate high enough to make the
waiver registry a chore would be a reason to reconsider the whole unit. The owner asked for the
measurement before any build order was fixed. This is it, run at `5770f4a`.

## Three passes

| pass | scope | hits | true positives | false positives |
|---|---|---|---|---|
| 1 — first draft | every tracked file | 276 lines across 634 files | not classified | not classified |
| 2 — S6's frozen-tree exclusion | every tracked file outside `memory/{builds,archive,gotchas}/` | 55 | 17 | 30, about 64% |
| 3 — bound word required, markdown only | tracked `*.md` outside the frozen trees | **18** | **18** | **0** |

Pass 1 is reported only to show the exclusion is load-bearing: without S6 the frozen record trees
supply roughly four fifths of the matches, and every one of them is a description of what was true
when it was written.

## What the two tightenings are, and why neither is fitted to the data

**A bound word must be adjacent to the number.** `≤`, `<=`, `at most`, `never more than`, `no more
than`, `up to`, `maximum of`, `max of`, `capped at`, `only`. This is what separates an ASSERTION
from a MEASUREMENT, and the false positives it removed were all measurements: the review protocol's
own record of four runaway reviews at 79 / 54 / 48 / 37 agents, the drift-audit tier table's
"~22 agents" and "0 agents", and the same figures in the rendered skill. None of those becomes wrong
when the cap moves, because none of them claims to be the cap.

**Markdown only.** The remaining fifteen false positives were all code, in four recognisable classes:
test fixtures spelling a bounded call (`agent(g)), 5)`), the deliberate `AGENT_CAP=50` refusal
fixture, a version-matching regex (`agent-cap@$ac`), and the node registry row naming the machine
`agent-0`. The unit is about PROSE carriers of a governance rule. Scanning executable files buys
nothing here and costs a waiver row for each fixture that legitimately spells a bound.

## The residual risks, both real

**A false negative found during the measurement.** The first tightened pattern lost
`memory/guides/REVIEW-PROTOCOL.md:135` — `≤5 batched default-refute skeptics` — because "skeptics"
was not in the noun list. Two lines, both genuine carriers, silently missing. The noun list is a
LIST, and a carrier phrased outside it is invisible; the gate's header has to say that in the same
register `check-method-carriers.sh` says it about its own structural limit. This is the strongest
argument against relying on the gate alone and for S1's measure-first rule.

**The markdown-only decision has a live cost, and here it is.** `tools/workflows/tier2-review.js`
describes its own find phase twice and the two disagree: line 7 says `4 finder lenses, one wave, ≤5
concurrent` and line 128 says `ONE ≤6-wide wave`. The code fans at `cap = 5` and `MAX_VERIFIERS = 5`,
so the `≤6` is stale prose inside the harness the BINDING protocol points at. It predates this build.
A markdown-only gate cannot see it. Filed rather than fixed here, because fixing it inside a
measurement pass is how a scoped unit stops being scoped.

## What this does not measure

The pattern was run against THIS corpus. An adopter's prose will phrase the same rule differently,
and the noun list is gov's vocabulary. The gate ships with the kit, so its first run in an adopter
tree is the one that matters and nobody has made it. That is the same class as a pin copied from
another corpus, and the honest mitigation is the one S1 already carries: measure, then set.
