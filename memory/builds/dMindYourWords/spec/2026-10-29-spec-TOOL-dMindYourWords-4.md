# TOOL-dMindYourWords-4 — override markers verified against the packs

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 10 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0265@a234cd84 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |
| [2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-12 TOOL-dMindYourWords-11 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-9 TOOL-dMindYourWords-16 TOOL-dMindYourWords-13 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

An override marker (`@typing.override`, `@typing_extensions.override`, TypeScript's `override`) is a
claim that some ancestor defines the member, and today the lexicon reads no such claim: it records a
decorator by its last segment and checks nothing. This unit verifies each Python marker against the
repository's own classes and the packs, reds only a marker no ancestor can define, as PEP 698 rules,
and reports every marker it cannot prove either way. A marker never exempts a name.

## 2. Scope (IN)

- **S1** — Marker recognition. A Python definition is a marked site when its `decorators`, read through
  TOOL-dMindYourWords-12's accessor `read_definition_context` (I5) at the working tree with aliases
  resolved, include `typing.override` or `typing_extensions.override`. So `from typing import override
  as ov` then `@ov` is a marked site, where `extract_decorators` (`tools/lexicon/lexicon.py:2527-2573`)
  reads it today as `ov`. The same rows' `enclosing` and `bases` start S2's walk. Observed by AC1, AC2.
- **S2** — The verdict. `check_override_marker(site, ancestry, packs)` in `tools/lexicon/lexicon.py`,
  beside `extract_decorators`, returns one of `confirmed`, `unconfirmed` or `red` with its reason, by
  the table in §4 "The verdict table". A confirmation carries its source in I2's spelling,
  `parent:<path>::<Class>` or `pack:<kit>:<row>` (TOOL-dMindYourWords-2). Observed by AC1, AC3, AC4,
  AC5.
- **S3** — The red. Each `red` verdict appends one refusal to `measure_pass`'s `problems`, spelled
  `MARKER WITHOUT BASE — <site> carries @override and no ancestor defines it (PEP 698): <chain>`,
  `<site>` in I3's spelling `<path>::<Class>.<name>` (TOOL-dMindYourWords-5) and no line number, so
  the `--offenders` key `render_offender_keys` (`:3482-3515`) builds from it survives a line move.
  `--check` and `--measure` exit 1 on it, as on every refusal there. Observed by AC1, AC2, AC3, AC7.
- **S4** — The tally. One line on green and on red, after I2's forced tally line:
  `lexicon: markers override=<n> confirmed=<c> (parent=<p>, pack=<k>) unconfirmed=<u> (outside=<o>,
  unresolved=<r>) red=<x>; ts-override=<t> reported`. Observed by AC1, AC4, AC5, AC6.
- **S5** — TypeScript reports until the second wave. Over every armed `ts` or `tsx` file the unit counts
  each `word` token `override` that `scan_ts_tokens` (`:950`) yields after a member head of
  `_TS_MEMBER_HEAD` (`:1672-1673`) and before a member name, and prints the count as `ts-override`.
  No TypeScript marker reds and none confirms: class context for TypeScript arrives with the
  extraction primitive's second wave (lexicon review `[forced]` item 1). Observed by AC6.
- **S6** — The docs and version. `tools/lexicon/README.md` and `tools/lexicon/LEXICON.md` state the
  verdict table, that a marker never exempts, and the TypeScript report; `KIT_LEXICON_VERSION`
  (`lexicon.py:90`) moves. Observed by AC8.

## 3. Non-goals (OUT)

- The forced exemption itself. Whether a marked name is forced, and by what, is TOOL-dMindYourWords-2's
  check; a marker is a fast path, never a pass (lexicon review `[forced]` item 3), so this unit grades
  nothing and exempts nothing.
- `hookimpl` and every other host marker. The clause names override markers; a pytest hook is forced
  by its pack's host row by name, which is TOOL-dMindYourWords-2's.
- The extractor and the definition context. I5 is TOOL-dMindYourWords-12's, and changing an
  extractor's output is TOOL-dTotalRecall-13's §3 non-goal; `extract_decorators` is not widened here.
- Pack data, its grammar and its loader (TOOL-dMindYourWords-7) and which packs apply
  (TOOL-dMindYourWords-8, which hands its selected set to S2).
- JavaScript markers, which have no `override` syntax, and a TypeScript marker red, which waits on the
  second wave.

### Edges

- **consumes-from** `TOOL-dMindYourWords-12` — `extract_ranges` with `context=True`, its definition context (I5): each definition's enclosing class, that class's bases resolved through imports, and its decorators with aliases resolved; without it an aliased marker is invisible and no ancestor can be walked
- **consumes-from** `TOOL-dMindYourWords-7` — `load_pack` and `Pack.read_row`, the one row matcher: asked with an outside ancestor as the base it confirms a marker there, and asked with base `None` the `python` pack's host rows confirm a marked dunder
- **consumes-from** `TOOL-dMindYourWords-2` — `Offender.source`, the spelling of a confirmation's source, and the in-repository base resolution and class index its parent-forced case builds (`resolve_forced_source`, `build_class_index`), which S2 walks instead of building a second
- **hands-off** `TOOL-dMindYourWords-8` — `check_override_marker`: its `packs` argument becomes the selected set in place of every shipped pack
- **hands-off** `TOOL-dMindYourWords-29` — its pass commit's `KIT_LEXICON_VERSION` move, which the minors batch observes against the pass base (review id 10)

## 4. Design

### Evidence

Read at `ba8b3c8c4`; no product file differs from base `ccd1292e`.

- `extract_decorators` (`tools/lexicon/lexicon.py:2527-2573`) returns `{(path, lineno, name): {decorator,
  …}}` for a `python-ast` extension, recording a dotted decorator by its last segment (`:2567`) and an
  aliased one by its alias; it resolves nothing through imports and records no enclosing class.
- `_python_defs` (`:425-456`) walks with `ast.walk` and records no class membership, so no base can be
  walked from today's extraction.
- `_TS_MEMBER_HEAD` (`:1672-1673`) already holds `override`; `scan_ts_tokens` (`:950`) yields
  `(kind, text, line)` code tokens.
- `measure_pass` (`:2796`) collects refusals into `problems`, which `check_pass` prints and which
  `render_offender_keys` (`:3482-3515`) emits under the rule `problem`, whitespace-collapsed.
- The population: 0 `@override` markers in this tree outside records (scout A row 4; prior-art:71),
  re-read by `git grep -n "@override"` over `*.py` at `ba8b3c8c4`, which matched none outside
  `memory/`. PINNED at that sha. The planted fixtures of §6 are the population, and one of them is a
  marker that fails.

### The verdict table

`ancestry` is the chain S2 walks from the site's enclosing class: each base resolved through I5's
imports, an in-repository base followed to its own bases through TOOL-dMindYourWords-2's class index,
until every branch ends at `object`, at a base outside the repository, or at a base that does not
resolve. A class with no bases has `object` as its one base. First matching row wins.

| Site | What the walk finds | Verdict |
|---|---|---|
| marked, no enclosing class | nothing to walk | `red`: no base at all |
| marked method | an in-repository ancestor whose body defines the member | `confirmed`, `parent:<path>::<Class>` |
| marked method | `Pack.read_row(<ancestor>, <name>)` returns a member or prefix row for an outside ancestor | `confirmed`, `pack:<kit>:<row>` |
| marked dunder | the chain reaches `object` and `Pack.read_row(None, <name>)` returns a `python` pack host row | `confirmed`, `pack:<kit>:<row>` |
| marked method | no confirmation; some base did not resolve | `unconfirmed`, `unresolved` |
| marked method | no confirmation; some ancestor is outside the repository, packed or not | `unconfirmed`, `outside` |
| marked dunder | no confirmation; the chain is complete and no `python` pack is selected | `unconfirmed`, `outside` |
| marked method, not a dunder | no confirmation; every ancestor is in the repository and the chain ends at `object` | `red` |

Two facts make the last row sound. `object` defines only dunder names (`dir(object)` holds nothing
else on any Python this kit runs on), so a chain of in-repository classes ending there is a complete
inventory of what can define a non-dunder member. And a pack row is a FORCED name, never an inventory
of a base's members, so a missing row on an outside base proves nothing: that ancestor reports and
never reds (§8 F1). "Defines" means a `def` of that name in the class body, a `@property` included;
a class attribute assigned a value is not read, and an override of one reports as `unconfirmed` only
where an outside ancestor exists, which is the stated limit.

### Files touched (estimate)

- `tools/lexicon/lexicon.py` — `check_override_marker`, its call in `measure_pass` after the forced check,
  the S4 line in `check_pass`, the S5 count, `KIT_LEXICON_VERSION`
- `tools/lexicon/selftest.py` — the planted fixtures of §6
- `tools/lexicon/README.md`
- `tools/lexicon/LEXICON.md`

### Alternatives rejected

- **Widening `extract_decorators` to resolve aliases.** Lost to I5: unit 12 owns the definition context,
  and `extract_decorators` becomes its adapter; a second alias resolver is two answers to one question.
- **Reading a missing pack row as "the base does not define it".** Rejected by the test the verdict table
  states: a pack lists forced names, so `logging.Handler`'s `format` or a member a later version added
  has no row while the base defines it; the red would fall on a correct override.
- **The red as a debt offender counted by the pin.** Rejected in §8 F2: under `lexicon.pin = absorb` a
  correctness error would be absorbed, and `[classes]` has no class for a broken claim.

## 5. Production-readiness checklist

- security — reads committed source and pack data only; imports and runs nothing (lexicon review
  `[forced]` item 5).
- perf / scale — one walk per marked site over an index the forced check already built; markers are
  rare (0 in this tree), so the cost is the TypeScript token count, which rides files already tokenized.
- error / empty / loading states — a tree with no marker prints `override=0` and the line still prints;
  a site whose base does not resolve reports `unresolved`, never red.
- observability — the S4 line on green and red; each red names the site and the chain it walked.
- risks — an adopter with a broken `@override` reds at its next run; that is PEP 698's own error, which a
  type checker already reports.
- testing — the planted fixtures of §6, each red case observed red and green without its plant.
- migration — none; no data moves.
- user docs — `tools/lexicon/README.md` and `tools/lexicon/LEXICON.md`; no `help/` page covers the
  lexicon.

## 6. Acceptance criteria

- **AC1** — When `python lexicon.py --check` runs in a fixture repository whose `base.py` defines
  `class Base` with `run_a` and whose `child.py` holds `class Child(Base)` with `@override` from
  `typing` on `run_b`, it prints one `MARKER WITHOUT BASE` line naming `child.py::Child.run_b` and the
  chain `Child -> Base -> object`, the S4 line reads `red=1`, and it exits 1; with the marked method
  renamed `run_a` the line is gone and the S4 line reads `confirmed=1 (parent=1, pack=0)`.
  Red when: the planted marker on a method its base does not define passes.
  fixture: the selftest builds the repository under the temp root, the kit copied beside it.
- **AC2** — When the same fixture spells the marker `from typing import override as ov` then `@ov`, and
  again as `typing_extensions.override`, `--check` prints the same `MARKER WITHOUT BASE` line each time.
  Red when: an aliased or `typing_extensions` marker is not read as a marker.
- **AC3** — When the fixture carries `@override` on a module-level function `run_free`, `--check`
  prints `MARKER WITHOUT BASE` naming `run_free` with `no base at all`, and exits 1.
  Red when: a marker outside a class body passes.
- **AC4** — When the fixture holds `class H(logging.Handler)` with `@override` on `emit`, the S4 line
  counts it `confirmed` with source `pack:python:` from the shipped `python` pack; with `@override` on
  `run_bogus` in the same class it counts `unconfirmed` under `outside`, and no `MARKER WITHOUT BASE`
  line prints for either.
  Red when: an outside base's missing row reds, or the row-confirmed marker reads unconfirmed.
  fixture: the first-wave `python-3.12.toml` and `python-3.14.toml` packs TOOL-dMindYourWords-7 ships,
  whose `member` rows carry `logging.Handler` and whose `host` rows carry the data model.
- **AC5** — When the fixture holds `class C(make_base())` with `@override` on `run_x`, `class
  D(somelib.Base)` with `@override` on `run_y` and `class E` with no bases and `@override` on
  `__repr__`, the S4 line reads `unresolved=1`, `outside=1` and one more `confirmed` under `pack`, and
  no red prints.
  Red when: an unresolved or unpacked base reds, or the marked dunder is not confirmed.
- **AC6** — When the fixture arms `ts` under `ts-tokens` and holds `class A extends B { override render()
  {} }`, the S4 line ends `ts-override=1 reported` and the exit is 0.
  Red when: a TypeScript `override` reds, or is not counted.
- **AC7** — When `python lexicon.py --offenders` runs over AC1's planted fixture, one key reads
  `-`, `problem` and the `MARKER WITHOUT BASE` text with no line number, and moving `run_b` down five
  lines leaves that key byte-identical.
  Red when: the key carries a line number, so a line move changes it.
- **AC8** — When `grep -n "MARKER WITHOUT BASE" tools/lexicon/README.md tools/lexicon/LEXICON.md`
  runs, each file names the refusal and the TypeScript report, and `KIT_LEXICON_VERSION` in
  `tools/lexicon/lexicon.py` differs from `1.24`.
  Red when: either document omits the marker rule.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the planted marker fixtures, its failing case `@override` on `run_b` that `Base` does not define · none

## 8. Open questions

- **F1 — A marker on an outside base whose pack holds no row for the member: red or report?** Options:
  (a) report it `unconfirmed`, `outside`; (b) red it when the covering pack is generated rather than
  curated; (c) red it always. (b) and (c) red a correct override wherever a pack's rows omit a member
  the base defines, since a row is a forced name and not a member inventory, which fails the clause's
  own rule that only a marker with no defining base reds (veto 1). RESOLVED (agent, 2026-10-29,
  delegated): (a), rung 3, the one survivor; the red is kept for the case the tree can prove, every
  ancestor in the repository and the chain ending at `object`. widens: none · relaxes: none
- **F2 — Where does the red sit?** Options: (a) a refusal in `problems`, exit 1 under every
  `lexicon.pin` value; (b) an offender graded `debt` and counted by the pin; (c) a third predicate kind
  in `KINDS` with its own pin. (b) lets `absorb` keep a broken claim and gives "debt" a correctness
  meaning `[classes]` does not; (c) adds a pin the clause's one-pin rule (TOOL-dMindYourWords-1)
  retires. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the most feature-rich survivor: the
  refusal reaches `--offenders` as a keyed `problem`, so the bar's by-name comparison reads it too.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Item 4, the lexicon review's `[forced]` items 1
  and 3, review findings M22 (B) and L4 (A) on PEP 698, scout A's row 4, and the spec brief's I2, I3, I5
  and I6.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-29); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `extract_decorators` (`tools/lexicon/lexicon.py:2527`), beside which
`check_override_marker` sits and whose decorator read I5 replaces; `measure_pass`'s `problems` list
(`:2796`) for the red; `check_pass`'s count lines (`:3378-3390`) for S4; and `scan_ts_tokens` (`:950`)
with `_TS_MEMBER_HEAD` (`:1672`) for the TypeScript count. TOOL-dMindYourWords-2's class index and
base resolution are walked, never rebuilt. `python tools/codebase-map/reuse_lookup.py "verify an
override decorator marker against the base class that defines the method"` ranked `resolve_compare_base`,
`extract_prompt_marker` and `derive_marker_basis` first, each a name-stem match; none walks a class
hierarchy, so the verdict table is new and every reader it calls exists or is a parent unit's. Scout A's
row 4 holds against source at `ba8b3c8c4`: `extract_decorators` is at `:2527-2573` and keys
`(path, lineno, name)`. The recall probe surfaced review findings M22 and L4, which read PEP 698 as
"no ancestor, in-repo or packed, defines the member"; §8 F1 records why a packed ancestor reports
rather than reds.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon verify an override marker
against a base or pack" --terms "lexicon override marker PEP 698 decorator base pack forced
extract_decorators debt"`
