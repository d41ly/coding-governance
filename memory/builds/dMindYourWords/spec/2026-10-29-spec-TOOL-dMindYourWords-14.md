# TOOL-dMindYourWords-14 — the lexicon kit's own defects: repeated headers, non-names, dead modes, one pin story

**Status:** DEFERRED · rev-3 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 2 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0275@f7d892e0 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-14-reuse-scout-d.md](../build/2026-10-29-build-TOOL-dMindYourWords-14-reuse-scout-d.md) | research | TOOL-dMindYourWords-15 TOOL-dMindYourWords-17 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-15 TOOL-dMindYourWords-12 TOOL-dMindYourWords-11 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-9 TOOL-dMindYourWords-16 TOOL-dMindYourWords-13 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

Fix the four defects gap-lex-07 names in the lexicon kit, as one batch: a repeated block header in
`.lexicon.conf` silently replaces the earlier block, an IIFE value and three `@property` definitions
are graded as verbs, `--brief` and `--help` exit 2 though about 130 calls used them, and the Skill,
the conf and the README each state a different pin. The pin they must agree on is
TOOL-dMindYourWords-1's.

## 2. Scope (IN)

- **S1** — The repeated-header refusal (I8). `load_conf`'s block loop
  (`tools/lexicon/lexicon_conf.py:139-157`) records the line of each `BLOCK_KEYS` header it opens, and
  a second header of the same key raises `ConfError` with the message
  `"{p}:{lineno}: duplicate block header {key!r}, first seen at line {n}"`, mirroring `_parse_rows`'
  duplicate-row refusal (`:198-200`). A commented header (`#   CELLS:`) stays a comment. Every block
  a later unit adds inherits the refusal through the same loop. Observed by AC1 and AC2.
- **S2** — Properties ungraded as verbs. In `measure_pass`'s P1 loop (`tools/lexicon/lexicon.py:2941`)
  a Python definition whose decorator set, from `extract_decorators` (`:2527`) computed once per armed
  `python-ast` extension before the loop, holds `property`, `cached_property`, `setter`, `getter` or
  `deleter` takes `Offender.grade` `not-a-name` before the verb test and never reaches it. The
  extractor's output is unchanged (§8 F3); the definition still counts in the graded population, and
  its case is still graded by its `CELLS` row (§8 F2). Observed by AC3 and AC4.
- **S3** — IIFE values ungraded. The `js-regex` arrow pattern's parameter list becomes `\([^()]*\)`, so
  `const holder = (() => {…})()` yields no definition while `const f = (a, b) => …` still does, the
  rule `parse_ts_defs` (`:1693`) already applies. At HEAD the pattern is `lexicon.py:146`; at the build
  run's base it sits in the `extract_code` block (TOOL-dTotalRecall-13 S1), so the pass edits
  `tools/lib/extract_code.py` and its two copies under the `extract_code` parity row. Observed by AC5
  and AC6.
- **S4** — The dead modes answered. `main` (`lexicon.py:4356-4378`) takes its usage text from one
  `render_usage(me)`; `--help` prints it on stdout and exits 0, and `--brief` prints it with one line
  naming `--suggest <name> --as <ext>.<surface>` as the mode that answers "what should I call this",
  and exits 0; every other unknown mode keeps the usage on stderr and exit 2. The precedent is
  `tools/memory-tree/backlog.py:2312`. `scaffold_lexicon.py`'s refusal of `--help` as a destination
  (`:189-198`) is untouched. Observed by AC7 and AC8.
