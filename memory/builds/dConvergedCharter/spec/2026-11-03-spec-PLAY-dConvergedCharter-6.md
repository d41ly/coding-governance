# PLAY-dConvergedCharter-6 — every record kind on dTotalRecall's registry: the residue sweep of the memory tree's homes, and the kinds no spec registers

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 10 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0480@7f73d023 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md](../build/2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md) | research | PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-15 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |

<!-- /gen:spec-records -->

## 1. Goal

dTotalRecall's registry, `tools/memory-tree/record-kinds.toml`, is the record-kind factory and its conformance
gate (TOOL-dTotalRecall-1 S1, S3, S9; P16), and each kind arrives with the unit that owns it. Nothing says every
record the memory tree holds has one: a home no row's `home` glob matches stays invisible to the gate. This unit
closes the clause, "every record kind on dTotalRecall's registry, the record-kind factory, and through its
conformance gate", as a residue sweep: an arm of `check_record_kinds` that reds every tracked file under the
memory root no row's home admits, and the rows, through the factory, of the kinds no spec registers.

## 2. Scope (IN)

Build-run preconditions, each specced and DEFERRED at base `0d1c1dda`: TOOL-dTotalRecall-1 (the registry, the
gate `check_record_kinds`, the factory `record_kinds.py new`, the leg `record-kinds`), TOOL-dTotalRecall-18 (the
`home`, `lifecycle`, `readers` and `layer` columns on every row, the `view`, `registry` and `archive` rows, and
`check_pockets`), TOOL-dTotalRecall-42 S4-S5 (the tracked-home grammar and `derive_record_kind`),
TOOL-dTotalRecall-2 (the door the factory grows into), PLAY-dOrderedCharter-7 S4-S5 (the `kind.record-kind`
conformance contract), PLAY-dOrderedCharter-42 (`TYPED_RECORD_KINDS`) and PLAY-dOrderedCharter-3 S1-S2
(`tools/playbook/documents.toml`). None of these files exists at base.

- **S1** — The residue arm. `check_record_homes(root)` in `tools/memory-tree/record_kinds.py`, called by
  `check_record_kinds` so the leg `record-kinds` runs it. Its population is `git ls-files -z` under the memory
  root `.memory-tree.conf` declares, as `tracked()` lists a tree (`tools/govkit/govkit.py:344`). It subtracts each
  path a row's tracked `home` glob admits, through the home-match predicate `check_pockets` and
  `derive_record_kind` already apply, never a second glob dialect, and each path a `documents.toml` row
  registers, so a document is never also a record. Every path left prints
  `record-kinds: unregistered home <path>` and the gate exits 1. Observed by AC1, AC2 and AC4.
- **S2** — The count line. The arm prints `record-kinds: homes <n> tracked · <m> admitted · <d> documents ·
  <u> unregistered` on every run, and a population of zero tracked files is red, `record-kinds: no tracked
  file under <root>`, so an empty population never reads as coverage. Observed by AC2 and AC5.
- **S3** — The kinds no spec registers, each through the factory, `python record_kinds.py new <name> --tag
  record.<name> --writer <door> --check record-kinds`, its `home`, `lifecycle`, `readers` and `layer` set
  through TOOL-dTotalRecall-18's landed verb, as TOOL-dLinkedLibrary-13 S2 sets them (§4 "The rows"):
  `run-state`, a build's run-state file and its rotated copies; and `memory-index`, the memory tree's own
  `README.md`. Observed by AC3.
- **S4** — The homes another kind owns. A residue path whose record belongs to a kind another unit registers
  (§4 "The census") takes that row's `home` cell by one added glob, written through TOOL-dTotalRecall-18's verb,
  never a second row for the kind. Observed by AC2.
- **S5** — The docs. `tools/memory-tree/README.md`'s registry section (TOOL-dTotalRecall-1 S12) gains the
  residue arm, its count line and the rule that a new record home owes a row or a glob before its first
  record lands. Observed by AC6.

## 3. Non-goals (OUT)

