# DEPL-cMendedVintage-20 — a retired flag's absence is graded under every spelling it has

**Status:** CLOSED · rev-2 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-20-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-20-acceptance-ledger.md) | journal | — |
| [2026-09-17-prompt-DEPL-cMendedVintage-20-2-build-brief.md](../prompts/2026-09-17-prompt-DEPL-cMendedVintage-20-2-build-brief.md) | journal | — |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-cMendedVintage-4` AC3 grades the retirement of `--allow-ungraded` with
`grep -c 'allow_ungraded' tools/govkit/govkit.py` returning 0. Measured in this worktree at that
spec's pinned blob, that pattern returns 8 while `grep -cE 'allow[_-]ungraded|ALLOW_UNGRADED'`
returns 14: it is blind to the USAGE line, the USAGE sentence, the `over` clause, the argv arm and
the `parse_args` unpack — the last being the very site AC3's own Red-when calls the likeliest miss.
Grade the absence from a source-level class arm that reads every spelling, so the observation does not
depend on a criterion's pattern being written correctly.

## 2. Scope (IN)

- **S1** `tools/govkit/selftest.py` gains a class arm that reads a DECLARED list of retired flag names
  and, for each, asserts zero occurrences in `tools/govkit/govkit.py` under a pattern covering the
  underscore spelling, the hyphen spelling and the upper-case constant spelling of the same name.
  The module it reads is a PARAMETER defaulting to the derived path, so the failing case is staged
  against a scratch copy and the tracked file is never edited to observe a red (rev-2).
  Observed by AC1 and AC2.
- **S2** The retired list lives in `tools/govkit/selftest.py` beside the arm as one literal per retired
  flag, seeded with `allow-ungraded` and carrying the date and the unit id that retired each.
  A retirement with no row is a retirement nothing grades. Observed by AC3.
- **S3** The arm's population is the whole operator-facing surface of that module — the USAGE block,
  every string literal, every identifier — and never a section of it. A pattern scoped to argv parsing
  is the same blindness one level in. Observed by AC1.
- **S4** The arm names, in its own header, what it does NOT check: it reads one module, it cannot see a
  flag re-introduced in `selftest.py` or in a sibling tool, and it grades spelling rather than
  behaviour. Observed by AC4.

## 3. Non-goals (OUT)

- No spec-lint join. Teaching `tools/check-spec-tokens.py` to run a criterion's literal `grep` and
  compare its figure was the review's own left-shift and it is refused here for scope: it grades
  specs, it would red every existing criterion whose figure is stale rather than wrong, and it does
  not make the six blind occurrences observable by anything. It is recorded as the follow-up.
- No widening of `DEPL-cMendedVintage-4` AC3 in this unit. That criterion stays as its author wrote
  it; this unit adds the observation that does not depend on it, which is what promoting the finding
  buys over folding it.
- No general "no dead flag" scanner over every tool in this repo. The declared list is govkit's, the
  arm reads govkit, and a scanner over a population nobody declared is the shape that gets widened
  until it grades nothing.
- No behavioural assertion. Whether the flag still WORKS is `DEPL-cMendedVintage-4` AC2's argv
  refusal; this arm grades whether its name survives anywhere an operator can read it.

### Edges

- **consumes-from** `DEPL-cMendedVintage-4` — that unit performs the retirement this arm grades.
  Before it lands the arm is red by construction, which is why this unit is sequenced after it.
- **hands-off** external — nothing else in this build reads the retired list.

## 4. Design

### The measurement, and what it says about the criterion

Both figures below were derived in this worktree against the blob the spec audit pinned, and both are
re-derivable by the arm rather than trusted from here.

| pattern | matching lines |
|---|---|
| `allow_ungraded` | 8 |
| `allow[_-]ungraded` or `ALLOW_UNGRADED` | 14 |

AMENDED AT REV-2: the unit is MATCHING LINES and not occurrences. Both figures came from `grep -c`,
which counts lines, and rev-1 wrote them down as occurrences. They differ here: one line reads
`allow_ungraded=ALLOW_UNGRADED` and carries the name twice, so the widened pattern has 15
occurrences on those 14 lines. The arm counts lines, which is the unit the criterion it grades was
measured in, and prints the offending lines beside the count so a red names the survivor.

The six the criterion cannot see are the two USAGE carriers, the `over … --allow-ungraded` clause in
the withheld-stamp message, the argv arm's `elif`, and the `parse_args` unpack's upper-case constant.
Five of those six are operator-facing strings, which is the half of the retirement an operator would
actually notice surviving.

### Why the arm reads a declared list rather than one hard-coded name

An arm asserting one literal absence is the instance fix: it certifies `allow-ungraded` and says
nothing about the next flag this engine retires. The list in S2 is what makes the next retirement cost
one row instead of one arm, and it is why each row carries the retiring unit id — a row with no
provenance is indistinguishable from a name somebody typed in.

### The pattern, spelled once

```
allow[_-]ungraded   case-folded
```

AMENDED AT REV-2. The pattern was spelled as two alternatives joined, `allow[_-]ungraded` beside
`ALLOW_UNGRADED`; it is now ONE alternation matched case-insensitively, which is a superset of that
pair and of every mixed-case spelling between them. Measured both ways against the blob this build
bases on: 14 matching lines either way, so the widening costs nothing here and removes the second
pattern that would have had to be kept in step with the first. Derived from the flag name by the
arm — the separators become a character class and case stops mattering — so a new row supplies a
name and never a regex. A row whose name needs a hand-written pattern is a name this engine does not
spell the way it spells the others, and that is worth a refusal naming the row rather than a special
case; the arm makes no absence assertion for a row it refused, because a green there is a skip
wearing coverage's clothes.

### Inventory

| identifier | cell | what it is |
|---|---|---|
| `RETIRED_FLAGS` | ungraded | the declared list, one row per retired flag with its date and unit id |
| `check_retired_flags` | `py.function` | the arm |

`check_retired_flags` leads with `check`, which is the verb this file's sibling arms already spell for
an assertion loop. Asked about the committed name, `lexicon.py --suggest` answers `OK`.

AMENDED AT REV-2: rev-1 gave the constant's cell as `py.const` at `UPPER`, and there is no such cell.
Measured — the tool answers that `py.const` is malformed because the closed surface set is
`function type file constant`, and that `py.constant` is UNDECLARED because the declared cells are
`js.function py.function py.type sh.function`. Module constants in this corpus are graded by nothing,
so the spelling is a convention this file follows rather than a rule anything enforces, and claiming
otherwise would have been a second answer to a question the declaration already owns.

### Migration

None. The arm is new, the list is new, and no shipped artifact changes shape.

### Rollout

Lands directly and is red until `DEPL-cMendedVintage-4` lands, which is the sequencing in §3 Edges and
not a defect. There is no flag: an arm gated dark is an arm nobody runs.

### Alternatives rejected

- **Widen `DEPL-cMendedVintage-4` AC3's pattern and stop there.** That is the fold, and M4 refuses it
  for a HIGH. It also leaves the class open: the next criterion written as a narrow literal `grep` has
  the same defect and nothing reports it.
- **Assert the two USAGE strings by content.** The instance fix one level down — it grades the two
  copies that exist today and is silent on the third.
- **Run the grep in `tools/check-spec-tokens.py` at lint time.** §3 records why: it grades the spec
  rather than the source, and the source is where the six occurrences are.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/selftest.py` | the declared list, the arm, and the header stating what it does not check |

