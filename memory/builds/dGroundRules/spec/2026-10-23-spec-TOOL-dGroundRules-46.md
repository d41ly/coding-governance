# TOOL-dGroundRules-46 — the spec-tokens checker refuses a criterion literal that sources a shell file by bare name

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-46-deviation-34.md](../build/2026-10-23-build-TOOL-dGroundRules-46-deviation-34.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 10 at HIGH**, which shares item **H1** with ids 1
(`TOOL-dGroundRules-47`) and 20 (`TOOL-dGroundRules-45`). Id 10 is H1 seen from grounding: run from
the repository root, `TOOL-dGroundRules-40`'s `PAIRS_SH` cannot even define `overlaps`, because it
sources the unattended library by its bare file name, and `TOOL-dGroundRules-34` AC16 carries the
same form. The same corruption has now crossed two audit rounds. This unit is id 10's promotion and
the item's left-shift gate, which the review names: `tools/check-spec-tokens.py` gains a join that
reds a live spec whose acceptance section sources a shell file by a name carrying no `/`. Measured
over every spec in the tree, that predicate hits exactly the two corrupted literals and nothing else,
so it is a class gate rather than a style rule. It repairs `TOOL-dGroundRules-40`, which sits at
order 13, so it builds at order 14.

## 2. Scope (IN)

- **S1** — The join. For every live spec, `scan_bare_sources(text)` reads the acceptance section
  whole, fenced blocks included, and returns each operand of a shell source command, a `.` or
  `source` word at a command position followed by an operand ending in `.sh`, whose operand carries
  no `/`. Each one is a hit,
  `[source] <spec> :: <operand> — sources a shell file by bare name, which resolves against the working directory and not the kit`.
  Observed by AC1, AC3.
- **S2** — The whole spelling passes. An operand carrying a `/`, a tracked path such as
  `tools/unattended/lib-unattended.sh` included, is never a hit. Observed by AC2.
- **S3** — The count line. Every run prints
  `spec-tokens: source join · <n> sourced file(s) examined in <m> live spec(s)`, so a join that
  examined nothing reads as zero examined and not as clean. Observed by AC4.
- **S4** — The docstring. The module docstring of `tools/check-spec-tokens.py` names the join and
  states what it does not see: an operand built at runtime or held in a variable, a sourced file whose
  name does not end in `.sh`, and a source command outside the acceptance section. Observed by AC5.

## 3. Non-goals (OUT)

- Running a spec's literals. Executing spec text from a gate is a write surface this unit does not
  price; the join reads text only.
- Any other bare argument, such as a help page named by basename. The `TOOL-dGroundRules-42`
  measurement and this unit's own (§4 Evidence) show that predicate is the house basename style in
  most of its hits, so it cannot tell a stripped literal from a kit file named by convention.
- A cutoff key. The two live hits sit in units that are terminal before this unit builds, and a
  terminal spec is not graded (§4 Rollout).
- The arm's trap row and the probes' single spelling: `TOOL-dGroundRules-44` and
  `TOOL-dGroundRules-45`.

### Edges

none

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `0ced625e1`.

- Over all 1415 spec files under `memory/builds/*/spec/`, the pattern
  `(^|[ ;'"(])(\.|source) [A-Za-z0-9_./-]+\.sh` found nine source commands. Seven name the library
  by a path carrying `/`; two name it bare, `TOOL-dGroundRules-34` :509 and `TOOL-dGroundRules-40`
  :125, the two literals review ids 1, 10, 20 and 30 cite (PINNED).
- A wider predicate, a bare file name in an acceptance section whose full path the same spec's
  scope or design names outside `tools/`, gave 89 hits over 78 live specs, most of them the house
  "`policy.md` under `help/`" form (PINNED, scratch script).
- `tools/check-spec-tokens.py:1513` walks the acceptance bullets for the paths join and reads only
  `- ` bullets, so a fenced literal is graded by no join today; `:1675` prints the run's summary
  line, beside which the bar and guards joins print their own count lines.
- The paths join's population is the live set, OPEN, SPECCED, INPROGRESS and BLOCKED, and
  `tools/check-spec-tokens.test.sh:405-410` holds a terminal spec ungraded.
- `python tools/lexicon/lexicon.py --suggest scan_bare_sources --as py.function` answered OK.

### The join

```text
SOURCE_CMD = (?:^|[;&|('"]|\s)(?:\.|source)\s+([^\s;&|'"()]+\.sh)\b

scan_bare_sources(text):
    section = extract_acceptance(text), fenced blocks kept
    return [op for op in SOURCE_CMD.findall(section) if "/" not in op]

(spec walk, per live spec):
    examined += count of SOURCE_CMD matches; specs_with += 1 if any
    for op in scan_bare_sources(text): hits.append((f, "source", op, <the S1 reason>))
(after the walk): print the S3 line
```

A hit is waivable by the waiver registry like every other join's, which this unit adds no row to.

The fixture text the criteria plant, spelled here because a live spec's own acceptance section may
not carry it:

```text
BARE_LINE  = PROBE = bash -c '. helper.sh; f'
WHOLE_LINE = PROBE = bash -c '. tools/unattended/lib-unattended.sh; f'
```

### Rollout

`TOOL-dGroundRules-34` and `TOOL-dGroundRules-40` sit at orders 12 and 13 and close before this unit
builds, so the join meets no live hit at its own close. A spec still live then, through a park, is a
true finding of this join, not a false one.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `scan_bare_sources` | py.function | `tools/check-spec-tokens.py` |
| `source join` | a report line | `tools/check-spec-tokens.py` |

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A leg that runs every read-only section-6 literal from the root and reds on exit 127.** It
  executes spec text, which widens the write surface, and deciding "read-only" from text is the
  judgement no gate can make.
- **The bug-class checklist entry alone.** It is `TOOL-dGroundRules-47`'s, and a checklist the same
  author skipped twice does not catch the third.

## 5. Production-readiness checklist

- security — the join reads spec text and runs nothing it reads.
- perf / scale — one regex pass over each live spec's acceptance section.
- error / empty / loading states — the count line makes an empty population visible.
- observability — each hit names the spec and the operand.
- risks — a prose sentence in a criterion that spells a dot, a space and a bare `.sh` name at a
  command position reads as a source; none exists in the corpus measured.
- testing — AC1 to AC5 and the arm.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: a gov-only checker; its docstring is its reference (S4).

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. A scratch copy is a git clone
of this repository under `%TEMP%/gr46`, checked out at the commit under test. The literal stagings are
spelled whole here, once, and the criteria name them:

```text
PLANT_BARE  = in the scratch copy, BARE_LINE (section 4) appended inside the first fenced block of
              the acceptance section of TOOL-dGroundRules-52's spec, which is live until order 16
PLANT_WHOLE = the same, with WHOLE_LINE in place of BARE_LINE
DOC_JOIN    = grep -c "source join" tools/check-spec-tokens.py
```

- **AC1** — When `PLANT_BARE` runs and `python tools/check-spec-tokens.py --list` runs in that copy,
  it prints a `[source]` hit naming that spec and `helper.sh`.
  Red when: a bare-name source in a fenced acceptance literal is graded by no join.
- **AC2** — When `PLANT_WHOLE` runs and the same `--list` runs in that copy, it prints no `[source]`
  hit.
  Red when: the whole spelling the fix prescribes is refused with the stripped one.
- **AC3** — When `python tools/check-spec-tokens.py --list` runs on the built tree, it prints no
  `[source]` hit.
  Red when: a live spec carries a criterion that cannot define the function it calls.
  fixture: units 34 and 40 terminal, which their orders make them before this unit builds.
- **AC4** — When the AC3 command runs, it prints the `source join ·` count line.
  Red when: a join that examined nothing reads as clean.
  figure: both counts DERIVED at observation time.
- **AC5** — When `DOC_JOIN` runs on the built tree, it prints `1` or more.
  Red when: the docstring omits the join and what it cannot see.

## 7. Gates

`spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `spec tokens (a spec's own names resolve)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 · a scratch repository whose one live spec's acceptance fence sources a shell file by bare name, then by its path · that suite's assertion count, raised by the arm

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 10 (HIGH, item H1) of the round-1 spec
  audit of units 35 to 43 as the item's left-shift gate, with the bare-source predicate and a wider
  bare-name predicate measured over the spec corpus on 2026-10-23.

## 10. Reuse audit

The seam extended is `tools/check-spec-tokens.py`, whose spec walk, acceptance-section reader and
waiver registry every join shares; the new join is one scan function and one count line inside them,
and its arm uses the suite's `scratch` and `arm` helpers (`tools/check-spec-tokens.test.sh:199-243`).
`python tools/codebase-map/reuse_lookup.py "flag a shell library sourced by a bare file name in a
spec acceptance literal"` ranked `read_spec_revisions`, `parse_spec_h1` and `build_spec_path_re`,
none of which reads a source command; no existing seam fits the scan itself. The recall probe
returned `TOOL-dGroundRules-42`, whose S5 measured the wider basename predicate as unusable, and the
open ask `TOOL-aKeyedAnnotation-9` on the paths join; both agree with this narrower join.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