- The registry, its gate, its factory and its leg: TOOL-dTotalRecall-1. This unit adds an arm and rows.
- A kind another build's unit owns: `gotcha` (TOOL-dLinkedLibrary-22 S4), `decision` (TOOL-dLinkedLibrary-1),
  `dossier`, `backlog-row` and `design-record` (TOOL-dTotalRecall-1 S2), `view`, `registry` and `archive`
  (TOOL-dTotalRecall-18 S5), `research-return` (TOOL-dLinkedLibrary-13 S2), and each member of
  `TYPED_RECORD_KINDS`. Each is cited, never registered twice.
- The pockets outside the tree: TOOL-dTotalRecall-18 S6's `check_pockets`.
- Rewriting any record into a registered form: legacy records keep theirs (TOOL-dTotalRecall-1 S8).
- Merging kinds: PLAY-dConvergedCharter-3.
- The instruction documents under the memory root: PLAY-dOrderedCharter-3's `documents.toml`, which S1 reads.

### Edges

- **hands-off** `PLAY-dConvergedCharter-3` — `record_kinds.py`, the registry whose every home is now a row, over which unit 3 measures and merges kinds
- **hands-off** `PLAY-dConvergedCharter-2` — `record_kinds.py`, the registry whose every home is now a row, whose `home` and `lifecycle` unit 2 reads to class a citing path; this unit adds no `--homes` print mode, and unit 2's S1 adds it to `record_kinds.py`
- **hands-off** `PLAY-dConvergedCharter-7` — `record_kinds.py`, whose `--template` renders every kind's schema, one of unit 7's view sources
- **consumes-from** external — TOOL-dTotalRecall-1, -2, -18 and -42, PLAY-dOrderedCharter-3, -7 and -42, each specced and DEFERRED at base, landed in ancestors before the build run

## 4. Design

### Evidence

- No registry exists at base: `tools/memory-tree/record-kinds.toml` and `record_kinds.py` are absent, and the
  kinds are spread over `RECORD_KIND_TOKENS` (`tools/memory-tree/tree_lib.py:406`) and runlog's `RECORD_SCHEMA`
  (`tools/runlog/record.py:176`).