## 5. Production-readiness checklist

- security — the arm reads one tracked file and writes nothing.
- perf / scale — one read of the module it is handed and one regex pass per declared row.
- error / empty / loading states — an empty declared list is a DEAD PROBE and reds by that fact rather
  than reporting a clean pass over nothing; a row whose name contains a character the derived pattern
  cannot express reds naming the row.
- observability — one line per declared row carrying the name, the derived pattern and the count, all
  DERIVED, so a red names the spelling that survived rather than only the flag.
- risks — the arm grades spelling and not behaviour, which is stated in its own header per S4 so the
  green row is never read as "the flag is gone from the product". Second: a declared list is a second
  place a retirement must be recorded, and a retirement that skips it is ungraded — which is why S2
  puts the retiring unit id in the row and §3 refuses to derive the list from anything.
- testing — AC1 through AC4, each a direct observation against this repo's own tree. Unlike most of
  this build, none of them needs a scratch install.
- migration — none.
- user docs — none. The arm is internal to the kit's own suite and ships no operator-facing surface.

## 6. Acceptance criteria

- **AC1** — When the `check_retired_flags` arm runs after `DEPL-cMendedVintage-4` has landed, it
  reports 0 matching lines for `allow-ungraded`, and re-adding one `ALLOW_UNGRADED` occurrence turns
  it RED naming the line that occurrence sits on.
  AMENDED AT REV-2: the re-introduction is staged on a COPY under the run's scratch root, never on
  the tracked module. The arm takes its target as a parameter for exactly this, and a checker that
  can only read one hard-coded path has no negative case anything can reach.
  Red when: the pattern is written as the underscore spelling alone, which is the shipped criterion's
  defect reproduced in the arm that was built to close it.
  figure: DERIVED — the count comes from the arm's own pass over the file it is handed, never from a
  number written in this spec.
