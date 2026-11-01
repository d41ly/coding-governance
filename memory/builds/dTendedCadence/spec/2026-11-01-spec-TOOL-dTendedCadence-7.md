# TOOL-dTendedCadence-7 — one dead-pointer detector over auto-memory and served text, its merge-bar leg kept in the maintain pack

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 10 · advances TOOL-dTendedCadence-19

**Carries:** cl-dClosedLoop-0448@6053b724 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-5-reuse-scout-c.md](../build/2026-11-01-build-TOOL-dTendedCadence-5-reuse-scout-c.md) | research | TOOL-dTendedCadence-5 TOOL-dTendedCadence-12 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |

<!-- /gen:spec-records -->

## 1. Goal

Two probes look for pointers to files that no longer exist, and neither belongs to Maintain. The
drift-audit signal `dangling_pointers_in_own_ledger` reads the agent's auto-memory and only reports
(gap-orient-10, gap-maint-08). The gov-only gate `check-dead-paths.sh` reads the text outside
`memory/`, map dossiers and gotcha pages that name a deleted or renamed file, and is a merge-bar leg
no reading reaches. This unit makes them one detector owned by Maintain: two populations, each
keeping its own oracle, each registered as a reading Maintain files on, and the script's merge-bar leg
kept, registered by the detector at Test's leg-pack point (NP-22; night-pass:755, "so a dead path
still blocks a merge").

## 2. Scope (IN)

