# TOOL-dGroundRules-8 — the reader-coverage arm: a key whose Owner build has landed has a reader

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dGroundRules-12

**Carries:** cl-dClosedLoop-0014@28a178b1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 |
| [2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-1 TOOL-dGroundRules-11 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-10 TOOL-dGroundRules-9 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

A catalogue key whose Owner build has landed but which no code consumes is a setting the owner can
change to no effect. This unit adds one arm that is red on such a key: its population is the catalogue's
`owner` field joined to the builds landed on the default branch, read from history, and a reader is a
call site that consumes the key's value, never the policy reader's own default path (H4, DA-M1).

## 2. Scope (IN)

- **S1** — The landed-owner set: a build counts as landed when, at the landed revision, its build
  folder holds at least one spec and every spec there carries a terminal status (§4 "Landed", §8 F1).
  Observed by AC1, AC2 and AC5.
- **S2** — The reader scan: the call shapes of §4 "Readers" over the tracked code of the tree under
  test, with the exclusions §4 names, pattern keys included. Observed by AC3, AC4 and AC6.
- **S3** — The arm `reader-coverage` in `tools/policy/check_policy.py`, a function
  `check_reader_coverage(repo, landed=None)` that reports one finding per landed-owner key with no
  reader and always prints its summary line, the empty population announced. Observed by AC1, AC7 and
  AC8.
- **S4** — The `--fixture reader-coverage` cases planting each red and green case of AC1 to AC6 in a
  temporary repository. Observed by AC1.
- **S5** — A section on the arm in `help/policy.md`: what reds it and the two remedies, a reader or a
  catalogue owner that has not landed. NOT OBSERVED — prose, read by the closing review; no command
  observes a help page's content.

## 3. Non-goals (OUT)

- Building a reader for any key. Each key's reader is its Owner build's; this build's own five keys
  are units 4, 9 and 10's.
- A landed-builds record of its own. The landed set is read from the default branch each run, never
  written down (the charter's `[derive]`).
- Grading whether a reader honours the value correctly. The arm sees a consuming call site, not its
  behaviour.
- The catalogue's `owner` field and its values: unit 1's.
- Readers in a language outside Python, shell and JavaScript (§4 "What it does not check").

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — `tools/policy/catalogue.toml` with each key's `owner` field,
  and `tools/policy/check_policy.py` with its `--fixture` mode and its merge-bar leg; without them the
  arm has no population and no home
- **consumes-from** `TOOL-dGroundRules-2` — the landed-revision resolution `resolve` uses for
  `rev=None`, and the CLI shape `policy.py get <key>` the reader scan matches; without the first the
  landed set would be read from the working tree
- **hands-off** `TOOL-dGroundRules-20` — `tree_lib.py`, which its cases read, named in the `policy fixtures` guard (finding 35)
- **hands-off** `TOOL-dGroundRules-21` — `tree_lib` reached through `resolve_kit_dir` and `requires`, the quoted pattern segment, the relocated-install case, the announced empty population and the regenerated codebase map (findings 6, 7, 16, 51, 40)

## 4. Design

### Landed

`landed_owners(repo) -> set[str]`: resolve the landed revision through unit 2's resolution; read the
memory root from `.memory-tree.conf` at that revision; for each distinct catalogue `owner`, list
`<memory root>/builds/<owner>/spec/` at that revision (`git ls-tree -r --name-only`), read every spec
there in one `read_blobs_at` call, and parse each status header with `HDR_RE`. The owner is landed when
at least one spec parses and every one carries a token in `TERMINAL`. `HDR_RE`, `TERMINAL`,
`read_blobs_at` and `parse_conf` are imported from `tree_lib` in the memory-tree kit beside the policy
kit (`tools/memory-tree/tree_lib.py:31`, `tools/memory-tree/tree_lib.py:328`,
`tools/memory-tree/tree_lib.py:376`), the one status vocabulary and blob reader this corpus has. An
`ImportError` alone, where no memory-tree kit is installed, reads no build as landed and prints
`reader coverage: no memory-tree kit beside the policy kit, so no build reads as landed`.

The rule is the schedule instrument's "build done" (`tree_state`,
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py:116`), read here
without its clause-coverage half, and the instrument is cited, never imported. A build whose spec run
landed with its units `DEFERRED`, as this build's README rule 1 has every chain build do, is not landed
(§8 F1).

`landed=None` derives the set; a passed set replaces it, which is how a probe asks "what would this arm
say once that build lands" (AC8). The bar's leg always passes `None`.

### Readers

A reader of key `K` is a match, in a scanned file, of one of two shapes, held in one table in the
arm so a new consumer shape is one row:

| Shape | Files | Pattern |
|---|---|---|
| a call whose first argument is `K` as a string literal | `.py`, `.js`, `.mjs`, `.cjs` | an identifier, `(`, optional space, an optional string prefix of up to two letters from `fFrRbB`, a quote (`'`, `"` or a backtick), `K`, the same quote |
| the reader CLI's `get` | `.sh`, and every file under `.githooks/` | `policy.py`, an optional closing quote, space, `get`, space, `K` optionally quoted, then space, `;`, `)`, a pipe, `&` or end of line |

The first shape covers the Python API's `resolve("<key>")` and a JavaScript call on the mirror helper
unit 5 writes, `tools/policy/policy-mirror.js`, whatever that helper names its function.

**Scanned files** are `git ls-files` of the tree under test, read from disk, with the suffixes above or
under `.githooks/`, minus: anything under the memory root or `help/`; a `*.test.sh`, `*.test.js`,
`selftest*.py` or `test_*.py`; and `tools/policy/check_policy.py`, whose fixtures name keys without
consuming them. A line whose first non-space characters are `#` or `//` is a comment and never matches.

**Never this reader's own default path.** The policy reader resolves every key by iterating the
catalogue, and the mirror writer does the same; neither names a key literally, so neither matches.
`.governance/policy.toml`, `.governance/policy.json` and the catalogue are not scanned files. A literal
read of one key inside `tools/policy/policy.py`, such as the invalid-file branch reading
`policy-file.on-invalid`, is a call site consuming that key and counts.

**Pattern keys.** A catalogue key holding a `*` segment or a `<name>` segment, such as `budgets.*` or
`roles.effort.<role>`, matches with each such segment read as one run of characters that are not a
quote, a space, a `.`, `(` or `)`. That admits an interpolated name (`"budgets.$cap"`,
`f"budgets.{cap}"`, `budgets.${cap}`). A match spelling another catalogue key exactly, such as
`budgets.enforce`, reads that key and never the pattern key.

### The arm

`check_reader_coverage(repo, landed=None) -> tuple[int, list[str]]` returns the count of keys graded
and one finding per graded key with no reader:
`reader coverage: <key> (owner <slug>, landed at <rev8>) has no reader`. The leg prints the findings
and then, on every run, `reader coverage: graded <n> of <m> catalogue key(s); landed owners: <slugs or
none>`, and with `n` zero, `reader coverage: graded 0, so this arm checked nothing at <rev8>`. A finding
exits the leg 1.

`--fixture reader-coverage` builds a temporary repository under the system temp directory with a short
name, never inside the worktree: a copy of the policy kit with a catalogue holding the planted key
`fixture.planted`, a build folder per planted owner with one conforming spec, and one bare remote whose
default branch carries the landed state. Each case of AC1 to AC6 prints `case <name>: red|green`.

### What it does not check

A reader in another language, or one reading a key through a name built at run time from parts that
spell no key segment, is not seen, and its key reads unread: a false red that names itself. A matched
call that names a key without consuming its value, such as a message, reads as a reader: a false
green the shapes keep narrow. A build that lands partially, deferring units, does not read as landed
until its last unit closes.

### Files touched (estimate)

- `tools/policy/check_policy.py` (the arm, `landed_owners`, the reader scan, the fixture cases)
- `help/policy.md` (this arm's section; the page is unit 1's where unit 1 wrote it, else created here
  holding only this section)

### Alternatives rejected

- A registry where each consumer declares the keys it reads: a typed list beside the code it describes,
  against the charter's `[derive]`, and it cannot tell a declared read from a real one.
- Any literal of the key in code counting as a reader: a key named in a message or a docstring would
  read as consumed, a silent false green (§8 F2).

## 5. Production-readiness checklist

- security — read-only: the arm runs `git` read commands and reads files; it executes nothing it reads.
- perf / scale — one `git ls-files`, one blob batch per run, and one regex pass per scanned file over a
  few hundred files; seconds at most.
- error / empty / loading states — the empty population is announced on every run; an unreadable
  landed revision is unit 2's refusal passed through, never read as "no build landed".
- observability — each finding names the key, its owner and the revision; the summary line names the
  landed owners.
- risks — at this build's own landing its five keys enter the population, and any of them without a
  reader in a matched shape reds the next push; AC8 observes that before the landing.
- testing — the `reader-coverage` fixture cases (AC1 to AC6) and the real-tree probes (AC7, AC8).
- migration — none; the arm is new and grades nothing until a catalogue Owner build lands.
- user docs — `help/policy.md`'s section (S5).

## 6. Acceptance criteria

- **AC1** — When `python check_policy.py --fixture reader-coverage` runs, case
  `landed-no-reader` (key `fixture.planted`, owner `bPlanted`, whose one spec is `CLOSED` at the
  landed revision, and no consumer) prints `red` with the finding naming `fixture.planted` and
  `bPlanted`. Red when: the population is read without the landed join, or the arm reports nothing on
  a key with no reader.
- **AC2** — When `python check_policy.py --fixture reader-coverage` runs, case `unlanded`
  (the same key, its owner's spec `OPEN` at the landed revision) and case `no-build` (owner `bAbsent`,
  no build folder) each print `green` with the key not graded. Red when: an unlanded owner's key is
  graded.
- **AC3** — When `python check_policy.py --fixture reader-coverage` runs, cases
  `reader-python` (`resolve("fixture.planted")` in a `.py` file), `reader-cli`
  (`python policy.py get fixture.planted` in a `.sh` file) and `reader-js`
  (`mirror.get('fixture.planted')` in a `.js` file), each with owner `bPlanted` landed, print `green`.
  Red when: a shape of §4's table does not match its own planted call.
- **AC4** — When `python check_policy.py --fixture reader-coverage` runs, case
  `not-a-reader` (owner landed; `fixture.planted` named only in a `.md` file, a `*.test.sh`, a comment
  line of a `.py` file, the arm's own module, the generated JSON mirror and the catalogue) prints `red`. Red when: a mention, a test, the mirror or the reader's own default path reads as a
  reader.
- **AC5** — When `python check_policy.py --fixture reader-coverage` runs, case
  `history-not-tree` (owner's spec `CLOSED` at the landed revision and edited to `OPEN` in the
  working tree, no consumer) prints `red`, and case `tree-not-history` (`OPEN` landed, `CLOSED` in the
  working tree only) prints `green`. Red when: the landed set is read from the working tree.
- **AC6** — When `python check_policy.py --fixture reader-coverage` runs, case
  `pattern-read` (catalogue key `fixture.*` with owner landed, and `policy.py get "fixture.$name"` in a
  `.sh` file) prints `green`, and case `pattern-only-sibling` (the only call names the catalogue key
  `fixture.exact`) prints `red` for `fixture.*`. Red when: interpolated segments do not match, or an
  exact sibling key's read counts for the pattern.
- **AC7** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; print(c.check_reader_coverage('.'))"`
  runs on the built tree before this build lands, it prints a graded count of 0 and no finding, and the
  leg's run prints the `graded 0` announce line. Red when: the empty population passes with no line
  saying so.
  figure: DERIVED at observation; 0 while no catalogue Owner build is landed on the default branch.
- **AC8** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; print(c.check_reader_coverage('.', landed={'dGroundRules'}))"`
  runs on the built tree, it grades the five keys this build owns, `policy-file.on-invalid`,
  `runtime.agents-in-flight`, `budgets.*`, `budgets.enforce` and `budgets.pinned`, and reports no
  finding. Red when: one of them has no reader in a matched shape, which would red the first push after
  this build lands.
  fixture: the real tree with units 4, 9 and 10 built; a unit-8 pass observes it for
  `policy-file.on-invalid` alone, and the main loop observes all five at the close.

## 7. Gates

`govkit selfcheck` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `kit epoch (shipped bytes move, the version moves)`

The leg that runs `tools/policy/check_policy.py` on the bar is unit 1's and is not in the manifest at
this spec's base, so it is named here in prose only; this unit's arm joins it.

New arm: tools/policy/check_policy.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the `--fixture reader-coverage` mode plants each case in a temporary repository · none

## 8. Open questions

- **F1 — What makes an Owner build "landed"?** (a) At the landed revision, every spec in the build's
  folder is terminal, with at least one. (b) A first-parent merge on the default branch whose subject
  names the slug. (c) Its run record at `LANDED` or a `RUN.LANDED.*` archive, as
  `check_build_landed` reads it (`tools/branch-reconcile/branch_reconcile.py:542`). A chain build lands
  twice: its spec run lands its specs `DEFERRED` (this build's README rule 1), and its build run lands
  them `CLOSED`. (b) and (c) read the first landing as landed, so every chain build's keys would red the
  bar from its spec run until its build run, the red-at-own-landing the design audit's M1 found
  (`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md:120`). (a)
  reads the default branch's committed state, which is history, and reads the second landing only.
  RESOLVED (agent, 2026-10-23, delegated): (a), by rung 3 of the execution plan's fork rungs: the only
  option meeting AC2 for a spec-run-landed owner.
- **F2 — What is a reader?** (a) The call shapes of §4. (b) Any string literal of the key in code. (c)
  A registry each consumer declares its reads in. (c) is typed, against the clause's "derived". (b)
  counts a message or a docstring as a reader, a silent false green; (a) misses an exotic call, a false
  red that names the key and its remedy. RESOLVED (agent, 2026-10-23, delegated): (a), by rung 3, with
  the shapes held in one table so a new consumer shape is one row.
- **F3 — Does the reader module itself count?** The clause excludes "this reader's own default path",
  and `policy-file.on-invalid` is consumed inside the reader. Options: (a) exclude
  `tools/policy/policy.py` wholly; (b) scan it like any file, the generic default path matching nothing
  because it names no key. (a) leaves `policy-file.on-invalid` readerless at this build's landing,
  failing AC8. RESOLVED (agent, 2026-10-23, delegated): (b), by rung 3.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft. The spec brief asks for a `DRAFT` status token; the header carries
  `OPEN`, the template's drafting token, because hygiene check 12 parses only the seven-token vocabulary
  (`tools/memory-tree/check-memory-hygiene.sh:1930`).
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-20, TOOL-dGroundRules-21 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit's findings that repair this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 10. Reuse audit

The seams this unit extends are the policy kit's `tools/policy/check_policy.py` arm table and catalogue
(unit 1) and the landed-revision resolution (unit 2); the landed predicate reuses
`tools/memory-tree/tree_lib.py` (`HDR_RE`, `TERMINAL`, `read_blobs_at`, `parse_conf`) rather than a
second status grammar. `reuse_lookup.py` with "find call sites that consume a named configuration key"
ranked `read_conf_key` (`tools/roles/roles_lib.py`, `tools/check-spec-tokens.py`) and `readConfKey`
(`tools/hooks/scratch-guard.js`): each reads one key's value, and none finds the call sites of a key,
so no existing seam fits the scan. `reuse_lookup.py` with "which builds have landed on the default
branch, derived from git history" ranked generic `git` and `build_*` helpers and no landed-build
predicate; reading source found `check_build_landed` in `tools/branch-reconcile/branch_reconcile.py:542`,
rejected as §8 F1 records. The recall query's hits agreed with source: the design audit's M1 fix is the
clause's text, and the runtime fold's "assert the population is non-empty" became the announce line,
since today's population is empty by the landed rule.

Recall terms used: `python tools/memory-recall/query.py "an arm red when a policy key whose owner build
has landed has no reader call site" --terms "reader coverage owner build landed catalogue key consumer
call site default path arm red history"`