- **AC2** — When `check_retired_flags` runs against the tree at this build's BASE, it reports 14
  matching lines and is RED.
  AMENDED AT REV-2: rev-1 said "14 occurrences". The figure is a LINE count — see the §4 table — and
  the same pattern has 15 occurrences on those 14 lines.
  Red when: the arm's pattern cannot see the upper-case constant, in which case it reports 8 at BASE
  and the six blind sites are still blind.
  figure: DERIVED by the arm at observation time; 14 is the count measured in this worktree at the
  blob `DEPL-cMendedVintage-4` was audited at, and the arm re-derives it rather than trusting it.
- **AC3** — When the declared list `RETIRED_FLAGS` is read, its `allow-ungraded` row carries a date
  and `DEPL-cMendedVintage-4` as the unit that retired it.
  Red when: the list holds bare names, so a later reader cannot tell a retirement from a typo and the
  row is deleted to clear a red.
- **AC4** — When the `check_retired_flags` header is read, it names the one module the arm reads and
  states that it grades spelling and not behaviour.
  Red when: the header is written as a description of what the arm catches, which reads as a semantic
  check to everybody who did not write it.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · the retired-flag class arm, staged by re-adding one
`ALLOW_UNGRADED` occurrence to a COPY of the engine under the run's scratch root · no assertion floor
to move.

AMENDED AT REV-2, the other half of AC1's amendment: rev-1 staged the break in the tracked engine,
which this unit does not write and which the pass after it reviews. The break goes on a copy, which
is what the arm's path parameter is for.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-17 · S1 and AC1: the arm's target module is a PARAMETER defaulting to the derived
  path, and the re-introduction is staged on a copy under the scratch root. The tracked module is not
  in this unit's write set, `DEPL-cMendedVintage-19` landed in it minutes before this pass, and a
  re-introduced flag left behind would surface in the closing review; the parameter also gives the
  checker the negative case a one-path checker cannot have.
- rev-2 · 2026-09-17 · §4 and AC2: the unit of both figures is MATCHING LINES, not occurrences. Both
  came from `grep -c`, which counts lines; measured here, the widened pattern has 15 occurrences on
  14 lines because `allow_ungraded=ALLOW_UNGRADED` carries the name twice. The arm counts lines, the
  unit the criterion it grades was measured in.
- rev-2 · 2026-09-17 · §4: the pattern is one case-folded alternation rather than two spellings
  joined. Measured 14 either way at BASE, so it is a superset at no cost, and there is no second
  pattern to keep in step with the first.
- rev-2 · 2026-09-17 · §7 and §5, the halves AC1's amendment left standing: §7 still staged the break
  in the tracked engine and §5 still named it as the one file read. Both now say the copy and the
  handed module. Caught by the `amendment-leaves-its-other-half-standing` class.
- rev-2 · 2026-09-17 · §4 Inventory: rev-1 claimed `.lexicon.conf` declares `py.const` at `UPPER`. It
  declares no such cell — measured, the surface set is `function type file constant` and the declared
  cells are `js.function py.function py.type sh.function` — so module constants here are graded by
  nothing and the row now says so.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "restore a snapshot entry whose kit key no rollback loop
selects"` was this promoted set's probe and returned no seam; its ranked rows are name-token
neighbours on `kit` and `key` and it named `.sh` as an unscanned layer, so nothing it returned is
reachable from a suite arm. The seam this unit extends was read from source instead, and it is
`DEPL-cMendedVintage-4` S4's own class arm: that unit already establishes the shape of a source-level
assertion over `tools/govkit/govkit.py`'s string literals, with a staged break, so this unit adds a
second predicate to an established arm style rather than a mechanism. `tools/govkit/selftest.py:8126`
is the prose-grep that unit replaces, and reading it is what shows the instance-versus-class defect
this arm is the class side of. The recall probe returned `DEPL-cMendedVintage-4`'s own brief and the
`DEPL-dCarriedReceipt-13` round-1 diff review, neither of which considered a flag surviving in an
upper-case constant.

Recall terms used: `--terms "govkit rollback snapshot attributes receipt row kit orphan restore
touched_kits claimed verify outcome regenerate"`, with the question "what decided how govkit rollback
selects snapshot entries by kit and what owns the synthetic attributes row".
