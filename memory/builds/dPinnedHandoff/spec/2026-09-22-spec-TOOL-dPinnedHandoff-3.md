# TOOL-dPinnedHandoff-3 — an acceptance grep runs, and cannot already hold at the spec's base

**Status:** SPECCED · rev-1 · 2026-09-22 · node d · Tier-2 · base 9b7e2de6 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The NicoCares email-header brief states its invariants as greps: a string, a scope with an exclusion,
and an expected count, which is zero hits of the retired header under the frontend source. This repo's
acceptance witness rule grades only that a criterion NAMES something. `TOOL-aHonedRuleset-12` records
the cost: criteria whose own grep could not fail, found by hand across two audit rounds. This unit
adds an `Invariant:` line a criterion may carry, and an eighth `tools/check-spec-tokens.py` join that
runs it twice. At the spec's `base` the line must NOT hold, or it observes nothing the unit changes.
At the commit that closes the unit, it must hold.

## 2. Scope (IN)

- S1. The grammar, written into the template's `## 6. Acceptance criteria` guidance. The template
  source is `tools/memory-tree/SPEC-TEMPLATE.template.md`, rendered to `memory/TEMPLATE-SPEC.md`. One
  line inside an acceptance bullet reads `Invariant:`, then a backticked fixed string, then ` · `,
  then one or more backticked git pathspecs separated by spaces, then ` · `, then a non-negative
  integer, and optionally ` · kept`. The line does not wrap. Observed by AC7.
- S2. `extract_invariants` and the `INVARIANT_LINE` pattern in `tools/check-spec-tokens.py` parse
  every such line inside the acceptance section, found by heading text. A line opening with
  `Invariant:` that does not parse is a `malformed` hit, not a skip. Observed by AC1 and AC4.
- S3. `measure_invariant` counts matching lines at a commit: the sum over
  `git grep -c -F -e <string> <sha> -- <pathspecs>`. Exit 1 reads as zero. Any other non-zero exit is
  a `grep failed` hit naming the line, because an erroring grep is not a count of zero. Observed by
  AC5.
- S4. The base arm, graded on every live spec. At `base`, a plain invariant that already holds is a
  `holds at base` hit. A `kept` invariant that does NOT hold at base is a `not kept at base` hit,
  because it claims a state the tree does not have. Observed by AC1 and AC2.
- S5. The close arm, graded on every CLOSED spec carrying an invariant. At the commit
  `derive_closing_commit` returns, an invariant of either form that does not hold is a
  `fails at close <sha8>` hit. A WONTDO spec is not graded, because it built nothing. Observed by AC3.
- S6. A canary, `INVARIANT_CANARY`, parsed and measured on every run against a string this checker's
  own source carries. A canary that yields no parse, or a zero where its count is known, reds as a
  dead arm. Observed by AC6.
- S7. A report line prints on every run: invariants examined, live specs carrying one, hits per arm,
  terminal specs graded. `--list` prints each live invariant's count at HEAD as progress, and counts
  acceptance bullets quoting a `grep` invocation as near-misses, meaning candidates to convert.
  Observed by AC6.
- S8. The dossier `memory/map/features/spec-tokens.md` counts this join in its `title` and join list.
  Observed by AC8.
- S9. The memory-tree kit's one version move for the build, from 2.85 to 2.86: `KIT_MEMORY_TREE_VERSION`
  in `tools/memory-tree/check-memory-hygiene.sh`, the marker in each `tools/memory-tree/*.template.md`,
  and the four rendered copies. The move changes `memory/guides/BUILD-METHOD.md`, which the kickoff
  manifest watches, so the manifest is re-stamped in the same commit. Observed by AC9.
- S10. The dry run. Before the join is wired, it prints how many acceptance bullets across the
  corpus quote a `grep` invocation, split live and terminal. That is the near-miss population. The
  output is recorded in this build folder. Observed by AC10.
