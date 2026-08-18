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

## CORRECTION — this record did not contain the pattern it reported

Round 2 of the spec audit found that no pattern stated here reproduces the headline figure, and
re-running it confirms that. The correction is appended rather than folded into the text above,
because the text above is what was reported to the owner and what the numbers were claimed from.

**The noun list was load-bearing and is absent.** The section "What the two tightenings are" names
two constraints — a bound word, and markdown only — and calls them the whole tightening. They are
not. The run that produced 18 also required the match to be followed by a fan-out NOUN, from a list
of nine (`agents`, `verifiers`, `lens`/`lenses`, `skeptics`, `concurrent`, `per verify stage`,
`are verify-stage`, `ever run`, `batched`). Re-measured at the commit this correction lands on:

| pattern | lines | files |
|---|---|---|
| bound word only, as this record states it | 54 | 23 |
| bound word AND the noun list, as it was actually run | 19 | 11 |

Neither is 18 across ten. The 18 was true of the tree at `5770f4a` under the unwritten pattern; the
figure moved because this build has since added records that themselves state bounds, which is a
property of the corpus rather than of the scanner.

**Two arithmetic faults in the pass table.** Pass 2 reads `55 hits, 17 true positives, 30 false
positives`, and 17 plus 30 is 47. The missing 8 are the two copies of `agent-cap.js`, which the
prose classified as SOURCE and the table silently dropped. The stated rate "about 64%" is therefore
30/47 and not 30/55. And pass 3 reports 18 true positives where pass 2 reports 17, while being a
strict narrowing of pass 2 in both scope and pattern — a subset cannot contain more. The 17 was a
hand count and it was wrong.

**A consequence for the spec, not just for this record.** `skills/session-kickoff/SKILL.md:47` reads
`report ≤5 lines` and MATCHES the bound-word-only pattern. Unit 5's AC2 names that exact line as the
gate's green control. Against the pattern this record documents, that control fails; against the
pattern actually run, it passes. An acceptance criterion cannot be graded on an undocumented
predicate, which is why round 2 called this a blocker rather than a tidy-up.

**What is not withdrawn.** The finding that the frozen-tree exclusion is load-bearing stands, and so
does the direction of the tightening: requiring a bound word does separate an assertion from a
measurement, and every false positive it removed was a measurement. What is withdrawn is the claim
that this record contains enough to reproduce any of it.

**A third fault, in the evidence for the markdown-only decision.** The enumeration above lists
"the node registry row naming the machine `agent-0`" among the fifteen false positives that
markdown-only removed. It cannot have removed it: the surviving carrier is `AGENTS.md:63`, which
is markdown and stays in the pass-3 population; the only other live matches were two archive
ledger files already excluded a pass earlier by the frozen-tree rule. That enumeration is the
only itemised evidence offered for a decision the spec calls measured rather than guessed, so
the class list needs re-deriving before it can carry that weight.

## Addendum — what committing before running §7 cost

Unit 5 was committed without running the gates its own §7 names. Four legs went red on the next
full bar, and three of them were unit 5's:

- **govkit selfcheck / selftest.** A new gate leg is not just a row in `tools/gate-legs.json` — the
  govkit registry grades the tracked SURFACE, so two legs and a waiver registry arrived claimed by
  no descriptor. Fixed with `tools/govkit/entries/check-agent-cap-restatement.kit.toml` and its
  registry row; the surface reads `0 unclaimed` again.
- **drift-audit records.** `handkept_inventories_disagreeing_with_source` fired: `AGENTS.md`'s
  gate-suite section named 70 legs against a manifest of 72. A gate that nothing in the charter
  describes is coverage a session obeying the charter under-reports.

The fourth was unit 3's `_lookback_of`, whose leading token is not in the declared VERBS table.
Renamed `_read_lookback` rather than bumping the pin — the standing rule from `TOOL-aLoosenedCeiling`
is that a pin bumped to fit a name is the ratchet going slack by one every time someone is in a
hurry.

**The charter bullet then tripped the gate it was describing.** The first draft quoted both carriers
the pattern had missed, verbatim and with their digits, inside the very section that bans a bare
fan-out number in live prose. That is the best evidence this build has that the gate fires on real
prose written by someone who knows the rule: it caught its own documentation on the first run. The
bullet now names them by noun and says so.

**One prose defect ran through three carriers.** The gate's header, the protocol-parity test's
header and the gate's own FAILURE MESSAGE all asserted the bound is "DECLARED and adjustable per
repo". Unit 4 is parked; `tools/hooks/agent-cap.js` still carries `const CAP = 5` as a bare literal,
so all three described a channel that does not exist. Nothing gates a comment against reality —
`non_terminal_specs_cited_by_product_source` caught two of the three only because they happened to
cite the spec id, and the remedy string, which is what a reader actually sees when the gate reds,
carried no id and would have survived.