Build-run preconditions: TOOL-dTendedCadence-8 (the `[[reading]]` row, I3, and the offender key, I5),
TOOL-dTendedCadence-18 (`run_signal_leg`, I12; the `pack` values, I13; `maintain.reading-tree`, I14)
and TOOL-dTendedCadence-15 (`item.maintain.file`); the parents TOOL-dWitnessedBar-11 S1-S3 (an
`[[exempt_leg]]` row carrying the leg's whole row, rendered by `leg_factory.py`) and PLAY-dOrderedCharter-19 S12 (the `pack` key).

- **S1** — The served-text population's shared function. `tools/check-dead-paths.sh` gains a third
  mode, `--offenders`, beside `--check`, `--list` and `--needles` (`:111-112`). It runs the same needle
  derivation (`:118-165`), the same two frozen sentinels (`:168-181`), the same haystack (`:188-198`)
  and the same waiver resolution (`:216-255`), and prints one line per carrier,
  `<path>:<line>\t<state>`, the state `hit` for an unwaived carrier, `waived` for a waived one and
  `stale` for a waiver row that names no hit or cannot resolve, the row's resolved token or its
  `<path>:<reason>` in the first field. It exits 0 when it printed the set, whatever the set holds, and
  1 or 2 on exactly the refusals `--check` exits 1 or 2 on: a broken derivation, an empty needle set, a
  missing sentinel and a malformed waiver row, each with its existing message. `--check` keeps its
  verdict and its output byte for byte. Observed by AC1, AC2 and AC3.
- **S2** — The detector, a new module `tools/drift-audit/dead_pointers.py`, holding both populations
  in drift-audit's reading record shape (I4: `signal`, `value`, `of`, `tolerance`, `gateable`, `live`,
  `unjudgeable`, `detail`, `not_asked`):
  - `measure_dead_text_pointers(ctx)`, signal `dead_paths_in_served_text`, repo-scoped, its oracle
    `check-dead-paths.sh`'s history needles: it runs `bash <root>/<prefix>/check-dead-paths.sh
    --offenders` as a bounded subprocess with `cwd` the root it reads (`ctx.root`, a scratch worktree
    at the base under `maintain.reading-tree: clean-base`, I14), `<prefix>` the drift-audit kit's
    parent relative to its own repository (`tools` on gov), so a clean-base reading runs the base's
    copy of the script. `value` counts the `hit` and `stale` lines, `of` counts every line, `detail`
    holds one `{"path", "line", "state"}` row per `hit` or `stale` line, `tolerance` is 0 and
    `gateable` is false, so `drift_report.py --check` gates nothing of it. Exit 1 or 2 reads `live:
    false` with the script's first output line as a `DEAD PROBE — …` note. No script at that path
    reads `not asked`, the I4 record with `not_asked: true` built inline, since this module imports
    nothing of `drift_report.py` at load time.
  - `signal_dangling_pointers(ctx)` with `resolve_auto_memory_dir` and the three patterns it reads
    (`tools/drift-audit/drift_report.py:941-1025`), moved into this module as TOOL-dTendedCadence-4 S5
    leaves it, its `tolerance` 0: signal `dangling_pointers_in_own_ledger`, node-scoped, its oracle the
    tracked set (`:988`, `:1005`).
    `drift_report.py` imports both names from `dead_pointers`, so `dr.signal_dangling_pointers` and
    `dr.resolve_auto_memory_dir` still resolve for every caller.

  Observed by AC4, AC6, AC7 and AC8.
- **S3** — The detector's command, `python dead_pointers.py [--leg] [--offenders]`. It reads the
  working directory's top level as its root, loads the project layer through `drift_report.py`'s
  `load_project_layer` at call time for `AUTO_MEMORY_DIR`, and prints one line per population through
  `run_signal_leg(signals, bounds)` (I12), the served-text record its one gateable signal at bound 0,
  so the exit is 1 while a carrier is a `hit` or a waiver is `stale`, and 1 on its dead probe, as
  `drift_report.py --check` reds a dead gateable signal. The auto-memory line is printed and never
  sets the exit. `--offenders` prints the I5 keys, `<signal>\t<detail key>`, for both populations.
  `--leg` makes a `not asked` served-text population a refusal, exit 2, so the leg can never pass by
  reading nothing. Observed by AC4, AC5, AC6 and AC7.
- **S4** — The leg kept. The leg `dead-path carriers (deleted files still named)` keeps its name, its
  `reads`, `chunk`, `subject` and `ceiling` (`tools/gate-legs.json:1367-1377`), and its argv becomes
  `["python", "{prefix}/drift-audit/dead_pointers.py", "--leg"]`. Its declaration is its
  `[[exempt_leg]]` row in `tools/govkit/registry.toml` (`:402-406`), which carries the leg's whole row
  under TOOL-dWitnessedBar-11 S1, now with `pack = "maintain"` (I13); `tools/gate-legs.json` is that
  row's render through `leg_factory.py --write`. Its self-test leg, `dead-path carriers self-test`,
  carries `pack = "maintain"` too. Both stay gov-only, so no adopter receives the leg. Observed by AC5.
  **Readers:** by name: the leg's old argv `{prefix}/check-dead-paths.sh`, which `tools/gate-legs.json`
  spells (`:1371`) and S4's render rewrites; `tools/govkit/registry.toml` spells the same path (`:246`) for
  the script's `[[exempt]]` row, which stays, since the script stays. by value: `tools/run-gates/run-gates.sh`,
  which runs each leg's argv as `tools/gate-legs.json` holds it, and `tools/run-gates/held_halves.py`
  (`:129`), which wraps each leg's argv; `tools/check-dead-paths.test.sh` runs the script by its path and
  never through the leg's argv, so it reads S1's script unchanged.
- **S5** — The two readings registered (I3) in `tools/drift-audit/kit.toml`. One new `[[reading]]` row,
  `dead_paths_in_served_text`, with `scope = "repo"`, `kind = "code"`, `pin = "dead_paths_in_served_text"`
  and `edges = [0, 0]`; and the
  `dangling_pointers_in_own_ledger` row TOOL-dTendedCadence-8 already declares among the 27, extended in
  place and never declared a second time, since that unit's check refuses a second row of one `name`: it
  carries `scope = "node"`, no `kind`, so its owner derives `layer.runtime` (TOOL-dTendedCadence-4 S1),
  `pin = "dangling_pointers_in_own_ledger"` and `edges = [0, 0]`. Each row's pin is 0, its record's `tolerance` 0, as TOOL-dTendedCadence-4 §8 F1
  states, and neither takes a `drift-pins.txt` entry, since a ledger row's count is a positive integer
  and a pin of 0 has no row (TOOL-dTendedCadence-34). The edges sit on the row beside its pin, as
  TOOL-dTendedCadence-14 S1 settles them, so any offender is in the act band. Neither declares a `fix`,
  so an offender over its pin routes to `item.maintain.file` (§8 F2, F3). Observed by AC9.
- **S6** — The docs: drift-audit's README signal table gains the `dead_paths_in_served_text` row and
  names `dead_pointers.py` as both rows' home; the dossier `memory/map/features/install-prefix.md`
  names `--offenders` and the detector beside its affordance line (`:205-209`). Observed by AC10.

## 3. Non-goals (OUT)

- `DEAD_PATH_PIN` (`.memory-tree.conf:455`, hygiene checks 13-15), a third dead-path population, the
  citations inside `memory/`: the clause names two populations, and that pin stays the hygiene gate's.
- One oracle for both populations: §4 "Alternatives rejected" records the test that rejects each
  merge of them.
- Shipping the served-text population to adopters: the script's sentinels name basenames only gov's
  history holds (`tools/govkit/registry.toml:245-250`), so in an adopter tree the population reads
  `not asked`.
- A safe fix for either population: rewriting a carrier or a node's notes changes prose, so both file
  through `maintain.file` (TOOL-dTendedCadence-15) and declare no `fix`.
- Which nodes read the node-scoped population: `maintain.node-readings` and the (period, node) lease,
  TOOL-dTendedCadence-16's key and TOOL-dTendedCadence-1's `maintain.lease`.
- The reading registry, its admission and its bands: TOOL-dTendedCadence-8, -4 and -14, cited.

### Edges

- **consumes-from** `TOOL-dTendedCadence-8` — the `[[reading]]` row (I3) both S5 rows are, and the offender key `render_drift_offenders` emits (I5), which S3's `--offenders` prints; without it neither population is a reading Maintain runs
- **consumes-from** `TOOL-dTendedCadence-18` — `run_signal_leg` (I12), through which S3 prints and exits; the `pack` value `maintain` (I13); and `maintain.reading-tree` (I14), whose clean-base tree is the root S2's served-text population reads
- **consumes-from** `TOOL-dTendedCadence-15` — `item.maintain.file`, the route an offender of either population takes, since neither declares a fix
- **consumes-from** external — TOOL-dWitnessedBar-11 S1-S3 (the `[[exempt_leg]]` row and `leg_factory.py`) and PLAY-dOrderedCharter-19 S12 (the `pack` key)

## 4. Design

### Evidence

At this base the two populations share nothing but their purpose. `signal_dangling_pointers`
(`tools/drift-audit/drift_report.py:968-1025`) reads `*.md` under `AUTO_MEMORY_DIR`
(`tools/drift-audit/drift_signals.py:476`), judges each backticked span with a `/` whose first
segment is a tracked top level, and calls it dead when `git ls-files` holds neither the path nor a
directory prefix of it; it is report-only and pinless (`:1010-1014`). `check-dead-paths.sh` derives
its needles from `git log --diff-filter=D` and the sources of `--diff-filter=R` rows outside
`memory/`, minus every basename still tracked (`:118-165`), greps them over every tracked path
outside `memory/` plus `memory/map/features/*` and `memory/gotchas/*` (`:193-197`), resolves a
text-keyed waiver registry (`:216-246`), and reds on an unwaived hit or a stale row (`:275-305`). Its
leg is a hand row of `tools/gate-legs.json` (`:1367-1377`) with an `[[exempt_leg]]` row
(`tools/govkit/registry.toml:402-406`), and the script itself is an `[[exempt]]` path (`:245-250`).
The clause was re-worded from "the memory's dead pointers" after the walk found the script covers
nothing inside `memory/` (walk-return-c5 C5-F2, confirmed low at skeptic-return-c4:44-47).

### The two oracles, kept apart

| Population | Scope | Oracle | Why this oracle |
|---|---|---|---|
| the node's auto-memory notes | node | the tracked set: a path is dead when `git ls-files` holds neither it nor a directory under it | a note may name a path that never existed, a typo the history oracle never sees |
| text outside `memory/`, map dossiers, gotcha pages | repo | history needles: a basename the repo once tracked and no longer tracks | the tracked-set oracle over shipped text measured 217 false hits, nearly all fixture literals (`check-dead-paths.sh:25-28`) |

The detector is one module with one owner and one filing route; the oracles stay two functions, so
neither population is ever judged by the other's rule. AC8 is the observation that keeps them apart.

### The leg, registered by the detector

The bar's verdict and Maintain's reading are one record: the leg runs `dead_pointers.py --leg`, which
reads the script's `--offenders` and bounds it at 0 through `run_signal_leg`, so the bar and the
maintenance record cannot disagree about a carrier. `--check` stays the script's own verdict, read by
its self-test and by an author; its bytes do not move, so `check-dead-paths.test.sh` keeps every arm
it has. The leg is declared in the maintain pack (`pack = "maintain"`, I13) and keeps its name, so
its timing history and its `ceiling` stay keyed.

### Inventory

Minted, each asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at this base
and answered OK: `measure_dead_text_pointers`. Module `dead_pointers.py`: the `py.file` cell is
undeclared at this base, so no convention answers it. Signal name `dead_paths_in_served_text`, a
record value and no identifier. Modes `--offenders` (the script) and `--leg` (the module). No policy
key: this unit owns no node.

### Readers of what moves

`signal_dangling_pointers` and `resolve_auto_memory_dir` move with their names; their readers keep
resolving through `drift_report.py`'s import: `SIGNALS` (`tools/drift-audit/drift_report.py:3523`)
and the arm `tools/drift-audit/selftest.py:3204-3245`, which calls `dr.signal_dangling_pointers` and
`dr.resolve_auto_memory_dir`. The signal name, the `drift-history.tsv` key, is unchanged, so its
dead streak survives (I4).

### Rollout

One commit lands `--offenders`, the module, the leg's new argv and its pack, so no bar runs the leg
against a mode that is not there. The script's `--check` is unchanged in that commit.

### Files touched (estimate)

- `tools/check-dead-paths.sh`
- `tools/check-dead-paths.test.sh`
- `tools/drift-audit/dead_pointers.py` (new)
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/kit.toml`
- `tools/drift-audit/README.md`
- `tools/govkit/registry.toml`
- `tools/gate-legs.json` (rendered by `leg_factory.py --write`)
- `memory/map/features/install-prefix.md`

### Alternatives rejected

- **The tracked-set oracle over served text.** Rejected by its recorded measurement: 217 hits,
  essentially all legitimate fixture literals (`check-dead-paths.sh:25-28`).
- **The history oracle over auto-memory.** Rejected by the arm `selftest.py:3204-3245`: its planted
  `src/gone.py` was never tracked, so no needle names it, and the history oracle reads that note clean.
- **A Python port of the script's derivation.** Rejected: the script's derivation, sentinels and
  waiver resolution carry 354 lines of arms in `check-dead-paths.test.sh`, and a port re-proves them for
  no new behaviour; `--offenders` shares the one function, as NP-22's proposal worded it ("its
  dangling-path function shared").
- **The leg left on `check-dead-paths.sh --check`** (§8 F1 option b). Rejected: the bar and the
  reading would hold two verdict functions over one population.
- **The signals left in `drift_report.py`, beside each other.** Rejected: the leg needs a command
  that loads no 4,484-line engine and none of its other 26 signals.

## 5. Production-readiness checklist

- security — N/A: both populations read the tracked tree, git history and the node's own notes, and
  write nothing; a note's path is a string compared against `git ls-files`, never opened.
- perf / scale — the served-text population is one script run, the leg's cost today (`ceiling` 430,
  PINNED in `tools/gate-legs.json:1376`, re-measured by `measure_legs.py`); the module adds one Python
  start. The auto-memory population reads one `git ls-files`.
- error / empty / loading states — no script: `not asked`, a refusal under `--leg`; a broken
  derivation or a malformed waiver: `dead probe` and exit 1; no auto-memory directory: `not asked`;
  a directory that does not exist: `dead probe` (`drift_report.py:982-984`).
- observability — one line per population; `--offenders` prints the keys Maintain files under.
- risks — the leg's argv moves; the rollout lands it with the mode it calls, and AC5 reads the row.
- testing — `--offenders` arms in `check-dead-paths.test.sh`; the module's arms in drift-audit's
  selftest; §7 New arm lines.
- migration — N/A: no record changes shape; both rows' pins are 0, their records' `tolerance`, with no `drift-pins.txt` row.
- user docs — drift-audit's README signal table and the install-prefix dossier (S6); no `help/` page
  covers drift-audit or the dead-path gate at this base.

## 6. Acceptance criteria

The dead-path fixture is a scratch git repository under `%TEMP%` with a short name. Its first commit
adds `tools/check-dead-paths.sh` copied from the worktree, an empty `tools/dead-path-waivers.txt`,
`parallel-coding-governance.domain-rules.md`, `parallel-coding-governance.template.md`, `gone.md` and
`src/a.py`. Its second commit removes the first file and `gone.md` and renames the second with `git
mv`. Its third commit adds `README.md` naming `gone.md` and `package.json`, `memory/r.md` naming
`gone.md`, and `memory/map/features/f.md` naming `gone.md`. Each command runs with the fixture as its
working directory; the module is the worktree's.

- **AC1** — When `bash tools/check-dead-paths.sh --offenders` runs in the dead-path fixture, it prints
  exactly `README.md:1` and `memory/map/features/f.md:1`, each with state `hit`, and exits 0.
  Red when: the record under `<fixture>/memory/` or the never-tracked `package.json` is printed, or
  the dossier is not.
- **AC2** — When `bash tools/check-dead-paths.sh --offenders` runs after a waiver row naming the
  `README.md` line and a second row naming text no file holds are added, it prints `README.md:1` as
  `waived` and the second row as `stale`; with a row whose ordinal is `0` it exits 1 printing
  `MALFORMED` and no carrier line.
  Red when: a stale row is not printed, or a malformed registry prints a set.
- **AC3** — When `bash tools/check-dead-paths.sh --offenders` runs in a copy of the fixture whose
  history never removed `parallel-coding-governance.domain-rules.md`, it exits 1 naming the frozen
  sentinel; `bash tools/check-dead-paths.sh --check` in the original fixture prints the bytes it
  printed before this unit.
  Red when: the broken derivation prints an empty set and exits 0, or `--check` output moves.
- **AC4** — When `python dead_pointers.py` runs in the dead-path fixture, it prints
  `dead_paths_in_served_text 2 of 2 · over` and exits 1; after a commit re-pointing both carriers it
  prints `0 of 0 · ok` and exits 0.
  Red when: a hit reads `ok`, or a clean tree exits 1.
- **AC5** — When `grep -n -A12 '"dead-path carriers (deleted files still named)"' tools/gate-legs.json`
  runs, the row carries `"pack": "maintain"` and an argv naming `dead_pointers.py` and `--leg`, and
  `grep -n -A6 'dead-path carriers' tools/govkit/registry.toml` shows `pack = "maintain"` on both
  `[[exempt_leg]]` rows.
  Red when: either leg lacks the pack, or the leg still runs the script directly.
- **AC6** — When `python dead_pointers.py --leg` runs in AC3's broken copy, it prints
  `dead_paths_in_served_text` with `dead probe:` and the sentinel message, and exits 1.
  Red when: a broken derivation reads `ok` or exits 0.
- **AC7** — When `python dead_pointers.py` runs in a scratch repository holding no
  `tools/check-dead-paths.sh`, the served-text line reads `not asked:` and the exit is 0; with
  `--leg` the exit is 2.
  Red when: the leg passes over a tree with no script.
- **AC8** — When a probe imports `dead_pointers` and calls `signal_dangling_pointers` with a
  namespace ctx whose `auto_memory_dir` holds a note naming two paths under `src`, the
  never-tracked `gone2.py` and the tracked `a.py`, it reads `1 of 2`; in the same fixture,
  `README.md` naming `package.json` adds no served-text offender.
  Red when: either oracle judges the other's population: the never-tracked note path reads clean, or
  the never-tracked README name reads dead.
- **AC9** — When `grep -n -A5 'name = "dead_paths_in_served_text"' tools/drift-audit/kit.toml` runs,
  the row carries `scope = "repo"`, `kind = "code"`, its pin and `edges = [0, 0]`,
  the `dangling_pointers_in_own_ledger` row carries `scope = "node"`, its pin and `edges = [0, 0]`, and
  `grep -c 'name = "dangling_pointers_in_own_ledger"' tools/drift-audit/kit.toml` prints 1.
  Red when: either row lacks its scope, its pin or its edges, so admission refuses it, or the auto-memory row is
  declared twice, which TOOL-dTendedCadence-8's check refuses.
- **AC10** — When `grep -n "dead_paths_in_served_text\|dead_pointers.py" tools/drift-audit/README.md`
  runs, the signal table row and the home are found, and `grep -n "offenders"
  memory/map/features/install-prefix.md` finds the mode.
  Red when: the new signal has no README row, so the hand-kept signal list disagrees with the engine.

## 7. Gates

`drift-audit selftest` · `dead-path carriers (deleted files still named)` · `dead-path carriers self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/check-dead-paths.test.sh · covers AC1 AC2 AC3 · the `--offenders` cases, staged by printing `waived` for a stale row · none
New arm: tools/drift-audit/selftest.py · covers AC4 AC6 AC7 AC8 · the detector's arms over a built dead-path fixture, staged by `measure_dead_text_pointers` reading the tracked set · none

## 8. Open questions

- **F1 — What does the kept leg run?** (a) The detector, `dead_pointers.py --leg`, reading the
  script's `--offenders` and bounded through `run_signal_leg`; (b) the script's `--check`, unchanged,
  with `pack = "maintain"` added. Both keep the leg's name, population and verdict class, so a dead
  path blocks a merge either way. (a) satisfies more: the bar and the maintenance record read one
  record (the charter's one-fact rule), the leg is registered by the detector as night-pass:755 states,
  and the factory I12 is used at its kind's instance; (b) leaves two verdict functions over one
  population. Rung 3, the most feature-rich survivor. RESOLVED (agent, 2026-11-01, delegated): (a).
  widens: none · relaxes: none
- **F2 — Which `kind` does the served-text reading declare, so its owner derives?** (a) `code`, the
  core record of tracked files (TOOL-dTotalRecall-8 S7, S11); (b) three rows split by carrier class,
  `dossier`, `gotcha` and `code`; (c) a new kind. Every candidate kind is a memory-contract kind, so
  (a) and (b) derive one owner, and the tie rule (layer-expansions:201-202) settles any difference by
  the layer that wrote the line; (b) triples the rows for no different filing, and (c) adds a kind no
  clause names. Rung 3, tie-broken by fewer rows. RESOLVED (agent, 2026-11-01, delegated): (a).
  widens: none · relaxes: none
- **F3 — Where does the auto-memory reading's pin live?** (a) A `drift-pins.txt` entry at count 0,
  named by the row's `pin`; (b) no entry, the record's `tolerance` 0 alone, as TOOL-dTendedCadence-4 S5
  leaves it ("takes no gov entry, since one node's count bounds no other node"), with `edges = [0, 0]`
  on the `[[reading]]` row; (c) an entry at this node's count today. (c) commits one node's count as
  every node's pin, the defect TOOL-aMendedFleet-51 named (`drift_report.py:1010-1012`). (a) cannot be
  written: a ledger row's count is a positive integer, so a pin of 0 has no row (TOOL-dTendedCadence-34).
  (b) holds: 0 is every node's right answer, and the edges live on the row beside its pin, as
  TOOL-dTendedCadence-14 S1 settles them, so admission under `maintain.tiers: bands`, the default,
  admits it and gap-orient-10 leaves report-only; TOOL-dTendedCadence-16 registers its node-scoped
  readings the same way. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (b), the spec run's fix
  brief ruling 2. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.

## 10. Reuse audit

The seams extended: `check-dead-paths.sh`'s derivation, sentinels and waiver resolution
(`tools/check-dead-paths.sh:118-255`), shared through a new mode rather than copied, as its dossier's
affordance line asks (`memory/map/features/install-prefix.md:205-209`); `signal_dangling_pointers`
with `resolve_auto_memory_dir` (`tools/drift-audit/drift_report.py:946-1025`), moved unchanged; the
leg's existing rows (`tools/gate-legs.json:1367-1389`, `tools/govkit/registry.toml:402-412`); and
I12's `run_signal_leg` (TOOL-dTendedCadence-18) for the leg's line and exit. The probe `python
tools/codebase-map/reuse_lookup.py "detect dead pointers to deleted or renamed files in text and in
auto-memory notes"` ranked name-stem neighbours (`read_text`, `note`, `write_text`) and, lower,
`signal_dangling_pointers` and `derive_dead_streaks`; it does not index shell gates, so it could not
name `check-dead-paths.sh`, which scout C's record and the dossier name. No existing seam joins the
two populations, so the module is new over the seams above. Where scout C's record disagrees with
source at this base: none; its `:941-1025`, `:946`, `drift_signals.py:476`, `:118-198`, `:216-246` and
`gate-legs.json:1367-1389` hold.

Recall terms used: `python tools/memory-recall/query.py "how does the dead-path gate and the
dangling-pointer signal find files named that no longer exist" --terms "dead-paths needles deletion
rename waiver sentinel dangling auto-memory tracked oracle drift-audit"`