- S11. The arms of AC1 to AC6 are added to the spec-tokens self-test. NOT OBSERVED as a suite,
  because a suite run is not an acceptance observation from `SPEC_DIRECT_CUTOFF` onward; §7 names the
  suite under `New arm:`.

## 3. Non-goals (OUT)

- Regex patterns. Fixed strings only, because `git grep` and Python disagree on dialect, and a
  config value spliced into a regex is a recorded bug class here. A string containing a backtick is
  not expressible, and the template says so.
- Converting existing criteria. Prose greps in landed specs stay prose. The near-miss count makes
  the population visible and asks nothing of it.
- Pairing every absence invariant with a positive one about the same file. That is one of the other
  candidates in `TOOL-aHonedRuleset-12`, and this unit leaves it there.
- Grading an INPROGRESS spec's invariants at HEAD. The build is incomplete by definition, so `--list`
  shows progress and the close arm owns the verdict.
- Shipping the join to adopters. `tools/check-spec-tokens.py` is exempt from shipping in
  `tools/govkit/registry.toml`, so an adopter receives the template paragraph only.

### Edges

- **consumes-from** `TOOL-dPinnedHandoff-2` — `derive_closing_commit`, which the close arm uses to
  find the commit that closed the unit. Without it the close arm has no immutable tree to measure.
- **consumes-from** external — `TOOL-aHonedRuleset-12`, the OPEN backlog row that measured the class
  and named "run every criterion's grep at the spec's declared base" as a candidate. This unit builds
  that candidate for criteria written as `Invariant:` lines. If false: the row has been closed or
  re-scoped by build time; re-read it and bind to whatever carries the class now. Do not close it
  from this unit, which builds one of its candidates and not all.

## 4. Design

### Data model

```text
- **AC3** — When the build lands, no carrier under the kit spells the old version.
  Red when: a carrier still spells it.
  Invariant: `memory-tree@2.85` · `tools/memory-tree/` `memory/` `:!memory/builds/` · 0
```

