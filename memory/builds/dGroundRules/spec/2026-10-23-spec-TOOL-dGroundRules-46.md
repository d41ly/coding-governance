# TOOL-dGroundRules-46 — the spec-tokens checker refuses a criterion literal that sources a shell file by bare name

**Status:** CLOSED · rev-3 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-46-deviation-34.md](../build/2026-10-23-build-TOOL-dGroundRules-46-deviation-34.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-46-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-46-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-46-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-46-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-43-staleness-probe-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-43-staleness-probe-brief.md) | research | TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 |
| [2026-10-24-prompt-TOOL-dGroundRules-46-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-46-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-46-probe-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-46-probe-fix-brief.md) | research | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 35 to 43
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md`)
exited BOUNDED with finding **id 10 at HIGH**, which shares item **H1** with ids 1
(`TOOL-dGroundRules-47`) and 20 (`TOOL-dGroundRules-45`). Id 10 is H1 seen from grounding: run from
the repository root, a criterion literal that sources the unattended library by its bare file name
cannot even define `overlaps`. `TOOL-dGroundRules-34` AC16 carries that form, and
`TOOL-dGroundRules-40`'s `PAIRS_SH`, `TOOL-dGroundRules-44`'s `TRAP_SH` and
`TOOL-dGroundRules-45`'s `PAIRS_TABLE` carried it until their rev-4, rev-4 and rev-3. The same
corruption has crossed two audit rounds. This unit is id 10's promotion and the item's left-shift
gate, which the review names: `tools/check-spec-tokens.py` gains a join that reds a live spec whose
acceptance section sources a shell file by a name carrying no `/`, a code span's opening word
included. Measured over every spec in the tree (§4 Evidence), the source commands' bare operands
are exactly two, unit 34's AC16 literal and this spec's own `BARE_LINE` fixture, the H1 corruption
and its staged copy, and over acceptance sections the join's own pattern finds unit 34's alone, so
it is a class gate rather than a style rule. It builds at order 14, after `TOOL-dGroundRules-40` at order 13.

## 2. Scope (IN)

- **S1** — The join. For every live spec, `scan_bare_sources(text)` reads the acceptance section
  whole, fenced blocks included, and returns each operand of a shell source command, a `.` or
  `source` word at a command position followed by an operand ending in `.sh`, whose operand carries
  no `/`. A command position includes the first word of a code span, directly after a backtick,
  and the operand stops before a backtick. Each one is a hit,
  `[source] <spec> :: <operand> — sources a shell file by bare name, which resolves against the working directory and not the kit`.
  Observed by AC1, AC3, AC6.
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
- A cutoff key. The one bare operand in an acceptance section sits in unit 34, which is CLOSED and
  so not graded, and a spec live with one when this join lands is a true hit (§4 Rollout).
- The arm's trap row and the probes' single spelling: `TOOL-dGroundRules-44` and
  `TOOL-dGroundRules-45`.

### Edges

- **hands-off** `TOOL-dGroundRules-63` — AC3, which that unit observes at its own close with units 34, 40, 44 and 45 terminal, and its re-measure of the population at `7810198ad`, which this spec's rev-3 restates in §4 Evidence (ids 6, 15 and 21 of the spec run's closing diff review)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 over the working tree on `7a600abf5`, which holds
`TOOL-dGroundRules-44` rev-4 and `TOOL-dGroundRules-45` rev-3 as this pass revises them, except the
one marked `0ced625e1`.

- Over all 1533 spec files under `memory/builds/*/spec/`, the pattern
  `(^|[ ;'"(])(\.|source) [A-Za-z0-9_./-]+\.sh` found 17 source commands. Fifteen name the file by
  a path carrying `/`, among them unit 40's `PAIRS_SH`, unit 44's `TRAP_SH` and unit 45's
  `PAIRS_TABLE`; two name it bare: `TOOL-dGroundRules-34` AC16, the H1 literal review ids 1, 10, 20
  and 30 cite, and this spec's own `BARE_LINE` (The join, below), its fixture (PINNED).
- `SOURCE_CMD` (The join, below) over the acceptance section of each of those files matched 12
  operands in 10 specs. One is bare, unit 34's, and none of the twelve sits in a live spec: unit 34
  is CLOSED, and each of the other nine specs reads a status outside `LIVE` (PINNED, scratch
  script). Over whole files the same pattern also matches eight bare operands outside any acceptance
  section: `BARE_LINE` and `TICK_LINE`, four git pathspecs opening a code span, and two code spans
  in prose quoting a bare source, in `TOOL-dDerivedDocket-24` and `TOOL-dGroundRules-53`; the join
  does not read them.
- A wider predicate, a bare file name in an acceptance section whose full path the same spec's
  scope or design names outside `tools/`, gave 89 hits over 78 live specs at `0ced625e1`, most of
  them the house "`policy.md` under `help/`" form (PINNED, scratch script).
- In `main` of `tools/check-spec-tokens.py`, the paths join's bullet loop over `extract_acceptance`
  reads only `- ` bullets and their continuation lines, so a fenced literal is graded by no join
  today; `main` prints the run's summary line, live and terminal specs counted, and after it the
  bar, guards, claims, covers, hands-off, size and carries joins print their own count lines.
- The paths join's population is the checker's `LIVE` set, OPEN, SPECCED, INPROGRESS and BLOCKED,
  so a DEFERRED spec is counted terminal and not graded, and the suite's arm "a CLOSED spec is
  frozen, so it refuses rather than grading" in `tools/check-spec-tokens.test.sh` holds a terminal
  spec ungraded.
- `python tools/lexicon/lexicon.py --suggest scan_bare_sources --as py.function` answered OK.

### The join

```text
SOURCE_CMD = (?:^|[;&|('"`]|\s)(?:\.|source)\s+([^\s;&|'"()`]+\.sh)\b

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
TICK_LINE  = - When `. helper.sh; f` runs, it prints `0`.
```

### Rollout

The join's pattern meets one bare operand in an acceptance section, `TOOL-dGroundRules-34` AC16
(Evidence), and that spec is CLOSED, so the join meets no live hit at its own close.
`TOOL-dGroundRules-40`, `TOOL-dGroundRules-44` and `TOOL-dGroundRules-45` source the library by its
tracked path. A spec live with a bare source when this join lands, at its build or through a park,
is a true finding of this join, not a false one. `TOOL-dGroundRules-63` observes AC3 again at its
own close (§3 Edges).

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
  command position reads as a source, and so does a code span that quotes the stripped form or
  opens on a git pathspec such as `:!*.test.sh`; each is waivable, and none sits in an acceptance
  section of the corpus measured (§4 Evidence).
- testing — AC1 to AC6 and the arm.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: a gov-only checker; its docstring is its reference (S4).

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. A scratch copy is a git clone
of this repository under `%TEMP%/gr46`, checked out at the commit under test. The literal stagings are
spelled whole here, once, and the criteria name them:

```text
PLANT_BARE  = in the scratch copy, this unit's own spec with its status cell set to INPROGRESS, so
              the checker grades it (a DEFERRED spec is counted terminal), and BARE_LINE (section 4)
              appended inside the first fenced block of its acceptance section, this block
PLANT_WHOLE = the same, with WHOLE_LINE in place of BARE_LINE
PLANT_TICK  = the same spec at INPROGRESS, with TICK_LINE (section 4) appended as the last line of
              its acceptance section, a bullet outside any fenced block, in place of BARE_LINE
DOC_JOIN    = grep -c "source join" tools/check-spec-tokens.py
```

- **AC1** — When `PLANT_BARE` runs and `python tools/check-spec-tokens.py --list` runs from that
  copy's root, it prints a `[source]` hit naming that spec and `helper.sh`.
  Red when: a bare-name source in a fenced acceptance literal is graded by no join.
- **AC2** — When `PLANT_WHOLE` runs and the same `--list` runs from that copy's root, it prints no
  `[source]` hit.
  Red when: the whole spelling the fix prescribes is refused with the stripped one.
- **AC3** — When `python tools/check-spec-tokens.py --list` runs on the built tree, it prints no
  `[source]` hit.
  Red when: a live spec carries a criterion that cannot define the function it calls.
  fixture: unit 34 CLOSED; units 40, 44 and 45 source the library by its tracked path.
- **AC4** — When the AC3 command runs, it prints the `source join ·` count line.
  Red when: a join that examined nothing reads as clean.
  figure: both counts DERIVED at observation time.
- **AC5** — When `DOC_JOIN` runs on the built tree, it prints `1` or more.
  Red when: the docstring omits the join and what it cannot see.
- **AC6** — When `PLANT_TICK` runs and the same `--list` runs from that copy's root, it prints a
  `[source]` hit naming that spec and `helper.sh`.
  Red when: a bare-name source that opens a code span, directly after its backtick, is graded by no join.

## 7. Gates

`spec-tokens self-test` · `memory-hygiene self-test` · `build-index selftest` · `spec tokens (a spec's own names resolve)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC6 · a scratch repository whose one live spec's acceptance fence sources a shell file by bare name, then by its path, then whose acceptance bullet opens a code span on a bare-name source · that suite's assertion count, raised by the arm

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 10 (HIGH, item H1) of the round-1 spec
  audit of units 35 to 43 as the item's left-shift gate, with the bare-source predicate and a wider
  bare-name predicate measured over the spec corpus on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-63 added, the reciprocal of
  that unit's **consumes-from** line: the promotion of the spec run's closing diff review's M1 (ids
  6, 15 and 21), which re-measures this unit's population with units 44 and 45 and observes AC3. No
  scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-24 · §1 §2 §3 §4 §5 §6 §7 §9 §10 · disagreements, from a read-only probe of step 14 at
  0860b8c1e: `PLANT_BARE` planted into TOOL-dGroundRules-52's spec, DEFERRED and so never graded;
  §7 lacked `policy fixtures`, whose guard holds the checker since TOOL-dGroundRules-20; the Goal's
  "exactly two" and the Evidence and Rollout population predated units 44 and 45, and unit 40's
  rev-4 had respelled its literal whole; the checker and suite citations had moved. Rulings:
  `PLANT_BARE` plants into this unit's own spec read as INPROGRESS; `policy fixtures` added; the
  population restated over the working tree on 7a600abf5, 1533 spec files and 17 source commands,
  where unit 44 rev-4 and unit 45 rev-3 of this pass spell the library whole, so two bare operands
  remain, unit 34's (CLOSED) and this spec's `BARE_LINE`, and the Goal's two is now those; the
  cutoff-key non-goal, the hands-off edge and AC3's fixture made to match; every moved citation
  named by symbol. This restates in the text what TOOL-dGroundRules-63 S1 and S2 re-measure, by the
  run's ruling over that unit's non-goal of editing this spec; 63 still observes AC3 at its close.
  Adopted in the same rev by the run's M3 ruling on a gap this pass found: `SOURCE_CMD` also reads a
  command position directly after a backtick and stops its operand before one, so a criterion whose
  code span opens on a bare-name source is caught; S1 says so, `TICK_LINE` and `PLANT_TICK` stage
  it, AC6 observes it, the arm covers it, and §5 names the quoted-form and pathspec risk it adds.

## 10. Reuse audit

The seam extended is `tools/check-spec-tokens.py`, whose spec walk, acceptance-section reader and
waiver registry every join shares; the new join is one scan function and one count line inside them,
and its arm uses the `scratch` and `arm` helpers of `tools/check-spec-tokens.test.sh`.
`python tools/codebase-map/reuse_lookup.py "flag a shell library sourced by a bare file name in a
spec acceptance literal"` ranked `read_spec_revisions`, `parse_spec_h1` and `build_spec_path_re`,
none of which reads a source command; no existing seam fits the scan itself. The recall probe
returned `TOOL-dGroundRules-42`, whose S5 measured the wider basename predicate as unusable, and the
open ask `TOOL-aKeyedAnnotation-9` on the paths join; both agree with this narrower join.

Recall terms used: `python tools/memory-recall/query.py "how is a stripped criterion literal repaired
and kept from being respelled" --terms "acceptance criterion literal stripped respelled fenced block
root re-run paths join spec-tokens table"`