- TOOL-dTotalRecall-1 S7's `--population` prints one member `record-kind-schema:<kind>.<field>` per field of a
  row, the step gate's class, and no record path. The brief's "`memory/**` minus `record_kinds.py
  --population`" therefore reads the wrong reader; the rows' `home` column (TOOL-dTotalRecall-18 S1) is the one
  that admits a path, and S1 reads it.
- TOOL-dTotalRecall-18 S6 already sweeps the common directory for entries no row's home matches; S1 is the same
  join over the tracked tree, its second instance, so it calls that predicate.

### The census

The FACT-QUESTION of §8 F1, run at base: `git ls-files memory` grouped by home, each home joined to the kinds
the specs of every build register (a `git grep` of `record_kinds.py new` and of each `home` cell under
`memory/builds/*/spec/`).

| Home at base | Files | Its kind and owner |
|---|---|---|
| `memory/builds/*/build/*.md`, `spec/*.md`, `reviews/*.md`, `prompts/*.md` | 9774 | the Serves kinds and `spec` (TOOL-dTotalRecall-1 S2), each typed kind, `instrument` for a script beside its record (-18 S5), and `research-return`'s `memory/builds/*/*/*.md` |
| `memory/builds/*/README.md`, `BACKLOG.md` | 347 | `build-readme` and `backlog-row` (dTotalRecall) |
| `memory/builds/*/RUN.md` | 113 | none: S3's `run-state` |
| `memory/builds/*/RUN.LANDED.*.md`, `RUN.ABORTED.*.md` | 11 | none: S3's `run-state` |
| `memory/gotchas/*.md` | 152 | `gotcha` |
| `memory/DECISIONS.md` | 1 | `decision` |
| `memory/project/*.txt` | 22 | `registry` (TOOL-dTotalRecall-18 S5) |
| `memory/LIVE.md`, `memory/ledger/*.md`, `memory/backlog/*.md` | 10 | `view` (the ask views and the ledger, -18 S5) |
| `memory/archive/**` | 18 | `archive` |
| `memory/map/features/*.md`, `memory/map/FOUNDATION.md` | 33 | `dossier` (S4 adds the second glob when its row lacks it) |
| `memory/map/README.md`, `memory/map/generated/*` | 5 | `view`, generated by `gen_map.py` (S4) |
| `memory/map/baseline.toml`, `memory/map/affordance-exempt.toml` | 2 | `registry` (S4) |
| `memory/guides/*.md`, `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` | 12 | documents, PLAY-dOrderedCharter-3 S2's seeded rows |
| `memory/README.md` | 1 | none: S3's `memory-index` |

Counts are PINNED at base `0d1c1dda` and re-derived by S2's count line at every run. Scout B's residue list
(`prompt`, `RUN.md`, `memory/project/*.txt`, the ledger) disagrees with source in three of four places: the
prompt records carry `journal` or `research` Serves lines and sit under `research-return`'s home, and the lists
and the ledger are TOOL-dTotalRecall-18 S5's `registry` and `view`.

### The rows

| name | home | lifecycle | form | writer | readers |
|---|---|---|---|---|---|
| `run-state` | `memory/builds/*/RUN.md`, `memory/builds/*/RUN.*.md` | `current-state` | `header` | the run driver's verb that writes it at the build run's base (TOOL-dWellOiledMachine-25), re-grounded on landed code | the run-state read keys the roles name, or `readers-none` with the reason |
| `memory-index` | `memory/README.md` | `current-state` | `header` | `hand` | `readers-none`: no work order hands it |

Both rows take `layer.memory` and `check = "record-kinds"`. A rotated copy (`RUN.LANDED.<sha>.md`) is the same
kind frozen by its rename, so it carries no row of its own.

### The arm

```
check_record_homes(root):
    tracked = git ls-files -z -- <memory root>                 # tracked(), govkit.py:344
    if not tracked: red "no tracked file under <root>"
    admitted  = {p for p in tracked if any row's tracked home admits p}   # the predicate check_pockets uses
    documents = {p for p in tracked if a documents.toml row registers p}
    for p in sorted(tracked - admitted - documents): red "unregistered home <p>"
    print counts
```

### Inventory

Minted, asked of `lexicon.py --suggest <name> --as py.function` at base and answered OK: `check_record_homes`.
The kind names `run-state` and `memory-index`, their tags `record.run-state` and `record.memory-index`, and
the count line `record-kinds: homes`.

### Files touched (estimate)

- `tools/memory-tree/record_kinds.py`: S1, S2
- `tools/memory-tree/record-kinds.toml`: S3, S4
- `tools/memory-tree/README.md`: S5
- `memory/HYGIENE.md`: re-rendered from `tools/memory-tree/HYGIENE.template.md`'s `gen:record-kinds` region,
  which carries the two new rows

### Alternatives rejected

- **The population minus `record_kinds.py --population`.** Rejected by reading TOOL-dTotalRecall-1 S7: that
  verb prints schema-field members, so every record path would read unregistered.
- **One catch-all row whose home is `memory/**`.** It admits every path, so the arm can never red: the
  vacuous-selector class.
- **A second residue gate beside `check_record_kinds`.** Two legs over one registry; the arm rides the leg the
  registry already declares.
- **Registering `prompt` as a kind.** The prompt files are `journal` and `research` records by their Serves
  lines, so a `prompt` row is a second kind for one record and grades it twice.

## 5. Production-readiness checklist

- security — read-only over tracked paths; no write surface beyond the registry file the factory owns.
- perf / scale — one `git ls-files` and one glob pass over about 10,500 paths.
- error / empty / loading states — an empty population is red (S2); an unreadable `documents.toml` is red, never
  an empty subtraction.
- observability — the count line on every run, and one line per unregistered path.
- risks — a broad home glob admits paths of other kinds: the arm grades that a home is declared, never that the
  admitting kind is the right one, which `derive_record_kind` grades per record.
- testing — AC1 to AC5, and the arm of §7.
- migration — none: the arm reads; existing records keep their form.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When `python record_kinds.py --check` runs in a fixture tree holding a planted record in a `notes`
  folder of a build, a home no row admits, it exits 1 printing `record-kinds: unregistered home` and that path.
  Red when: the arm stays silent on the planted home, the clause's seen-red case.
  fixture: a scratch repository under `%TEMP%/<short>` with the registry copied in.
- **AC2** — When `python record_kinds.py --check` runs over the build run's tip, it prints the count line with
  `0 unregistered` and a tracked count above 10,000.
  Red when: any census home of §4 is left without an admitting glob.
  figure: DERIVED at observation; the floor 10,000 is PINNED from the base census of 10,500.
- **AC3** — When `python record_kinds.py new run-state --tag record.run-state --writer hand --check
  record-kinds` runs on a fixture registry already holding the row, it exits 2 refusing the duplicate; and on the
  tip, `grep -c 'name = "run-state"\|name = "memory-index"' record-kinds.toml` prints 2.
  Red when: a residue kind is written as a hand-added row the factory never wrote, or twice.
- **AC4** — When the fixture plants a guide under the memory root's `guides` folder with a `documents.toml` row
  registering it, the arm passes it; with the row removed, it exits 1 naming the path.
  Red when: the document subtraction admits a path no document row names.
- **AC5** — When `python record_kinds.py --check` runs with the memory root pointed at an empty tracked
  directory, it exits 1 printing `record-kinds: no tracked file under`.
  Red when: an empty population passes.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/record_kinds.py · covers AC1 AC3 AC4 AC5 · the `--selftest` plants of the residue arm, its failing case the planted unregistered home passing with the subtraction widened to `memory/**` · none

## 8. Open questions

- **FACT-QUESTION · F1 — Which homes does no spec register?** Probe: `git ls-files memory` grouped by home at
  base, joined to the `home` cells and `record_kinds.py new` calls under `memory/builds/*/spec/`. The
  observation that decides it is §4 "The census". Liveness: the probe reads `memory/builds/*/RUN.md` and
  `memory/README.md` as matched by no spec, so it can produce a negative. RESOLVED (agent, 2026-11-03, delegated): `run-state` and `memory-index` are this unit's rows; the map's files take their owners' rows' homes (S4). widens: none · relaxes: none
- **F2 — Where does the residue arm run?** (a) Inside `check_record_kinds`, on the leg `record-kinds`; (b) its
  own leg. (b) adds a leg over the same registry, and a new public surface no clause names. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F3 — Are the instruction documents under the memory root records?** (a) Subtracted when a `documents.toml`
  row registers them, so one path has one registry; (b) a `document` record kind. (b) declares one path in two
  registries, against the charter's `[one-fact]` rule. Rung 3. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, from the spec brief's unit row, scout B's row and the census of §4.

## 10. Reuse audit

The seams extended: TOOL-dTotalRecall-1's `check_record_kinds` and factory `record_kinds.py new`, and
TOOL-dTotalRecall-18 S6's `check_pockets`, the common-directory residue sweep whose home predicate S1 calls over
the tracked tree, with `tracked()` (`tools/govkit/govkit.py:344`) as the listing.
`python tools/codebase-map/reuse_lookup.py "find tracked files under the memory tree that no declared home glob
matches"` ranked `tracked` and name stems (`tree`, `resolve_memory_root`); none at base joins a path to a kind,
so no existing callable fits beyond the specced `check_pockets`. Where a record and source disagreed: the brief
reads `--population` as a path list, which TOOL-dTotalRecall-1 S7 contradicts; the brief cites `decision` as
TOOL-dDeclaredLoop-31's, which is `flow.on-exhausted`, while TOOL-dLinkedLibrary-1 registers it; and scout B's
residue list is three-quarters owned (§4 "The census").

Recall terms used: `python tools/memory-recall/query.py "which record homes under memory does no record kind register" --terms "record-kind registry home glob residue unregistered RUN.md run-state check_pockets population factory"`
— its hits were the brief, scout B's row, TOOL-dTotalRecall-18's `check_pockets` criterion and
TOOL-dCalibratedLens-33's one-glob-dialect rule, which S1 follows.
