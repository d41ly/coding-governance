# TOOL-aMendedFleet-86 — the map digest reports code coverage apart from record coverage

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 86 · closes TOOL-aProbedToolkit-8

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The digest's header is the map's convergence metric, and it divides mapped files by every changed
path, records included. Over the last thirty commits it reads 38%, while code alone is 73% and
records alone 9%: the figure measures how much of a range was memory-tree writing, not how much of
the code the map covers. This unit splits the figure into a code line and a record line, by a record
root the adopter declares, and adds a whole-tree mode, so the number a reader acts on describes code
and the tree-wide figure the kit never printed exists.

## 2. Scope (IN)

- **S1** — `.codebase-map.conf` gains a key `RECORD_ROOTS`: repo-relative directories whose files are
  records rather than code, separated by spaces or commas. This repo declares `memory`. The kit's
  `tools/codebase-map/.codebase-map.conf.example` carries the key blank with a comment saying what it
  splits and what a blank prints. Observed by AC1 and AC4.
- **S2** — `tools/codebase-map/map_diff.py` gains `derive_record_roots(root, conf)`, which splits the
  key and checks each entry names at least one tracked path with one `git ls-files` call. It returns
  the roots and, when any entry names nothing tracked, that entry as the reason the split cannot be
  trusted. The call names `encoding="utf-8"`. Observed by AC3.
- **S3** — The digest keeps its existing header line unchanged and prints two lines beneath it,
  `# code: mapped <m>/<n> (<p>%)` and `# records: mapped <m>/<n> (<p>%) under RECORD_ROOTS <roots>`,
  through one `render_coverage_line(label, mapped, total)`. A population of zero prints
  `n/a (0 files)`, never a percentage over nothing. The module docstring's sentence naming the
  coverage line as the convergence metric names the CODE line instead. Observed by AC1 and AC2.
- **S4** — With `RECORD_ROOTS` blank or absent, one line prints where the two would,
  `# code/records: undeclared - set RECORD_ROOTS in .codebase-map.conf`, so an adopter who has not
  declared it is told the header mixes both; with an entry naming no tracked path, by
  `# code/records: DEAD PROBE - RECORD_ROOTS entry <x> names no tracked path`. Neither case prints a
  split. Observed by AC3 and AC4.
- **S5** — `map_diff.py --tree` attributes every tracked file instead of a range and prints the
  header and the S3 or S4 lines only, no per-feature file list. The range positional becomes
  optional in this mode only; given both, the parser refuses. The affordance-exempt rewrite flag
  with `--tree` is refused too, because a whole tree would clear every grace, and so is
  `--stale-dossiers` with `--tree`, since `TOOL-aMendedFleet-37` already defines that mode's
  no-range scope as the whole history and the two modes print different reports. Observed by AC2.
- **S6** — The `map_diff.py` row of `tools/codebase-map/README.md` names `--tree` and the code and
  record lines, and the `codebase-map` dossier's sentence on the digest says which line is the
  convergence figure. Observed by AC5.

## 3. Non-goals (OUT)

- The baseline shrink assert, the other half of `TOOL-aProbedToolkit-8`. Unit 40 builds it; this unit
  closes the ask on the assumption that unit lands first, which its order guarantees.
- Changing attribution. `attribute_paths` in `tools/codebase-map/map_lib.py` decides mapped and
  unmapped exactly as today; this unit only partitions the population it is given.
- Gating either figure. The digest is a report; a coverage floor is a later decision with its own
  ratchet, and the ask does not request one.
- Reading the memory-tree kit's own conf for its root. A kit file names nothing outside itself by
  literal (charter §12), so the root is declared in this kit's conf.
- Per-feature file lists under `--tree`. Three thousand paths in one report is a listing, not a
  digest; `--verbose` over a range still prints files.
- The codebase-map kit version bump, owed once at the build's close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-40` — the baseline half of `TOOL-aProbedToolkit-8`; without it
  this unit's `closes` verb would close an ask whose second finding is unanswered.
