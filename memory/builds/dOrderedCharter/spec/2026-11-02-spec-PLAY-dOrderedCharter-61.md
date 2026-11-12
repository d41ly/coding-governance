# PLAY-dOrderedCharter-61 — the layer check reads an edge only where a path names a file a non-core kit ships, and never from a word inside a string

**Status:** CLOSED · rev-1 · 2026-11-02 · node d · Tier-2 · base 8bec4cef · streams playbook · order 3 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 |
| [2026-11-02-build-PLAY-dOrderedCharter-61-1-builder-return.md](../build/2026-11-02-build-PLAY-dOrderedCharter-61-1-builder-return.md) | journal | — |
| [2026-11-02-build-PLAY-dOrderedCharter-61-ledger.md](../build/2026-11-02-build-PLAY-dOrderedCharter-61-ledger.md) | journal | — |
| [2026-11-03-build-PLAY-dOrderedCharter-17-midbuild-lint.md](../build/2026-11-03-build-PLAY-dOrderedCharter-17-midbuild-lint.md) | journal | PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-62 |
| [2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md](../build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 |
| [2026-11-02-prompt-PLAY-dOrderedCharter-61-1-spec-writer.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-61-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-PLAY-dOrderedCharter-61-build-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-61-build-brief.md) | journal | — |
| [2026-11-02-prompt-PLAY-dOrderedCharter-61-spec-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-61-spec-brief.md) | research | PLAY-dOrderedCharter-17 |
| [2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md](../reviews/2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md) | diff-review | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 |

<!-- /gen:spec-records -->

## 1. Goal

PLAY-dOrderedCharter-16's `tools/playbook/check_layers.py` reports 60 red edges over the tree at
`20d02c59c`, and 21 of them are no dependency: a journal path under the git directory, an id shaped
like a path, the check's own read of the core kits' descriptors, and a kit's name inside a message
that spans two lines. This unit repairs the check with two class rules, so the leg reports only real
dependencies of a core file on a non-core kit. It decides how a core kit's test suite and a whole-tree
resolver are dispositioned, and it lands the guard unit 16 owes, so PLAY-dOrderedCharter-17 cures a
population that is real.

## 2. Scope (IN)

- **S1** — The path rule. A path the check reads as naming a non-core home, `<home>/<rest>`, is an
  edge only when `<rest>` names a file the tree tracks under that home, or a directory or glob that
  matches one, and at least one such file is not owned by a core kit. A core kit owns its descriptor
  and the files that descriptor ships. An empty `<rest>`, or one that starts with a variable, names
  the home itself and stays an edge. The rule binds every reader of a spelled path: the slash-joined
  literal, the path of a `dynamic` load and the source of a `copy`, and a bare home name handed to a
  Python call, read together with the call's later constant arguments. Observed by AC1, AC2 and AC4.
- **S2** — The string rule. The shell line scan reads a bare home word from each line's code as
  `scan_shell_lines` (`tools/memory-tree/check-arms.py:305`) yields it: quoted spans, comments and
  here-document bodies blanked, with the quoting state carried across lines, and a command
  substitution inside double quotes read as code. A script whose quoting does not balance is read
  with unit 16's same-line reading and named on one `layers:` line. Observed by AC1, AC2 and AC3.
- **S3** — What the check does not read, said. The not-read line at `check_layers.py:88`, the
  module docstring (`:14-26`) and the layer section of `tools/playbook/README.md` (`:146-181`) each
  say that a path naming no file the kit ships, and a bare kit name inside a string or a here-document,
  is not an edge. Observed by AC6.
- **S4** — Two fixture plants, `quoted` and `unshipped`, in `check_layers.py --fixture` and as rows
  of the plant table in `tools/playbook/adopt-playbook.sh:200-215`. Observed by AC3 and AC4.
- **S5** — Unit 16's owed guard. The `playbook render selftest` leg's guard in
  `tools/gate-legs.json:1728-1730` names `{prefix}/memory-tree/import_walk.py`, and with S2 also
  `{prefix}/memory-tree/check-arms.py` and `{prefix}/memory-tree/tree_lib.py`, which `check-arms.py`
  imports (`:175-176`). The kickoff manifest's `last-audit` stamp is re-stamped in the same commit,
  since `tools/gate-legs.json` is on its `watch:` list (`memory/guides/SESSION-KICKOFF.md:6`). Observed
  by AC5.
- **S6** — The disposition of a core kit's test suite and of a whole-tree resolver, decided in §8 F1:
  each is graded like any other core file and cured by an `optional` row with a named fallback.
  NOT OBSERVED here: the check does not change for it, and PLAY-dOrderedCharter-17's AC1 observes
  the rows.

## 3. Non-goals (OUT)

- Curing any edge the repaired check still reports: PLAY-dOrderedCharter-17's.
- A new edge kind, a new register key, or a per-target `optional` row. A row still allows every edge
  of the file it names as `part` (`check_layers.py:280-282`), as unit 16 built it.
- Data-flow analysis. A placeholder path that is only written into a settings file, such as
  `tools/settings-merge.py:620`, cannot be told by a static rule from one that is read, such as
  `tools/policy/check_policy.py:1041`; it stays an edge (§10).
- Changing `scan_shell_lines` or any reader of it.
- Unit 16's spec, which is CLOSED and stays frozen.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-16` — `tools/playbook/check_layers.py`, its fixture and plant table, and `tools/memory-tree/import_walk.py`; without them there is no check to repair
- **hands-off** `PLAY-dOrderedCharter-17` — the 40 edges the repaired check reports, each made an `optional` row with a named fallback, the test suites and whole-tree resolvers included by §8 F1
- **hands-off** `PLAY-dOrderedCharter-62` — the repaired `tools/playbook/check_layers.py`, its fixture and `adopt-playbook.sh`'s plant table, which that unit's plants read an edge through

## 4. Design

### The two rules in the check

Both change `derive_edges` (`check_layers.py:165-283`) and nothing else in the edge reading.

- **S1.** The `seg` pattern (`:187`) captures the path text after `<home>/` up to the first
  character no path holds. `derive_named_homes` (`:197-198`) keeps a match only when
  `check_far_path(home, rest)` answers true. That function matches `<tool root>/<home>/<rest>` against
  the tracked files with `fnmatch.fnmatchcase`, or as a directory prefix, and answers true when a hit
  is not in the core-owned set: every core kit's `path` and `files` from `read_descriptors`
  (`:115-155`). `derive_edges` gains a `tracked` argument, passed from `check_layers` (`:343`, `:372`),
  its only caller. The bare-name reader of a Python call (`:253-257`) joins the constant string
  arguments that follow the home name with `/` and asks the same question; a bare name bound to a
  name has an empty rest.
- **S2.** `check_layers.py` loads `check-arms.py` from the memory-tree directory it already resolves
  for `import_walk` (`:81`), through `importlib.util.spec_from_file_location`, as `govkit.py:2890`
  and `tools/push-main.test.sh:1413` load it. The shell scan (`:263-277`) calls
  `scan_shell_lines` once per file and reads the `bare` pattern (`:195`) over each line's code in
  place of the same-line `unquoted` text (`:272`). The `seg`, `resolve_kit_dir` and `cp` readers keep
  reading the raw line, so a quoted path is still read. A file for which `scan_shell_lines` returns
  a trailing `None` is still read, with unit 16's same-line reading, and the run
  prints `layers: <file> read line by line: its quoting does not balance`.

### Measured: the class rules over the real tree

The candidate, a scratch copy of `derive_edges` carrying both rules and run with `--list` over the
tree at `20d02c59c` on 2026-11-02, PINNED as measured then:

| Reading | Edges | Removed | Added |
|---|---|---|---|
| unit 16 as built | 60 | — | — |
| S1 alone | 44 | 16 | 0 |
| S2 alone | 56 | 5 | 1 |
| S1 and S2 | 40 | 21 | 1 |

No core shell file returned an unbalanced scan. The 21 sites the two rules remove, each read at HEAD:

| Rule | Site | What the line spells |
|---|---|---|
| S1 | `.githooks/pre-push.test.sh:2279`, `:2281`, `:2573`, `:2584` | a runlog journal under the git directory, which `:2237` reads with `git rev-parse --git-dir` |
| S1 | `.githooks/pre_push_bar_selftest.py:180` | `os.path.join(self.work, ".git", "runlog", "pushes.log")` |
| S1 | `skills/session-kickoff/manifest-check.test.sh:1918` | a runlog journal under a clone's git directory |
| S1 | `tools/unattended/unattended.sh:12194` | the codebase-map lookup journal under the git common directory, found at `:12192` |
| S1 | `tools/unattended/unattended.test.sh:1540`, `:1558`, `:16434` | the same lookup journal, and the runlog push journal under the common directory |
| S1 | `tools/push-main.test.sh:1270`, `:1286`, `:1464`, `:1582` | a planted upgrade step's id, govkit/planted-witness-fails |
| S1 | `tools/playbook/check_layers.py:118`, `:129` | the govkit entries glob, which matches only core kits' descriptors |
| S2 | `tools/memory-tree/check-memory-hygiene.sh:1288` | a `fail 6` message whose quote closes on `:1289` |
| S2 | `tools/push-main.test.sh:1550`, `:1553`, `:1555`, `:1556` | lines of an expected-output string opened on `:1546` |

S2 also finds one edge unit 16 missed: `tools/check-wiring.sh:1101`, a bare `memory-recall` handed
to `resolve_receipt_path` in a command substitution inside double quotes.

### What remains, for PLAY-dOrderedCharter-17

40 edges: 24 in product files, 14 in `*.test.sh` suites, and 2 in the in-file selftest of
`tools/settings-merge.py` (`_selftest`, `:548`). Every site spec 17's §4 table names still reports,
at its HEAD line, except `tools/unattended/unattended.sh:12194`, whose journal read S1 removes; that
read already skips when the project declares no `MAP_CLI` (`:12185-12189`).

### Inventory

Minted: the function `check_far_path`; the plants `quoted` and `unshipped`; the line
`layers: <file> read line by line: its quoting does not balance`. Naming cells: the function is
checked with `python tools/lexicon/lexicon.py --suggest check_far_path --as py.function` at the pass.

### Rollout

Live at landing. The leg stays red over the tree until PLAY-dOrderedCharter-17's pass, as unit 16
§8 F3 decided, with 40 edges where it had 60.

### Files touched (estimate)

- `tools/playbook/check_layers.py`
- `tools/playbook/adopt-playbook.sh`
- `tools/playbook/README.md`
- `tools/gate-legs.json`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/symbols.json` (regenerated for the new function)

### Alternatives rejected

- **A list of the 21 sites as exemptions.** It gates the instance and not the class (charter
  `[class]`), and the next journal path or id under a kit's name is red again.
- **Strip git-directory paths by spelling.** `pre-push.test.sh:2279` reaches the git directory
  through a variable, which no spelling reveals; S1 needs no spelling, since it asks what the path names.
- **Lift `scan_shell_lines` into `import_walk.py`.** It changes `check-arms.py`, the harness
  meta-gate every adopter runs, for no reader that the load in S2 does not already serve.
- **A second shell lexer inside `check_layers.py`.** A copy of a kind at its second instance
  (charter `[reuse]`); `scan_shell_lines` already handles here-documents, `$'...'` strings and
  double quotes nested in a command substitution inside double quotes.

## 5. Production-readiness checklist

- security: read-only over the tree; no new write path.
- perf / scale: one `scan_shell_lines` pass per core shell file, and one `fnmatch` over the tracked list per spelled path; measured at the pass against the leg's `ceiling` of 120 (`tools/gate-legs.json:1822`).
- error / empty / loading states: an unbalanced script is read the old way and named, never skipped; an unreadable register still exits 2.
- observability: the not-read line names both rules on every run, and the summary counts are unchanged in shape.
- risks: S1 drops a path to a file a non-core kit writes but does not ship, untracked in its home; the not-read line says so, and the tree holds no such read today.
- testing: AC1 to AC6, and the arms of §7.
- migration: none; the leg is gov's own and an adopter receives `check_layers.py` with the playbook-render kit, its output narrower.
- user docs: `tools/playbook/README.md`, the layer section (S3).

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/check_layers.py --list` runs after the pass, its summary
  reads `40 red` and no `layers: edge` line names any of the 21 sites of §4's table.
  Red when: a journal path, an id, a core descriptor read or a word in a continued string still
  reads as an edge.
  figure: 40 is PINNED, measured at `20d02c59c` on 2026-11-02; AC2 re-derives it at the pass.
- **AC2** — When the builder saves the `layers: edge` lines of `check_layers.py --list` before the
  first edit and again after the pass, `diff` of the two removes exactly the 21 sites of §4's table
  and adds exactly `tools/check-wiring.sh:1101`.
  Red when: an edge outside the table disappears, which would be a real dependency silenced.
- **AC3** — When `python tools/playbook/check_layers.py --fixture --plant quoted` runs, it exits 1
  with `0 allowed, 1 red`, the red naming the fixture `run.sh` line holding a bare `expkit` in a
  command substitution inside double quotes, and none naming the line where a message naming
  `expkit` opens a quote it closes on the next line.
  Red when: a word inside a continued string is an edge, or a command substitution inside quotes is
  no longer read.
- **AC4** — When `python tools/playbook/check_layers.py --fixture --plant unshipped` runs, it exits 1
  with `0 allowed, 1 red`, the red naming the `core.py` line spelling "mapkit/reader.py", and none
  naming the lines spelling `os.path.join(root, ".git", "mapkit", "journal.log")` or the id
  "mapkit/planted-id".
  Red when: a path naming no shipped file is an edge, or a path naming one is not.
- **AC5** — When `python -c "import json; print([l['guard'] for l in json.load(open('tools/gate-legs.json', encoding='utf-8')) if l['name'] == 'playbook render selftest'])"`
  runs, it prints `{prefix}/playbook/`, `{prefix}/memory-tree/import_walk.py`,
  `{prefix}/memory-tree/check-arms.py` and `{prefix}/memory-tree/tree_lib.py`; and
  `git show --stat HEAD -- memory/guides/SESSION-KICKOFF.md` on the pass commit names the manifest.
  Red when: a file `check_layers.py` reads at run time is missing from the guard.
- **AC6** — When `python tools/playbook/check_layers.py` runs, its `layers: not read:` line names a
  path naming no file the kit ships and a bare kit name inside a string or a here-document, and
  `grep -n "names no file the kit ships" tools/playbook/README.md` prints the layer section's line.
  Red when: either rule narrows what the check reads and nothing says so.

## 7. Gates

`layer dependencies (the core never depends on an expansion)` · `playbook render selftest` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/playbook/adopt-playbook.sh · covers AC3 AC4 · the plant table's `quoted` and `unshipped` rows, each asserting its exit, its one red line and `0 allowed, 1 red`, red against unit 16's `derive_edges` · none
New arm: tools/playbook/check_layers.py · covers AC1 AC2 · the layer leg over the tree, its failing case staged by restoring unit 16's `derive_edges`, which reports the 21 sites again · none

## 8. Open questions

- **F1 — How a core kit's test suite, and a whole-tree resolver, is dispositioned.** Fourteen
  edges sit in `*.test.sh` suites of core kits, two in the in-file selftest of
  `tools/settings-merge.py`, and nine in the whole-tree resolvers `tools/check-kit-versions.sh:243-252`
  and `tools/check-wiring.sh:700`, `:1101`, `:1103`. Options: (A) a test class the register declares
  by file pattern, whose edges the check prints and never reds; (B) an `optional` row per file, the
  descriptor key unit 16 built, whose fallback is the file's own degraded branch, a suite's arm
  skipping with a line that names the kit absent and counting its assertions, as
  `tools/unattended/unattended.test.sh:13443-13446` already does; (C) withholding the suites from
  adopters with `role = "project-owned"`, so they leave the check's population. The test that
  decides (M12), written before it ran: A loses if any edge it would grade green is a hard failure
  of a file the kit ships. Run over the repaired tree, three are:
  `tools/check-wiring.test.sh:280`, `tools/memory-tree/check-memory-hygiene.test.sh:260` and
  `tools/unattended/unattended.test.sh:1972` each `exit 2` when the kit does not resolve, in a suite
  its kit ships (`check_layers.py:127-150` reads shipped files only). A passes an unconditional read
  of an optional component, which unit 16's AC5 names as its red, and reads an exemption as coverage
  (charter `[gate]`): veto 1. C changes what installs at every adopter: veto 2, so it is parked, not
  taken. B survives, reuses unit 16's seam, and adds no key. A whole-tree resolver takes B on its
  existing branch: `check-wiring.sh:1103` prints `skip recall`, and `check-kit-versions.sh` reds a
  missing kit as MISSING by name (`:26-30`), the seed its entry's `kit-versions-need-list` hole has
  the target edit down. RESOLVED (agent, 2026-11-02, delegated): B, by M3 rung 1 after vetoes 1 and
  2, by `2026-11-02-prompt-PLAY-dOrderedCharter-61-spec-brief`. The loser A and the test that
  rejected it are recorded here and in §10. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, by `2026-11-02-prompt-PLAY-dOrderedCharter-61-spec-brief`.
- 2026-11-04 · section 3 Edges · from `2026-11-04-prompt-PLAY-dOrderedCharter-15-edge-mirror-brief.md`: the hands-off mirror of the consumes-from edge unit 62 declares against this unit; a mirror-only edit, so the status line keeps its rev.

## 10. Reuse audit

The seams extended: `derive_edges` and its readers in `tools/playbook/check_layers.py:165-283`, as
unit 16 built them and its deviation 163 records them; `scan_shell_lines`
(`tools/memory-tree/check-arms.py:305`), loaded by path as `tools/govkit/govkit.py:2890` and
`tools/push-main.test.sh:1413` already load it; `read_descriptors` (`check_layers.py:115-155`),
whose `files` are the core-owned set S1 reads; and the `optional` row, unit 16's, for §8 F1.
`python tools/codebase-map/reuse_lookup.py "blank quoted strings comments and here-document bodies in a shell script before matching"`
ranked `scan_shell_lines` among its candidates, with `scan_shell_layer` (`tools/codebase-map/map_extractors.py`)
and `parse_shell_defs` (`tools/lexicon/lexicon.py`) in optional kits the core may not import. Where the brief and
the source disagree: `tools/memory-tree/check-memory-hygiene.test.sh:260` is no message but a
`resolve_kit_dir` call to codebase-map that exits 2 when it fails, a real edge in a suite (§8 F1);
`tools/settings-merge.py:620` is a pin inside `_selftest` that is never read from disk, but no static
rule separates it from the read of `{prefix}/govkit/registry.toml` at `check_policy.py:1041`, and the
same file's `resolve_sibling("memory-recall", ...)` at `:711` is a real edge, so one `optional` row
for the file covers both. M12's loser: option A of §8 F1, rejected by the three hard exits measured
there.

Recall terms used: `python tools/memory-recall/query.py "why does a dependency check read a message or a git journal path as a kit dependency" --terms "layer check edge probe path literal kit home false positive quoted string heredoc git dir journal resolve shipped file"`