`INVARIANT_LINE`, anchored on both ends:
`^[ \t]*Invariant:[ \t]*`([^`\n]+)`[ \t]*·[ \t]*((?:`[^`\n]+`[ \t]*)+)·[ \t]*([0-9]+)(?:[ \t]*·[ \t]*kept)?[ \t]*$`

The pathspecs pass to git as written, so pathspec magic such as `:!memory/builds/` works. A pattern
that begins with `-` is safe because the string always follows `-e`.

### The two arms

| form | at `base` | at the closing commit |
|---|---|---|
| plain | must NOT hold, else `holds at base` | must hold, else `fails at close` |
| `kept` | must hold, else `not kept at base` | must hold, else `fails at close` |

A plain invariant observes a change, and a `kept` invariant observes a preservation. The NicoCares
brief used both kinds: zero hits of the retired header was a change, and "the intake API still has
no hand-rolled fetch" was a preservation. Each form is graded in both directions, so neither is an
escape from the other.

The base arm runs on live specs. It is the one moment the criterion can still be rewritten, so it
is where a vacuous criterion is cheapest to catch. The close arm runs on CLOSED specs over an
immutable commit, so its verdict does not drift as history grows. A hit there is cleared by a waiver
row, never by rewriting the landed record.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `INVARIANT_LINE` | module constant, the parse pattern | none; constants are not graded |
| `INVARIANT_CANARY` | module constant, the self-proving sample | none |
| `extract_invariants` | function | `py.function`, checked OK by `tools/lexicon/lexicon.py --suggest` |
| `measure_invariant` | function | `py.function`, checked OK |
| `scan_invariants` | function | `py.function`, checked OK |
| `check_invariant_canary` | function | `py.function`, checked OK |

### Migration

None for the join. No spec carries an `Invariant:` line at `9b7e2de6`, which is why the canary is
the join's only proof of life on landing day. The version move is a marker change and changes no
behaviour by itself.

### Rollout

The join lands live and opt-in. This spec's own AC9 carries the first real `Invariant:` line in the
corpus, and it is graded from the landing commit onward.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/check-spec-tokens.py` | the pattern, the canary, the four functions, both arms, the report line, the docstring rows and cannot-see list |
| `tools/check-spec-tokens.test.sh` | the arms of AC1 to AC6, each staged red first, and the floor raise |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | the grammar under the acceptance guidance, and the version marker |
| `tools/memory-tree/HYGIENE.template.md` | the version marker |
| `tools/memory-tree/BUILD-METHOD.template.md` | the version marker |
| `tools/memory-tree/ANNOTATION-STYLE.template.md` | the version marker |
| `tools/memory-tree/check-memory-hygiene.sh` | `KIT_MEMORY_TREE_VERSION` |
| `memory/TEMPLATE-SPEC.md` | REGENERATED |
| `memory/HYGIENE.md` | REGENERATED |
| `memory/guides/BUILD-METHOD.md` | REGENERATED |
| `memory/guides/ANNOTATION-STYLE.md` | REGENERATED |
| `memory/guides/SESSION-KICKOFF.md` | the `last-audit` re-stamp the watched file owes |
| `memory/map/features/spec-tokens.md` | the join count in `title`, one join row, one Gaps bullet |
| `memory/backlog/TOOL.md` | at landing, the `TOOL-aHonedRuleset-12` row notes which candidate this unit built |

### Alternatives rejected

- **Run the prose greps criteria already quote.** Their shapes vary: pipes, `-c` or not, `wc -l`,
  counts written as words. A parser over them would be a second grammar recovered from prose, and the
  one this unit adds would still be needed for new specs.
- **Grade at HEAD for live specs.** A live spec is mid-build. Redding on an unmet invariant at HEAD
  reds every INPROGRESS unit on every bar until its last commit.
- **A cutoff key.** The population is opt-in and empty on landing, so a date would gate nothing,
  and the register refuses a key not strictly past its commit day anyway.

## 5. Production-readiness checklist

- security: N/A — `git grep` over committed trees. The string and pathspecs pass as argv, never
  through a shell, so a spec cannot inject a command.
- perf / scale: two `git grep` processes per invariant, one per tree. The population is new specs
  only.
- error / empty / loading states: no invariant means not graded. A malformed line is a hit. A grep
  erroring is a hit. An unresolvable base is skipped and counted, since hygiene already reds it.
- observability: the report line and the canary print every run, and `--list` shows live counts.
- risks: an invariant whose string is a runner path, such as the merge bar's, is also read by the
  `bar` join and reds there. The template tells the author to drop the path prefix.
- testing: every self-test arm is observed red on a staged break before it is kept.
- migration: none for the join; the version move is marker-only.
- user docs: the rendered template is the doc. This repo has no `help/`.

## 6. Acceptance criteria

- **AC1** — When `tools/check-spec-tokens.py` runs over a scratch repository whose live spec carries
  a plain invariant that already holds at the spec's base, it prints `holds at base` naming the
  criterion.
  Red when: no hit is printed.
  fixture: a `mktemp -d` repository the self-test builds, with a base commit and the spec.
- **AC2** — When the same spec's invariant is marked `kept` and does not hold at base,
  `tools/check-spec-tokens.py` prints `not kept at base`; when it is `kept` and holds, it prints no
  hit.
  Red when: either direction is wrong.
- **AC3** — When a CLOSED spec's invariant does not hold at the commit that closed it,
  `tools/check-spec-tokens.py` prints `fails at close` with that commit's sha8. When a later commit
  breaks the invariant again, the verdict does not change.
  Red when: the close failure passes, or the later commit changes the verdict.
- **AC4** — When an acceptance bullet carries a line opening with `Invariant:` whose count is a word
  and not a digit, `tools/check-spec-tokens.py` prints `malformed`.
  Red when: the line is skipped silently.
- **AC5** — When an invariant names a pathspec git refuses, `tools/check-spec-tokens.py` prints
  `grep failed` for that line and does not count it as zero.
  Red when: the line is graded as a zero-count match.
- **AC6** — When `tools/check-spec-tokens.py` runs over this tree, the report line prints the
  invariants examined and the canary's measured count. When the canary's string is staged out of the
  checker's source, the run reds as a dead arm.
  Red when: the report line is absent, or the staged break stays green.
  figure: DERIVED — every count comes from the run.
- **AC7** — When `memory/TEMPLATE-SPEC.md` is re-rendered from its template, its acceptance guidance
  carries the `Invariant:` grammar with both forms.
  Red when: the rendered file lacks `Invariant:`, or a fresh render differs from the committed copy.
- **AC8** — When `memory/map/features/spec-tokens.md` is read after landing, its `title` counts eight
  joins and names the invariant join.
  Red when: the title counts fewer.
- **AC9** — When `tools/check-kit-versions.sh` runs after the version move, every memory-tree carrier
  and `KIT_MEMORY_TREE_VERSION` read 2.86, and no carrier outside the build records spells the old
  marker.
  Red when: a carrier still reads 2.85.
  Invariant: `memory-tree@2.85` · `tools/memory-tree/` `memory/` `:!memory/builds/` · 0
- **AC10** — When the dry run counts acceptance bullets that quote a `grep` invocation over every
  spec in the tree, it prints the live and terminal counts. The output is recorded in this build
  folder before the join is wired.
  Red when: both counts are zero, which would mean the bullet match found nothing.
  cost: seconds.
  figure: DERIVED. At least 378 opening lines quote one, PINNED at `9b7e2de6` on 2026-09-22 as a
  sanity bound. Continuation lines were not counted, so the true figure is higher.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `kit/dogfood doc parity` · `kit version markers` · `kickoff-manifest ratchet` · `memory-hygiene self-test` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `memory hygiene`

`kit version markers` and `kickoff-manifest ratchet` are the two legs the version move arms: the
first compares every marker to the constant, and the second sees a watched file change.
`kit/dogfood doc parity` is armed by the template edits. `recall floor` and `recall floor arms` carry
the guard `memory/`. `spec-tokens self-test` and `memory-hygiene self-test` are held by default; the
post-build run reaches them.

New arm: `tools/check-spec-tokens.test.sh` · AC1's held-at-base line, AC2's two kept directions,
AC3's close failure and later break, AC4's word count, AC5's refused pathspec, AC6's staged-out
canary · the suite's floor moves by the arms added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-22 · initial draft, from the comparison of the three NicoCares handoff briefs with
  this template; the build README states the source.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "run a declared grep count from a spec acceptance
criterion against the tree at a commit"` returned no seam this unit can extend. Its candidates rank
by name fan-in on `run` and `tree`, such as `tree` in `tools/memory-recall/selftest.py` and
`load_map_tree` in `tools/codebase-map/map_lib.py`, and none measures text at a commit. The seams
this unit extends are in the checker it joins: `extract_acceptance` (`tools/check-spec-tokens.py:307-319`)
finds the section by heading text, `run` executes git without a shell, and the canary follows
`CLAIM_CANARY` and `check_claim_canary` (`tools/check-spec-tokens.py:547`). The close arm reuses
`derive_closing_commit` from `TOOL-dPinnedHandoff-2` rather than finding the closing commit twice.

Recall terms used: `python tools/memory-recall/query.py "was a halt rule on external edges, a
do-not-touch path list checked against the diff, or a runnable grep invariant as acceptance
considered before, and what decided the Edges block and the acceptance witness shape" --terms "Edges
consumes-from external precondition witness Red-when Files-touched guard join invariant grep frozen
shape-only"` — 40 hits. The load-bearing one is `TOOL-aHonedRuleset-12` in `memory/backlog/TOOL.md`,
whose first candidate this unit builds. `TOOL-cTracedPromise-2`, also OPEN, deferred a
machine-checkable witness for every criterion on cost; this unit offers one per criterion that opts in.