- **consumes-from** `TOOL-aMendedFleet-37` — the `--stale-dossiers` flag in the same parser, whose
  combination with `--tree` S5 refuses and AC2 observes.
- **hands-off** external — the kit version bump at the close.

## 4. Design

### Evidence

Read at base `7af5f564`; `git diff --stat 7af5f564 HEAD` over every file below is empty at
`8312d315`.

- `map_diff.py` computes `mapped_count = len(files) - len(unmapped)` over every changed path and
  prints it as `mapped <m>/<n> (<p>%)`; nothing partitions the population.
- `python tools/codebase-map/map_diff.py HEAD~30..HEAD` at `8312d315` prints 635 files and 245
  mapped, 38%. Partitioned by the `memory/` prefix with the same `attribute_paths` call, code is 213
  of 290, 73%, and records 32 of 345, 9%. Over every tracked file, code is 268 of 356, 75%, and
  records 156 of 2878, 5%. Figures PINNED as read on node a; AC1 and AC2 re-derive them.
- `.codebase-map.conf` declares no record root, and the kit reads no other kit's conf. The only
  memory-shaped literal in the kit engine is the default `MAP_ROOT`.
- Units 37 and 38 edit `map_diff.py` earlier in the build order: 37 adds `--stale-dossiers` with the
  same "range optional in this mode only" rule S5 follows, and 38 deletes `--converge`. Dispatch is
  sequential, so this unit's pass starts from their bytes.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `RECORD_ROOTS` | conf key | none; conf keys are not a declared cell |
| `derive_record_roots` | function in `map_diff.py` | `py.function`; `--suggest` answered OK |
| `render_coverage_line` | function in `map_diff.py` | `py.function`; `--suggest` answered OK |
| `--tree` | CLI flag | none |

### Files touched (estimate)

- `tools/codebase-map/map_diff.py`
- `tools/codebase-map/.codebase-map.conf.example`
- `.codebase-map.conf`
- `tools/codebase-map/README.md`
- `tools/codebase-map/selftest.py`
- `memory/map/features/codebase-map.md`

### Alternatives rejected

- **Deriving the record root from `MAP_ROOT`'s parent.** It reads `memory` here by coincidence of
  layout; an adopter whose map sits elsewhere would get a wrong split with no warning.
- **Reading `MEMORY_ROOT` from the memory-tree conf.** A literal sibling-kit name in a kit file, which
  the charter bans.
- **Replacing the existing header line.** No reader parses it today, but kickoff Step 1 shows it to
  a human every session; adding two labelled lines changes nothing a reader relies on.
- **Excluding records from the digest entirely.** The record line is information too: a range that
  touched 345 records and mapped 9% of them says the map does not describe the memory tree, which it
  does not claim to.

## 5. Production-readiness checklist

- security — N/A — a read of tracked paths and a conf key.
- perf / scale — one extra `git ls-files` per declared root; attributing all 3234 tracked paths
  through `attribute_paths` took 0.66 s on node a at writing, PINNED, by a scratch probe.
- error / empty / loading states — undeclared and dead roots print S4's lines; an empty population
  prints `n/a (0 files)`.
- observability — the record line names the roots it used, so a reader sees what was excluded.
- risks — an adopter whose code lives under a declared record root loses it from the code figure;
  the line naming the roots makes that visible.
- testing — a fixture arm in the kit selftest at the close, declared in §7; AC1 to AC5 run directly.
- migration — the new key is blank in the example, and blank prints S4's line, so no adopter breaks.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/map_diff.py HEAD~30..HEAD` runs after the unit's commit,
  it prints a `# code:` line and a `# records:` line whose two totals sum to the header's file count,
  and whose records total equals the count of the range's changed paths under `memory/`.
  Red when: a record path is counted as code, or the totals do not sum.
  figure: DERIVED at observation from `git diff --name-only HEAD~30..HEAD`; 290 and 345 at writing.