- **S5** — One pin story across the carriers. Each live sentence stating the pin as a two-sided
  equality is rewritten to TOOL-dMindYourWords-1 §4's pin sentence, or cut where its paragraph's only
  subject was a seam that unit removed. The population is a grep at the pass's base, never a line list
  (review M17's left-shift): `git grep -n -i -E "two-sided|equality in both directions"` over
  `tools/lexicon/`, `.lexicon.conf` and the rendered Skill. At `ba8b3c8c4` it reads 47 hits, of which nine
  mean a git diff (`adopt-lexicon.sh:330`, `:345`, `:348`, `:369`; `selftest.py:4631`, `:4638`,
  `:4711`, `:4725`, `:4730`) and stay, and those TOOL-dMindYourWords-1 rewrites with its code
  (`lexicon.py:3274-3360`, `scaffold_lexicon.py:292`, `:369`, `:430`, `selftest.py:2071`, `:2428`,
  `:3470`) are gone by this pass. The carriers left are `lexicon.py`'s `run_expand` COST line (`:4099`),
  `README.md` (`:134`, `:547`, `:591`), `LEXICON.md:180`, `SKILL.template.md:53` and `:58`, `kit.toml`'s
  `lexicon-pins` hole text (`:190`), `adopt-lexicon.sh:559-560`, line 2 of both waiver files, and the
  conf comments that remain. `tools/lexicon/README.md:650`, which calls the waiver registry
  shrink-only, stays. Observed by AC9.
  **Readers:** by name: `tools/lexicon/selftest.py`, whose arm H2 (`:4247-4248`) asserts the literal
  `TWO-SIDED EQUALITY` in `tools/lexicon/SKILL.template.md` and moves with S6, and
  `tools/lexicon/adopt-lexicon.sh`, which renders that template; no other code spells the sentences ·
  by value: the rendered Skill `.claude/skills/lexicon/SKILL.md`, compared with its template by
  `adopt-lexicon.sh --check` and regenerated in S6; line 2 of each waiver file is a `#` comment that
  `load_waivers` skips (`lexicon.py:2333`), so nothing reads its value.
- **S6** — The Skill reconciled. `SKILL.template.md:10-11` says a non-fitting name is refused, which
  becomes true under `lexicon.pin = shrink-only`, the default: a new debt offender is an undeclared
  ledger row and reds. The template says so with the condition, the "What the gate does with it"
  section (`:51-60`) states the ledger and the three values, and selftest arm H2 (`selftest.py:4241-4248`),
  which asserts the literal `"TWO-SIDED EQUALITY"`, asserts the pin sentence instead. The render
  `.claude/skills/lexicon/SKILL.md` is regenerated by `adopt-lexicon.sh --render`, and
  `KIT_LEXICON_VERSION` moves. Observed by AC10.

## 3. Non-goals (OUT)

- The pin mechanism, the ledger and the selftest arms that grade them (AC10 at `selftest.py:2071`, the
  conv-pin arms, AC7 and AC9 of TOOL-aSurfacedLexicon-7): TOOL-dMindYourWords-1, which rewrites them
  with its code (§8 F5).
- Changing what any extractor returns for a Python definition, the frozen `(name, lineno)` pair
  included: TOOL-dTotalRecall-13 §3. The decorator context with aliases resolved is
  TOOL-dMindYourWords-12's; S2 reads decorators by their last segment, as `extract_decorators` does.
- The other non-names the design does not name (a nested closure, a test arm): ask TOOL-aProbedToolkit-5
  states them, and the class this unit sets is for the two shapes gap-lex-07 measured.
- Restoring the `--brief <path>` report TOOL-aSurfacedLexicon-3 deleted (`9eda72825`).

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `Offender.grade`, the field S2 sets to `not-a-name`, and the §4 pin sentence S5 and S6 state; without it S5 has no pin to agree on
- **hands-off** `TOOL-dMindYourWords-15` — `load_conf`, whose repeated-header refusal the `OUT_OF_SCOPE:` block inherits
- **hands-off** `TOOL-dMindYourWords-8` — `load_conf`, whose repeated-header refusal its packs block inherits
- **hands-off** `TOOL-dMindYourWords-10` — `load_conf`, whose repeated-header refusal its families and nouns blocks inherit
- **hands-off** `TOOL-dMindYourWords-3` — `load_conf`, whose repeated-header refusal its contracts block inherits
- **consumes-from** external — TOOL-dTotalRecall-13 S1 and S3, an ancestor build's, which moves the `js-regex` set into `tools/lib/extract_code.py` before this build run
- **consumes-from** `TOOL-dMindYourWords-27` — the ledger home `.lexicon-debt.txt`, where the three accessor rows are drained, in place of `memory/project/lexicon-debt.txt` (review id 45)
- **hands-off** `TOOL-dMindYourWords-29` — the IIFE edit's third copy and AC2's repeated-header case, which the minors batch repairs (review ids 3, 12)
- **hands-off** `TOOL-dMindYourWords-37` — the three accessor rows it drains, which the minors batch confirms are gone from the root home and from the old path (review id 6 of the audit of units 22 to 29)

## 4. Design

### Evidence

Read at `ba8b3c8c4`; no product file differs from base `ccd1292e`.

- `load_conf` opens a block when `_BLOCK_RE` matches a `BLOCK_KEYS` header and assigns
  `out[key] = _parse_block(…)` (`lexicon_conf.py:155`), so a second header overwrites the first. The
  live conf carries the defect: an empty `PINS:` at `.lexicon.conf:515` inside comment prose and the
  real one at `:579`. TOOL-dMindYourWords-1 S7 removes both, so no repeated header remains at this
  pass; S1 is the refusal for the next one.
- The three `@property` sites graded as verb offenders, from `python tools/lexicon/lexicon.py
  --offenders` at `ba8b3c8c4`: `has_block` (`tools/codebase-map/map_lib.py:1281`), `clean` (`:1398`)
  and `empty` (`tools/codebase-map/reuse_lookup.py:165`). PINNED at that sha.
- The IIFE: no live one remains (scout D: `holder` left `tools/hooks/agent-cap.js` with
  TOOL-dGroundRules-10), so the case is planted. A probe of the two patterns over the 34 tracked
  `.js` files at `ba8b3c8c4` yields the same 34 names under both, and over the planted
  `const holder = (() => {…})()` and `const k = (async () => { })()` the new one yields none.
- `main` returns 2 for every mode outside its seven (`lexicon.py:4359-4378`). `--brief` was a mode
  until `9eda72825` deleted it; nothing outside records documents `--brief` or `--help` (`git grep`).
- `extract_decorators` records a dotted decorator by its last segment, so `@x.setter` reads `setter`
  and `@functools.cached_property` reads `cached_property` (`:2541-2543`).

### The refusal

```python
opened: dict[str, int] = {}
...
if mb and mb.group(1) in BLOCK_KEYS:
    key = mb.group(1)
    if key in opened:
        raise ConfError(f"{p}:{i + 1}: duplicate block header {key!r}, first seen at line {opened[key]}")
    opened[key] = i + 1
```

`adopt-lexicon.sh --check` shells out to the same reader, so the refusal reaches the unguarded wiring
leg.

### The accessor decorators

`ACCESSOR_DECORATORS = ("property", "cached_property", "setter", "getter", "deleter")`, a module
constant beside `KINDS`. A definition whose site key `(path, lineno, name)` carries one is an
`Offender("P1 verb", …, grade="not-a-name")` with detail `accessor (@<decorator>), not a name`, so
`--list` names it and the class line counts it, and it enters no debt count (TOOL-dMindYourWords-1 S2).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `ACCESSOR_DECORATORS` | module constant, `lexicon.py` | `py.constant`, screaming |
| `render_usage` | function, `lexicon.py` | `py.function`, answered OK by `--suggest` at `ba8b3c8c4` |
| `duplicate block header` | refusal text, `lexicon_conf.py` | none |

### Migration

An adopter whose conf repeats a header reds at its next run, the message naming both lines; the remedy
is merging the two blocks by hand, since no step can tell which block was meant (§8 F1). The three
`@property` sites leave the debt ledger as drains, each printed with its row to delete.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1
- `tools/lexicon/lexicon.py`: S2, S4, the COST line, `KIT_LEXICON_VERSION`
- `tools/lib/extract_code.py`, `tools/lexicon/extract_code.py`, `tools/codebase-map/extract_code.py`:
  S3, the canonical block and its copies once TOOL-dTotalRecall-13 has landed
- `tools/lexicon/selftest.py`: the arms of §7 and H2
- `tools/lexicon/README.md`, `tools/lexicon/LEXICON.md`, `tools/lexicon/kit.toml`,
  `tools/lexicon/adopt-lexicon.sh`, `tools/lexicon/lexicon-verb-waivers.txt`,
  `tools/lexicon/lexicon-suffix-waivers.txt`, `.lexicon.conf`: S5
- `tools/lexicon/SKILL.template.md` and its render `.claude/skills/lexicon/SKILL.md`: S6
- `memory/project/lexicon-debt.txt`: the three accessor rows drained

### Alternatives rejected

- **Dropping `@property` definitions in `_python_defs`.** It changes what the extractor returns, which
  TOOL-dTotalRecall-13 §3 makes a non-goal and which the map and drift-audit read by position
  (`lexicon.py:2532-2540`). The grader mark reaches the same class and leaves the pair frozen.
- **Ending the arrow pattern's parameters at the first `)` followed by `=>`.** A lazy match still
  admits `(() =>` as a parameter list; the probe in §4 shows `\([^()]*\)` loses no live name.
- **Answering `--brief` with exit 2 and a pointer.** Lost to [fixes]: "remove … from the
  documentation, or answer them"; nothing documents them, so answering is the half left, and a
  refusal is what the 130 calls already met.

## 5. Production-readiness checklist

- security — N/A — no write path, input or surface widens; S1 refuses more, never less.
- perf / scale — S2 adds one `ast.parse` per armed Python file per run, the walk `extract_decorators`
  already makes for a decorator selector; the run's seconds print on the leg log.
- error / empty / loading states — a conf with no repeated header parses as before; a fixture with no
  accessor counts `not-a-name=0` on the class line.
- observability — the refusal names both lines; `--list` names each accessor with its decorator.
- risks — an adopter's conf with a repeated header reds on update; the message names both lines.
- testing — the arms of §7.
- migration — §4 "Migration".
- user docs — `tools/lexicon/README.md` and the Skill; no `help/` page covers the lexicon.

## 6. Acceptance criteria

- **AC1** — When `python lexicon_conf.py --print-rows CELLS` runs on a planted conf carrying `CELLS:`
  twice, it exits non-zero and prints `duplicate block header 'CELLS', first seen at line` with both
  line numbers; with the two blocks merged it exits 0.
  Red when: the second block silently replaces the first, the defect gap-lex-07 names.
- **AC2** — When `bash adopt-lexicon.sh --check` runs in a fixture whose conf repeats `VERBS:`, it
  exits 1 printing the same refusal; and `grep -cE '^(VERBS|CELLS|PINS|PATTERNS|CANON):'
  .lexicon.conf` prints at most one per key at the pass.
  Red when: the wiring leg's reader accepts the repeat, or this repository's conf still repeats one.
- **AC3** — When `python lexicon.py --list` runs on a fixture holding `@property def has_block(self)`,
  `@functools.cached_property def empty(self)` and `@x.setter def clean(self, v)`, each prints with
  grade `not-a-name`, the P1 offender count is 0, and the class line reads `not-a-name=3`.
  Red when: an accessor is graded on its leading token, as `has` is today.
- **AC4** — When the same fixture holds `def has_block(self)` with no decorator, `python lexicon.py`
  grades it a P1 offender; a camelCase `@property def hasBlock(self)` under `py.function  snake` is a
  convention violation.
  Red when: the mark exempts an undecorated definition, or exempts a property's case.
- **AC5** — When `python lexicon.py --list` runs on a fixture `.js` file holding `const holder = (() =>
  { return 1; })();`, it prints no definition named `holder`; the same file's `const f = (a, b) => a`
  is graded.
  Red when: the IIFE value is extracted as a function, the planted case gap-lex-07 names.
- **AC6** — When the 34 tracked `.js` files are extracted under `js-regex` at the pass, the names
  equal those the old pattern yields.
  Red when: the new pattern loses a live arrow definition.
  figure: DERIVED at the pass's base; 34 at `ba8b3c8c4`.
- **AC7** — When `python tools/lexicon/lexicon.py --help` runs, it prints the usage on stdout and exits
  0; `--brief` prints the usage and the line naming `--suggest`, and exits 0.
  Red when: either exits 2, the dead-mode defect.
- **AC8** — When `python tools/lexicon/lexicon.py --frobnicate` runs, it prints the usage on stderr and
  exits 2; `python scaffold_lexicon.py --help` in a fixture still refuses.
  Red when: an unknown mode exits 0, or the scaffold writes a file named `--help`.
- **AC9** — When `git grep -n -i -E "two-sided|equality in both directions" -- tools/lexicon
  .lexicon.conf .claude/skills/lexicon` runs at the pass, every line it prints is one of the nine
  git-diff senses §2 S5 lists.
  Red when: a carrier still states the pin as a two-sided equality.
- **AC10** — When `bash adopt-lexicon.sh --check` runs, the Skill render matches its template byte for
  byte; `grep -c "lexicon.pin" tools/lexicon/SKILL.template.md` prints at least 1; and the H2 arm
  asserts the pin sentence of TOOL-dMindYourWords-1 §4 where it asserted `"TWO-SIDED EQUALITY"`.
  Red when: the Skill and the README state different pins, or the render drifts from its template.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `check-wiring self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `drift-audit selftest` · `govkit acceptance matrix` · `policy fixtures` · `straggler-guard arms` · `recall floor` · `recall floor arms` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 · beside the conf-refusal table (`selftest.py:1842-1860`), a planted conf repeating `CELLS:` and one repeating `VERBS:` through `adopt-lexicon.sh --check`, its failing case the repeat accepted · none

New arm: tools/lexicon/selftest.py · covers AC3 AC4 AC5 AC7 AC8 · planted accessor and IIFE fixtures and the two dead modes, its failing cases `has_block` graded on `has`, `holder` extracted, and `--help` exiting 2 · none

New arm: tools/lexicon/selftest.py · covers AC10 · arm H2 rewritten to assert the pin sentence in the template, its failing case the template restating a two-sided equality · none

## 8. Open questions

- **F1 — Does a repeated header refuse at once, or warn through a window?** Options: (a) refuse, naming
  both lines; (b) warn until a window closes, as P38 asks of an adopter-visible surface. A conf that
  repeats a header never meant what it says, since the earlier block was dropped silently, so no
  working behaviour exists to keep. RESOLVED (agent, 2026-10-29, delegated): (a), rung 1: the clause
  says "repeated block headers refused". widens: none · relaxes: none
- **F2 — Does `not-a-name` cover a property's case convention too?** Options: (a) the verb predicate
  only, the `CELLS` row still grading the name's case; (b) both. gap-lex-07's defect is non-names
  "graded as verbs", and a property's name has a case its readers type. RESOLVED (agent, 2026-10-29,
  delegated): (a), rung 1 (gap-register:262). widens: none · relaxes: none
- **F3 — Where does the property fix sit?** Options: (a) a grader mark through `extract_decorators`;
  (b) in the extractor, as the lexicon review's `[classes]` row says (lexicon review:217). (b) changes what
  the extractor returns, which TOOL-dTotalRecall-13 §3 makes a non-goal and two readers unpack by
  position. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3; the clause says only "properties
  ungraded", so v2 is met either way. widens: none · relaxes: none
- **F4 — What does `--brief` answer, and with what exit?** Options: (a) the usage plus the line naming
  `--suggest`, exit 0; (b) the same with exit 2; (c) the deleted per-file report restored. (c)
  reopens TOOL-aSurfacedLexicon-3's deletion and (b) is the defect. RESOLVED (agent, 2026-10-29,
  delegated): (a), rung 1: [fixes] "or answer them" (lexicon review:464). widens: none · relaxes: none
- **F5 — Which unit rewrites the selftest arms that assert two-sided pins?** Options: (a) each arm with
  its subject: the arms grading the pin's behaviour (AC10, the conv-pin and vocab-row arms) with
  TOOL-dMindYourWords-1's code, and H2, a wording arm, here; (b) all of them here, as the spec brief's
  row for this unit words it. Under (b) the pass that changes the pin leaves its own arms red until
  this one. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Items 14, the lexicon review's `[current]`
  defects and `[fixes]`, review M17, research-lexicon-kit's mode table, scout D's row 1, its two-sided
  list and its parent disagreement, and the spec brief's I8.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-27, TOOL-dMindYourWords-29); no scope, design or criterion moved.
- rev-3 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 22 to 29
  declare toward this unit (TOOL-dMindYourWords-37); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are `load_conf`'s block loop (`tools/lexicon/lexicon_conf.py:139-157`) with
`_parse_rows`' refusal shape (`:198-200`), `extract_decorators` (`tools/lexicon/lexicon.py:2527`) for
the accessor mark, the `js-regex` set (`lexicon.py:146`, the `extract_code` block at the build run),
and `main`'s usage block (`:4356-4378`) with the `tools/memory-tree/backlog.py:2312` precedent. `python
tools/codebase-map/reuse_lookup.py "refuse a repeated block header in a conf file reader"` ranked
`load_conf` (eleven definitions, the lexicon's among them), `parse_conf` and `ConfError`; none refuses a
repeated header, so the refusal is new inside the seam the lookup named. Scout D's row 1 holds against
source at `ba8b3c8c4`, with one correction: the usage block and its exit are `:4359-4378`. Scout D's
two-sided list is replaced by the grep S5 runs at the pass, because TOOL-dMindYourWords-1 rewrites
seven of its lines first. The recall probe surfaced research-lexicon-kit's mode table ("Neither mode
exists any more"), which `git log -S` confirmed at `9eda72825`.

Recall terms used: `python tools/memory-recall/query.py "lexicon conf repeated block header property IIFE dead modes brief help" --terms "lexicon_conf load_conf repeated block header PINS property IIFE js-regex --brief --help two-sided wording"`
