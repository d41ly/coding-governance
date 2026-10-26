# TOOL-dWellOiledMachine-16 — the journal grammar moved into the core, its runtime producer, and its retention by `runtime.journal`

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 2 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0294@41b6d311 whole
**Carries:** node:record-kind.journal
**Carries:** node:policy-key.runtime.journal
**Carries:** node:point.journal-readers

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-d.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-d.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-61 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

The core must write what observability reads (layer-runtime `[contract]`, LR:938, "the journal
grammar, moved from runlog into the core"), and today the grammar's one implementation lives in the
runlog kit, an observability kit the core may not depend on. Nothing prunes the journals
(gap-rt-16), and no line carries an act or session key (gap-rt-27). This unit makes the runtime kit
the grammar's canonical home, adds the runtime's own producer with a closed set of event classes,
each line keyed by `act=` or `session=`, and prunes every journal at the node tick as
`runtime.journal` says (v2:1221; layer-runtime `[schedule]` "Journal retention").

## 2. Scope (IN)

- **S1** — The grammar's canonical home. The journal grammar of `tools/runlog/runlog_lib.py` moves
  verbatim into `tools/runtime/journal.py` between `# >>> journal_grammar_py` and
  `# <<< journal_grammar_py`: `GRAMMAR_VERSIONS`, `MAX_LINE_BYTES`, `EVENTS`, `PAIRED_EVENTS`,
  `REQUIRED_KEYS`, `JOURNAL_DIR`, `PRODUCER_FILES`, the compiled key and time patterns,
  `JournalLine`, `Journal`, `parse_line`, `check_line`, `render_line`, `read_journal` and
  `resolve_journal_root` (`runlog_lib.py:28-66,70-75,86-292,322-340`). `runlog_lib.py` carries the
  block inline, byte-identical, held by a `journal_grammar_py` row of
  `tools/lib/resolve-python.test.sh`'s `PARITY_ROWS` with the runtime kit's file as its canonical,
  as `mempause_sh` names a kit file. `Invocation`, `build_invocations`, `SLUG_RE` and the conf
  readers stay runlog's, outside the block. Observed by AC4.
- **S2** — The redactor beside it (I12's move). `CLASS_IDS`, `TABLE_NAME`, `TABLE_COLUMNS`,
  `PLACEHOLDER_HEAD`, `Rule`, `load_rules`, `scan_secrets` and `render_redacted`
  (`runlog_lib.py:415-565`) move verbatim into `tools/runtime/redaction.py` between
  `# >>> redaction_py` and `# <<< redaction_py`, carried inline by `runlog_lib.py` under a
  `redaction_py` parity row; the table `tools/runtime/redaction.tsv` is the canonical, and
  `tools/runlog/redaction.tsv`, which each copy's `load_rules` reads beside itself, is held
  byte-identical to it, CR stripped, by `check_table_parity` in `tools/runtime/selftest.py`.
  Observed by AC5.
- **S3** — The runtime producer. `PRODUCER_FILES` gains `"runtime": "runtime.log"` inside the
  block, so both copies agree on four producers. `JOURNAL_CLASSES` in `journal.py`, outside the
  block, is the closed tuple `no-progress`, `repeat`, `budget-spent`, `deadline-passed`,
  `breaker-open`, `cycle`, `refusal`, `stall`, `compaction`, `map-read-outside-slice`,
  `secret-hit` and `hook-failure`. `write_journal_line(cls, fields, root=None)` renders
  `v=1`, `t=<epoch>`, `p=runtime`, `ev=once`, `class=<cls>` and the fields through `render_line`
  and appends the line with one write to `<git common dir>/runlog/runtime.log`. It refuses, writing
  nothing, a class outside `JOURNAL_CLASSES`, a line carrying neither `act` nor `session`, and a key
  outside the grammar: the write boundary validates once. Observed by AC1, AC2.
- **S4** — One writer per language. Python callers import `write_journal_line`; a shell or
  JavaScript producer runs `python journal.py write <class> <k=v>…` through its resolved
  interpreter, the same function behind a CLI, so no second renderer exists to drift. Exit 0
  written, 2 refused naming the rule. Observed by AC1, AC2.
- **S5** — Retention. `write_retained_lines(path, cutoff)` in `journal.py` rewrites one producer
  file keeping every line whose `t` is at or after `cutoff` and every line that does not parse,
  since a line with no readable `t` cannot be judged old, through a temp file and `os.replace`.
  `python journal.py prune [--repo <root>] [--now <epoch>]` reads `runtime.journal` through the
  policy kit's `resolve` (`tools/policy/policy.py:752`): under `all` it rewrites nothing; under
  `N` days it applies `cutoff = now - N * 86400` to each file of `PRODUCER_FILES`, printing
  `journal — pruned · <file> · <pruned> of <total> line(s)`. A refused read takes the catalogue
  default with the reason printed, never `all`. Observed by AC3.
- **S6** — The node tick. `tools/unattended/resume-tick.sh` runs the prune once per tick after its
  worktree scan, through the inline `resolve_python` block the kit's scripts already carry and the
  `resolve_kit_dir` its library defines (`tools/unattended/lib-unattended.sh:188-196` calls it the
  same way). `--dry-run` prints `journal — would prune` and rewrites nothing. A failed prune prints
  one line and leaves the tick's exit unchanged. Observed by AC6.
- **S7** — The point and the kind. `point.journal-readers` is what reads the journal (layer-runtime
  `[extend]`); its contract: a reader opens a producer file only through `read_journal` and parses
  no line itself, and `runlog` is its first reader. The `[[point]]` row is
  TOOL-dWellOiledMachine-20's to write. `record-kind.journal` is this line journal under
  `<git common dir>/runlog/`: its schema is grammar v1 and its producers `PRODUCER_FILES`; the
  memory tree's Serves kind of the same word becomes `log` (TOOL-dTotalRecall-18 §3), freeing it.
  Observed by AC4.

## 3. Non-goals (OUT)

- The six node-local grammars beside the journal that gap-rt-16 counts (health log, stall
  sidecars, task ledger, landed log, recall queries): no clause of this unit moves them.
- A native shell or JavaScript twin of the writer: one implementation behind a CLI until a hook's
  latency budget measures the spawn as too slow (`ponytail:` ceiling stated at the CLI).
- Each class's producer: the stall, loop and breaker lines are units 46, 47 and 49's, `compaction`
  unit 12's, `hook-failure` unit 10's, `map-read-outside-slice` unit 24's, `secret-hit` unit 17's
  and 57's.
- `[presets]`' pair rule bounding `runtime.journal` while observability is installed: the preset
  store's (KICK-dKeptSession-1); this unit reads the resolved value.
- An `[[adapter]]` row registering `runlog` at `point.journal-readers`: the row schema with its
  `grant` lands at units 20 and 17, and the reader contract holds without it.

### Edges

- **hands-off** `TOOL-dWellOiledMachine-61` — `scan_secrets`, in the core's `redaction.py`, which refuses a credential written into the node profile
- **hands-off** `TOOL-dWellOiledMachine-20` — `point.journal-readers`, the `[[point]]` row S7's contract becomes
- **hands-off** `TOOL-dWellOiledMachine-10` — `write_journal_line`, with the `hook-failure` class a pack that failed open journals
- **hands-off** `TOOL-dWellOiledMachine-6` — `write_journal_line`, the supervisor's journal, with the classes its own scope adds to `JOURNAL_CLASSES`
- **hands-off** `TOOL-dWellOiledMachine-12` — `write_journal_line`, with the `compaction` class
- **hands-off** `TOOL-dWellOiledMachine-24` — `write_journal_line`, with the `map-read-outside-slice` class
- **hands-off** `TOOL-dWellOiledMachine-34` — `write_journal_line` and `read_journal`, the lines `gov trace` reads by key
- **hands-off** `TOOL-dWellOiledMachine-46` — `write_journal_line`, with the `no-progress` and `repeat` classes
- **hands-off** `TOOL-dWellOiledMachine-47` — `write_journal_line`, with the `deadline-passed` and `stall` classes
- **hands-off** `TOOL-dWellOiledMachine-49` — `write_journal_line`, with the `refusal` and `breaker-open` classes

- **hands-off** `TOOL-dWellOiledMachine-53` — `write_journal_line`, with the `ledger-refused` class this unit adds
## 4. Design

### A runtime line

```
v=1	t=1793006400.25	p=runtime	ev=once	class=stall	act=act-0123456789ab	why=api-error
```

`ev=once` is the grammar's act event (`runlog_lib.py:34`), so `build_invocations` skips every
runtime line and no runlog reader changes. `class` passes the key grammar `_KEY_RE`
(`runlog_lib.py:56`).

### The prune

```
prune --repo R --now T
  value = resolve("runtime.journal", R)        # 60 by default; "all" or a day count
  all -> rewrite nothing
  N   -> for f in PRODUCER_FILES: write_retained_lines(<common>/runlog/<f>, T - N*86400)
```

`ponytail:` one rename per file, as `health_log`'s trim (`tools/lib/health_log.py:16-19`): an append
racing the rename can lose that one line; a lock file if a lost line is ever observed.

### Why a gated copy and not an import

The runlog kit is copy-installed and ships to adopters who install no runtime kit; an import would
make it require one (§8 F1). The repo's own form for a block two copy-installed kits share is the
inline copy under a parity row (`tools/lib/resolve-python.test.sh:168-186`), and a kit file may be
the canonical (`kickoff_region`, `mempause_sh`).

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `journal_grammar_py`, `redaction_py` | parity block markers and rows | `tools/runtime/journal.py`, `tools/runtime/redaction.py`, `tools/lib/resolve-python.test.sh` |
| `runtime` | producer | `PRODUCER_FILES`, inside the block |
| `JOURNAL_CLASSES` | constant | `tools/runtime/journal.py` |
| `write_journal_line`, `write_retained_lines` | functions | `tools/runtime/journal.py` |
| `write`, `prune` | CLI verbs | `journal.py` |
| `check_table_parity` | selftest arm | `tools/runtime/selftest.py` |

### Migration

None: v1 lines stay v1, a fourth producer file appears only where the runtime writes, and the first
tick's prune removes only lines older than the resolved retention.

### Files touched (estimate)

- `tools/runtime/journal.py` — S1, S3, S4, S5 (new)
- `tools/runtime/redaction.py`, `tools/runtime/redaction.tsv` — S2 (new)
- `tools/runtime/README.md` — the grammar's statement, moved from the runlog README with S7's contract
- `tools/runtime/selftest.py` — the arms in §7
- `tools/runlog/runlog_lib.py` — S1, S2: the two inline blocks
- `tools/runlog/README.md` — the grammar section points at the runtime kit's
- `tools/runlog/selftest.py` — the producer set its location arm asserts (`selftest.py:1011-1012`)
- `tools/lib/resolve-python.test.sh` — the two parity rows
- `tools/unattended/resume-tick.sh` — S6

### Alternatives rejected

- **Pruning inside `write_journal_line`.** It would prune only the runtime's file, on a write path
  with a latency budget; the tick prunes every producer once per period.
- **A grammar version 2 for runtime lines.** The class and key rule bind one producer at its own
  write boundary; every v1 reader keeps reading.

## 5. Production-readiness checklist

- security — `write_journal_line` validates class, key and field shape before any byte is written;
  values are escaped by `render_line`. A secret in a field is the caller's to redact with
  `render_redacted` before it writes.
- perf / scale — one append per line; the prune reads each file once per tick.
- error / empty / loading states — an absent journal file is `absent` and skipped; a torn or
  unparseable line is kept and counted.
- observability — the `journal — pruned` lines at each tick.
- risks — a prune racing an append can lose that one line (the `ponytail:` ceiling above).
- testing — the criteria of §6 and the arms in §7.
- migration — none (§4).
- user docs — `tools/runtime/README.md` states the grammar, the classes and the retention; the
  policy key's row already carries its summary.

## 6. Acceptance criteria

Each command runs in a scratch git repository with the runtime and policy kits on its kit path.

- **AC1** — When `python journal.py write stall act=act-0123456789ab why=x` runs, the last line of
  `runtime.log` passes `check_line`, and carries `p=runtime`, `ev=once`, `class=stall` and
  `act=act-0123456789ab`.
  Red when: the written line fails `check_line`, or lands in another producer's file.
- **AC2** — When `journal.py write bogus act=x` and `journal.py write stall why=x` run, each exits 2,
  the first naming `JOURNAL_CLASSES` and the second `act or session`, and `runtime.log` is unchanged.
  Red when: either writes a line.
- **AC3** — When `journal.py prune --now <T>` runs with `runtime.journal = 60` over a `runtime.log`
  holding a line at 59 days before `T`, one at 61 days and one torn line, the 61-day line is gone and
  the other two stay; under `runtime.journal = "all"` all three stay.
  Red when: a pruner stubbed to rewrite every file empty passes, or the torn line is removed.
  figure: the day offsets are PINNED by the fixture against `--now`, never against the clock.
- **AC4** — When `python -c "import runlog_lib as r, journal as j; print(sorted(r.PRODUCER_FILES) ==
  sorted(j.PRODUCER_FILES), r.render_line({'v': '1', 't': '1', 'p': 'x', 'ev': 'once'}) ==
  j.render_line({'v': '1', 't': '1', 'p': 'x', 'ev': 'once'}))"` runs with both kits on its path,
  it prints `True True`, and the `journal_grammar_py` parity row finds `runlog_lib.py` byte-identical
  to `journal.py`'s block.
  Red when: one byte of `runlog_lib.py`'s block differs from the canonical and the row stays green.
- **AC5** — When `check_table_parity` runs, the two `redaction.tsv` copies compare equal and
  `redaction.scan_secrets('Authorization: Bearer abcdefghijklmnop')` names `auth-header`; with
  one row of the runlog copy edited, it fails naming the row.
  Red when: an edited copy passes.
- **AC6** — When `bash resume-tick.sh --repo <scratch>` runs over a scratch clone whose `runtime.log`
  holds a line older than the resolved retention, the line is gone and the tick exits 0; with
  `--dry-run` the line stays and `journal — would prune` is printed.
  Red when: the old line survives a real tick, or a dry run rewrites the file.

## 7. Gates

`runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures`

The broad guards `{prefix}/` and `{prefix}/lib/` leave the line by the checker's floor; the
`python resolver (behaviour + inline parity + idiom ban)` leg reads the two new parity rows, and the
bar at the close runs it with the rest.

New arm: tools/runtime/selftest.py · covers AC1 AC2 AC3 AC5 AC6 · a scratch repository per case: an unknown class, a keyless line, a fixture journal with dated and torn lines under each retention value, an edited table copy, and a scratch clone for the tick · none
New arm: tools/lib/resolve-python.test.sh · covers AC4 · the `journal_grammar_py` and `redaction_py` rows, staged by one byte changed in `runlog_lib.py`'s copy · none
New arm: tools/runlog/selftest.py · covers AC4 · the location arm's producer set, now four, staged by the old three-producer literal · none

## 8. Open questions

- **F1 — How does the runlog kit read a grammar whose home is the core?** (a) It imports
  `journal.py` through `resolve_kit_dir`, its descriptor gaining `requires = ["runtime"]`; (b) it
  carries the grammar inline, byte-identical to the core's canonical block under a parity row;
  (c) the grammar stays in runlog and the core imports it. (c) makes the core depend on an
  observability kit, which v2 P28 refuses ("expansions meet only through the core"), and fails the
  clause. (a) makes every adopter that installs runlog install the runtime kit, a public-surface
  change veto 2 refuses outside the grant. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3,
  the one survivor, the repository's own form for a block two copy-installed kits share; runlog's
  readers keep importing `runlog_lib`, whose grammar is the core's gated copy, so no reader parses a
  line itself. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended: runlog's grammar and redactor (`tools/runlog/runlog_lib.py:28-340`, `:415-565`),
moved rather than rewritten; the parity table (`tools/lib/resolve-python.test.sh:168-186`); the
health log's trim-by-rename (`tools/lib/health_log.py:9-21`) for the prune's write; `resolve`
(`tools/policy/policy.py:752`) for the key, whose row is `tools/policy/catalogue.toml:511-516`;
the shell sibling load `resolve_index_generator` (`tools/unattended/lib-unattended.sh:188`) for the
tick's call. `python tools/codebase-map/reuse_lookup.py "append one journal line and prune journal
lines older than a retention"` ranked `read_journal`, `check_line`, `render_line` and
`resolve_journal_root` in `runlog_lib.py`, the grammar this unit moves, and found no pruner: the
30-day mtime prune at `tools/run-gates/run-gates.sh:5455` is the reuse cache's, not a journal's,
as scout D reads it. Scout D's rows hold against source.

Recall terms used: `python tools/memory-recall/query.py "where does the run log journal grammar live and who prunes the journal" --terms "runlog journal grammar runlog_lib parse_line render_line producer driver gates pushes retention prune"`