- **AC2** — When `python tools/codebase-map/map_diff.py --tree` runs after the unit's commit, it prints
  the header and the two lines and no `## ` feature section, and its records total equals the line
  count `git ls-files memory` prints; when `--tree` is given with a range, or with
  `--stale-dossiers`, it exits non-zero.
  Red when: the mode lists files, miscounts the tree, or accepts either combination.
  figure: DERIVED from `git ls-files`; 2878 records at writing.
- **AC3** — When a scratch clone under the TEMP root sets `RECORD_ROOTS="memory nosuchdir"` in its
  `.codebase-map.conf`, the AC1 command in it prints the `DEAD PROBE` line naming `nosuchdir` and no
  `# code:` line.
  Red when: a root naming nothing tracked still yields a split.
- **AC4** — When the same scratch clone blanks `RECORD_ROOTS` instead, the AC1 command prints the
  `undeclared` line, and `git grep -n "^RECORD_ROOTS=" -- tools/codebase-map/.codebase-map.conf.example`
  prints the key blank.
  Red when: an undeclared root is silent, or the example omits the key.
- **AC5** — When `git grep -n -e "--tree" -e "RECORD_ROOTS" -- tools/codebase-map/README.md
  memory/map/features/codebase-map.md` runs after the unit's commit, it hits both files.
  Red when: either document still describes one mixed coverage figure.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `kit epoch (shipped bytes move, the version moves)` · `encoding posture (text IO names its encoding)` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/codebase-map/selftest.py · a fixture tree with one code file and one record file under a declared root, asserting one of each, staged red by dropping the root from the conf · none

## 8. Open questions

- **F1 — Is the whole-tree figure the same mechanism as the range split, or a second unit?**
  The ask states both: the digest's figure measures the wrong population, and no command reports
  whole-tree coverage. Options: split the range figure only; split it and add `--tree`.
  `--tree` changes only the population handed to the same attribution and the same split, so it
  adds no mechanism; leaving it out leaves half the ask open with no unit holding it.
  RESOLVED (agent, 2026-10-04, delegated): one mechanism; `--tree` is in scope as S5.
- **F2 — Where does the record root come from?**
  Options: a conf key in this kit; the map root's parent; the memory-tree conf.
  RESOLVED (agent, 2026-10-04, delegated): a conf key, `RECORD_ROOTS`. §4 rejects the other two, one
  for guessing and one for the charter's literal ban.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `TOOL-aProbedToolkit-8`, `map_diff.py` and a partition of
  the digest's population at `8312d315`.
- rev-2 · 2026-10-04 · §3 S5 AC2 · the M2 cross-read: `TOOL-aMendedFleet-37` makes the range optional
  for `--stale-dossiers` in the same parser, and S5 left `--tree --stale-dossiers` undefined between
  the two "optional in this mode only" rules; the parser now refuses it, AC2 observes that, and §3
  Edges declares the flag it rests on.

## 10. Reuse audit

The seam extended is `attribute_paths` in `tools/codebase-map/map_lib.py`, which the digest already
calls; this unit partitions its input and changes nothing inside it. `python
tools/codebase-map/reuse_lookup.py "split a coverage figure into code paths and record paths"`
returned `compute_coverage` (fan-in 4, SEAM), which is the gate's claims ratchet over inventory keys
and computes no path population, `attribute_paths` itself, and name-stem neighbours under
`tools/runlog/` that read run records, not tree paths. The probe printed `unscanned layers: .sh`; no
shell reader of the digest exists to see. The recall probe returned the ask itself, the two sibling
specs that hand this half on, and a parked dTracedLattice note that path globs cap map coverage by
rule, which is why the code figure, not the whole-tree one, is the convergence metric. Where the
report and the tree disagree: the ask measured 21% over thirty commits on 2026-09-03; the same
command reads 38% at `8312d315` because the population moved, and the code-only figure the ask
derived, 67%, now reads 73% over the range and 75% over the tree.

Recall terms used: `python tools/memory-recall/query.py "why does the map digest coverage figure
count memory records beside code" --terms "map_diff digest coverage mapped unmapped memory records
code population attribute_paths convergence TOOL-aProbedToolkit-8 whole-tree"`
