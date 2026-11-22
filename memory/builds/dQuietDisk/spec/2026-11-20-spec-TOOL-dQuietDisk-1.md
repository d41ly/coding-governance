# TOOL-dQuietDisk-1 — one store of immutable history verdicts, keyed by the ids each one reads, with one `cat-file --batch` reader

**Status:** CLOSED · rev-4 · 2026-11-22 · node d · Tier-2 · base e4699ee7 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-build-TOOL-dQuietDisk-1-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-1-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-1-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-1-deviation-1.md) | deviation | — |
| [2026-11-22-build-TOOL-dQuietDisk-1-red-fix-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-1-red-fix-1.md) | red-fix | — |
| [2026-11-22-build-TOOL-dQuietDisk-1-red-fix-2.md](../build/2026-11-22-build-TOOL-dQuietDisk-1-red-fix-2.md) | red-fix | — |
| [2026-11-22-build-TOOL-dQuietDisk-1-red-fix-3.md](../build/2026-11-22-build-TOOL-dQuietDisk-1-red-fix-3.md) | red-fix | — |
| [2026-11-22-build-TOOL-dQuietDisk-1-widen-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-1-widen-1.md) | widen | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-2-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-2-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-3-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-3-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-2-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-2-task.md) | research | TOOL-dQuietDisk-7 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task.md) | research | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-owner-build-on-land-branch.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-owner-build-on-land-branch.md) | research | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task.md) | research | TOOL-dQuietDisk-14 TOOL-dQuietDisk-9 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

The history legs regrade all of history on every commit and ask git one process per question
(`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, row G3 and
rework K5, K6). This unit builds the two shared pieces units 2 to 4 consume. The first is a store
of immutable per-item verdicts under the git common dir, keyed by the commit and blob ids an item
reads and by the grading code's own bytes, with a last graded tip per leg. The second is one
`git cat-file --batch` reader per leg run. The unit wires no leg to them, so no verdict moves here.

## 2. Scope (IN)

- **S1** — `tools/lib/history_store.py`, the canonical module. Its body sits inside one marked
  block, `history_store_py`, as `tools/lib/legacy_ledger.py` holds its own. It defines
  `BatchReader`, `resolve_store` and the store class section 4 names. Observed by AC1, AC2, AC3 and
  AC4.
- **S2** — `BatchReader(repo)` holds one `git -C <repo> cat-file --batch` process, started on the
  first question. `read(name)` answers the object's bytes or None, and `read_info(name)` answers its
  oid, type and size or None. A `missing` or `ambiguous` reply is None. An end of stream or a
  malformed header is a dead process: the reader restarts it once, and after a second death it
  answers each question by a one-shot `git cat-file` spawn. A dead process is never read as
  missing. Observed by AC1 and AC2.
- **S3** — `resolve_store(repo, leg, code_paths)` returns the store for one leg run. Its root is
  `<git common dir>/history-verdicts/v1/<leg>/`, beside the reuse cache's `gate-cache`. An item is
  one file under `items/<key[0:2]>/<key>`. A key is the SHA-256 of the schema tag, the leg, the
  code digest and the caller's id fields. The code digest hashes the working bytes of every path
  in `code_paths`, so an edit to the checker or to a library it sources moves every key. A code
  path that cannot be read disables the store for that run. Observed by AC3.
- **S4** — An item file opens with one header line naming the schema tag, its key and its body
  length. A missing, unreadable, truncated or foreign-version file reads as a miss, never as a
  verdict. Every write goes to a sibling temp file that `tempfile.mkstemp` names in the item's own
  directory, then `os.replace`, as the reuse cache's writer does. So two bars that write the same
  key or different keys at once lose nothing and leave no temp file. Observed by AC3 and AC4.
- **S5** — The tip. `read_tip()` and `write_tip(sha)` keep the leg's last graded tip in
  `tips/<scope>`, where the scope is the first 16 hex of the SHA-256 of the absolute git dir. Each
  worktree keeps its own tip and every worktree shares the items. Observed by AC5.
- **S6** — `remove_aged()` unlinks each item file older than 30 days by mtime, in the calling process. It
  runs at most once per 24 hours per leg, recorded by the mtime of a `pruned` stamp, so a warm run
  never lists the store. Observed by AC6.
- **S7** — The switch. `resolve_store` reads the policy key `tests.history-verdicts` once, through the
  policy kit's `policy.py get`, found by the module's inline `resolve_kit_dir` block. `stored`, the
  default, is the store. `regraded` is today's behaviour: every `read` misses, `write` and
  `write_tip` write nothing, and `read_tip` answers None. An absent policy kit or an unreadable key
  reads as the default. The key lands with its catalogue row in `tools/policy/catalogue.toml`,
  `owner = "dQuietDisk"`, with a `summary` and a `usage`, and `help/reference/policy.md` is
  re-rendered from it. Observed by AC7.
- **S8** — The bash face, `tools/lib/history-store.sh`, the canonical block `history_store_sh`. It
  defines `init_hs`, `read_hs_tip`, `read_hs_items` and `write_hs_items`, which call the module's CLI
  once each, and `init_bh`, `read_bh_info`, `read_bh_blob` and `remove_bh` over one `coproc` of
  `git cat-file --batch`. `read_bh_blob` reads under `LC_ALL=C` and returns 3 when the bytes read differ
  from the header's size, which a blob holding a NUL causes. Observed by AC8.
- **S9** — The CLI, `python history_store.py --leg <leg> --code <path>... <verb>`. `tip` prints the
  tip. `lookup` reads `<item id>TAB<field>...` lines and prints `<item id>TAB<hit|miss>TAB<body>`.
  `store --tip <sha>` reads `<item id>TAB<field>...TAB<body>` lines, writes each item, then the tip,
  then prunes. A body is escaped one way, `\\`, `\t` and `\n`, defined once in the module. Observed
  by AC8.
- **S10** — The copies. `tools/unattended/history_store.py` and `tools/memory-tree/history_store.py`
  carry the module whole, and `tools/unattended/lib-unattended.sh` carries the `history_store_sh`
  block, so the two copy-installed kits units 2 to 4 grade inside hold their own copies. Two rows
  join `PARITY_ROWS` in `tools/lib/resolve-python.test.sh`, one per block. The module also carries
  the `git_env_leaks_py` block inline (section 4, the environment of every git child), whose
  existing row already grades every file carrying its marker. Observed by AC9.
- **S11** — `python tools/lib/history_store.py --selftest` runs the module's arms in its own scratch
  repository, printing one line per arm and a count line. A held leg,
  `history-store selftest`, runs it, with subject `kit`, chunk `selftests`, a ceiling of 120 s and a
  guard naming the module and the bash face. `tools/lib/` is no kit: it has no `kit.toml`, and the
  registry exempts it (`tools/govkit/registry.toml@e4699ee75:253`). So the leg is declared as an
  `[[exempt_leg]]` row of `tools/govkit/registry.toml`, in the shape of the
  `python resolver (behaviour + inline parity + idiom ban)` row, and `tools/gate-legs.json` is
  re-rendered from the declarations by `python tools/run-gates/leg_factory.py --write`, never edited
  by hand. Because every held leg must carry a budget row, the leg's row joins
  `tools/run-gates/selftest-budgets.txt`. A role agent runs no `--selftest`, so the row is a PINNED
  estimate from a proxy reading: the wall time of one timed run of section 6's probes, times 1.5,
  floored at 60 s. Its note says it is not a `--selftest` reading and names the proxy, as the
  `leg-factory selftest` and `ratchet selftest` rows do. The main loop re-prices it from the first
  measured run at the close. Observed by AC10 and AC12.
- **S12** — The shell-line ledger. The bash face stays, because units 2 and 3 are its bash
  consumers. `memory/project/shell-role.txt` is shrink-only, read by the unguarded leg
  `portability (shell lines only shrink)`. Three of its keys grow here: the new
  `tools/lib/history-store.sh`, which has no row, and `tools/unattended/lib-unattended.sh` and
  `tools/lib/resolve-python.test.sh`. They are widened through the ledger factory's widen door,
  `python tools/memory-tree/ratchet.py widen shell-role --key <path> --key <path> --key <path>
  --reason <one line> --unit TOOL-dQuietDisk-1`, as dWitnessedBar's units 58 and 60 widened theirs
  (`memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-60-widen-4.md`). The door
  writes the next widen record of this build under `memory/builds/dQuietDisk/build/`, then each
  row `widened:<record stem>` (`tools/memory-tree/ratchet.py@e4699ee75:33`); no row is
  hand-edited. The record's one-line Reason states two figures apart for each key. The first is
  the lines this unit adds. The second is the base excess the merge `e4699ee75` already carried,
  none for the new file: the pass's reading gave 1557 lines against the row's 1420 for
  `tools/lib/resolve-python.test.sh`, and 1331 against 1319 for `tools/unattended/lib-unattended.sh`
  (`2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-2-task`). The base excess comes from
  dWitnessedBar's land tip. When the run re-merges main after dWitnessedBar's landing, it
  re-measures each row and amends the record. A row for a file this unit does not touch is not
  this unit's, and no widen names one. Observed by AC13.

## 3. Non-goals (OUT)

- No leg is wired to the store or the reader. `check-pass-order.sh`, `check-brief-recorded.sh` and
  `routed_commits.py` are units 2, 3 and 4.
- No change to the reuse cache's key. The `head $RG_HEAD` line of `build_key_text`
  (`tools/run-gates/run-gates.sh@e4699ee75:3553`) stays: a history leg's whole-run verdict does
  depend on HEAD, and the store makes the leg cheap rather than reusable across commits.
- No migration of the existing coprocesses. `upgrade_steps.py#derive_introduced` and
  `tools/drift-audit/drift_report.py` hold their own `--batch` process, and
  `routed_commits.py` and `tools/lexicon/lexicon.py` send one batch per question set, which is
  already one process. Moving them is the unit that owns each file, or a later ask.
- No `--batch-command`. It needs git 2.36, this repository declares no git floor, and an adopter on
  an older git would lose the reader. `--batch` answers both questions.
- No kit version bump by hand. `govkit.py mint` writes every owed bump at the lander.
- No second sweeper and no store under `gate-cache`. The reuse cache's 30-day prune lists all of
  `gate-cache` on every bar (analysis row G6), which this store's daily stamp avoids.

### Edges

- **hands-off** `TOOL-dQuietDisk-2` — wiring the pass-order leg to the store, its items and its tip,
  through the bash face this unit puts in the unattended kit's library
- **hands-off** `TOOL-dQuietDisk-3` — wiring the brief-recorded leg to the store, and persisting its
  subject cache through it
- **hands-off** `TOOL-dQuietDisk-4` — wiring the routed-commits leg to the store and the reader,
  through the memory-tree kit's copy of the module

## 4. Design

### Where the code was read

Every citation is at `e4699ee75`, the build base: the merge that brought dWitnessedBar's land tip
`ed833f684` into this run, as the owner ruled on 2026-11-22. A citation is written
`<path>@e4699ee75:<line>` or by symbol.

### The seams this extends

- The reuse cache lives at `$RG_COMMON_RAW/gate-cache`
  (`tools/run-gates/run-gates.sh@e4699ee75:3651`), one file per entry under `<key[0:2]>/<key>`.
  Its writer is one python block that opens at `tools/run-gates/run-gates.sh@e4699ee75:5988`; it
  stages each entry through `tempfile.mkstemp` in the entry's directory and moves it with
  `os.replace` (`tools/run-gates/run-gates.sh@e4699ee75:6029`). The store takes the same home,
  layout and write rule, under its own directory.
- The one revision-blob reader is `upgrade_steps.py#blob_at`. Its batch branch writes
  `<commit>:<path>` and reads the `<oid> <type> <size>` header and `size + 1` bytes. It reads a
  short header as None, so an end of stream reads as "no such blob". `BatchReader` keeps the header
  parse and separates the two answers (S2).
- The copy rule. `tools/lib/` ships nothing (`tools/govkit/registry.toml@e4699ee75:253`), so a
  copy-installed kit carries a shared primitive inline, gated by `PARITY_ROWS` in
  `tools/lib/resolve-python.test.sh@e4699ee75:405`. `tools/lib/legacy_ledger.py` with its copies in
  `tools/gate-lint/` and `tools/memory-tree/` is the whole-module precedent, and
  `tools/unattended/commit_trailers.py` the unattended kit's.
- The live-generation shape of TOOL-aPiecewiseGrade-1 S4 is not needed here. Its entries are
  findings that a later run may replace; these items are immutable per key, so a reader never sees
  a half-promoted generation, and a lost tip only costs a regrade.

### Data model

```text
<git common dir>/history-verdicts/v1/<leg>/
  items/<key[0:2]>/<key>     history-verdict v1 <key> <body length>\n<body bytes>
  tips/<scope>               sha\t<40-hex tip>\n
  pruned                     empty; its mtime is the last prune
key   = sha256("history-verdict v1\n" + leg + "\n" + code digest + "\n" + "\n".join(fields))
code  = sha256 over sorted "<path>\0<sha256 of its working bytes>\n" for each code path
scope = sha256(absolute git dir)[:16]
```

`<leg>` is the caller's leg slug, `[a-z0-9-]+`, refused otherwise. A field holding a newline is
refused, so two field lists never join to one key text.

### The reader's protocol

| Reply | `read` | `info` |
|---|---|---|
| `<oid> <type> <size>` then the bytes | the bytes | the three fields |
| `<name> missing` or `<name> ambiguous` | None | None |
| end of stream, or a header that does not parse | restart once, then a one-shot spawn | the same |
| a name holding a newline | a one-shot spawn, since the protocol is line-framed | the same |

The one-shot spawn is the safe fallback, not a second reader. It runs `git cat-file -t <name>` for
the type and `git cat-file <type> <name>` for the bytes, whose length is the size. For `read_info`
alone it then takes the oid from `git rev-parse --verify --quiet <name>`, never from
`cat-file -t`, which prints no oid. Neither the batch header nor `rev-parse` peels, so both name the
same object. The `<name>^{object}` form is not used: in a `<rev>:<path>` name the suffix is read as
part of the path, so `HEAD:a.txt^{object}` asks for a file of that name. `--batch-check` is not
used either, since it would be a second process beside the held one.

### The environment of every git child

The module carries the `git_env_leaks_py` block inline, byte-identical to
`tools/lib/git_env_leaks.py`. Every git child it starts runs under this process's environment less
`GIT_ENV_LEAKS`: the held `--batch` process, the one-shot spawn, the store's `rev-parse`, and the
selftest's calls in its scratch repository. So a `GIT_DIR` that a hook exports never points a
`-C <repo>` call at gov's own repository, and never points the selftest's scratch-repo calls there.
The commit-trailer readers drop the same names (`tools/lib/commit_trailers.py@e4699ee75:143`). The
block's existing `PARITY_ROWS` row, `git_env_leaks_py`
(`tools/lib/resolve-python.test.sh@e4699ee75:422`), finds its copies by marker over the tracked tree
(`tools/lib/resolve-python.test.sh@e4699ee75:540`). So all three `history_store.py` files are graded
against the canonical copy, and no row is added for them.

### The bash face

`init_hs <leg> <code path>...` resolves python through the caller's inline `resolve_python`, which
both legs already carry, and keeps the leg and code list for the three CLI calls. `read_hs_items`
and `write_hs_items` take one file each, so a leg pays one python process to read all its items and
one to write them, whatever the unit count. `init_bh` starts the coprocess, `read_bh_info` and
`read_bh_blob` set `BH_OID`, `BH_TYPE`, `BH_SIZE` and `BH_TEXT`, and `remove_bh` closes it. A dead
coprocess returns 2 from both, and the caller grades that question as it does today.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `tests.history-verdicts` | policy key, values `stored` and `regraded` | the catalogue | `policy.py check` |
| `history_store_py`, `history_store_sh` | parity block markers | `PARITY_ROWS` | `tools/lib/resolve-python.test.sh` |
| `BatchReader`, `HistoryStore` | Python classes | `py.type`, lexicon `--suggest` OK | the module's `--selftest` |
| `resolve_store` | Python function | `py.function`, lexicon `--suggest` OK | the module's `--selftest` |
| `derive_git_env` | Python function, the environment less `GIT_ENV_LEAKS` | `py.function`, lexicon `--suggest` OK | the module's `--selftest` |
| `read`, `read_info` | `BatchReader` methods | `py.function`, lexicon `--suggest` OK | the module's `--selftest` |
| `read`, `write`, `read_tip`, `write_tip`, `remove_aged` | `HistoryStore` methods | `py.function`, lexicon `--suggest` OK | the module's `--selftest` |
| `init_hs`, `read_hs_tip`, `read_hs_items`, `write_hs_items` | shell functions | `sh.function`, lexicon `--suggest` OK | the module's `--selftest` |
| `init_bh`, `read_bh_info`, `read_bh_blob`, `remove_bh` | shell functions | `sh.function`, lexicon `--suggest` OK | the module's `--selftest` |
| `tip`, `lookup`, `store` | CLI verbs | none: the lexicon declares no cell for a CLI verb | the module's `--selftest` |
| `history-store selftest` | gate leg, an `[[exempt_leg]]` row | `tools/govkit/registry.toml` | `gate-leg conformance` |
| `history-verdicts/` | directory under the git common dir | none | the module's `--selftest` |

`.lexicon.conf` pins `VERB_OFFENDER_PIN` at the full offender count, so every function, method and
shell function above leads with a declared verb, checked by
`python tools/lexicon/lexicon.py --suggest <name> --as <cell>`. A method is graded as a function, a
dunder included, so neither class defines `__enter__` or `__exit__`.

### Files touched (estimate)

`tools/lib/history_store.py` · `tools/lib/history-store.sh` · `tools/unattended/history_store.py` ·
`tools/memory-tree/history_store.py` · `tools/unattended/lib-unattended.sh` ·
`tools/lib/resolve-python.test.sh` · `tools/policy/catalogue.toml` · `help/reference/policy.md` ·
`tools/govkit/registry.toml` · `tools/gate-legs.json` · `tools/run-gates/selftest-budgets.txt` ·
`memory/guides/SESSION-KICKOFF.md` · `memory/project/shell-role.txt` ·
`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-1-widen-1.md`

The widen record's name is the door's: its date is the day the pass runs it, and its number is one
past the highest widen record in the build folder (`tools/memory-tree/build_records.py@e4699ee75:892`),
which holds none at this revision, so `1`.

The leg's declaration is the `[[exempt_leg]]` row in `tools/govkit/registry.toml`, and
`tools/gate-legs.json` is the manifest `python tools/run-gates/leg_factory.py --write` re-renders
from it. The kickoff manifest's `watch:` line names `tools/gate-legs.json`, so the commit that adds the leg
re-stamps the manifest's `last-audit`. A new file under `tools/unattended/` and
`tools/memory-tree/` is claimed by each kit's `include = "**"` row
(`tools/unattended/kit.toml@e4699ee75:26`, `tools/memory-tree/kit.toml@e4699ee75:30`).
`tools/run-gates/selftest-budgets.txt` is asserted both ways, so a held leg with no row is a
failure (its header, `tools/run-gates/selftest-budgets.txt@e4699ee75:16`).

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Items inside `gate-cache` | That directory is listed and stat-ed whole on every prune, 11,442 files measured (analysis row G6), and its schema constant belongs to the runner. |
| One SQLite file | Two bars finishing together contend on one lock, and a torn write costs the whole store rather than one item. |
| An append-only TSV | Readers must scan it, and two writers need a lock. A file per key is lock-free by rename. |
| Keying the code by its index blob | An uncommitted edit to a checker would reuse verdicts its old bytes earned. |
| A bash-native key | Hashing each item in bash costs a process per item, which is the cost this unit removes. |

## 5. Production-readiness checklist

- security: the store is under the git common dir, never pushed, never a ref and never rendered.
  It holds a leg's own outcome text and no secret. A forged item can only make a leg report what
  the forger wrote, which needs write access to `.git` already.
- perf / scale: a warm leg pays one `rev-parse`, one `cat-file --batch` and two python processes.
  The prune lists the store once a day.
- error / empty / loading states: every store failure is a miss and every reader failure falls
  back to a spawn. The table in section 4 is the contract.
- observability: the CLI's `lookup` prints one stderr line, `history-store: <leg> <hits> hit(s),
  <misses> miss(es)`.
- risks: the gotcha classes `append-without-an-idempotence-key`,
  `suite-invalidated-by-a-commit-under-it`, `history-leg-graded-before-the-reconcile-commit` and
  `test-oracle-read-from-a-historical-sha` were read. The first is closed by a write per key. The
  second and fourth are the consumers', which units 2 to 4 answer. The third is why the key holds
  ids and never HEAD.
- testing: the module's `--selftest` and the probes of section 6.
- migration: N/A — a new store; a missing root is an empty store.
- user docs: the policy key's help row is rendered from its catalogue row.

## 6. Acceptance criteria

- **AC1** — When a probe builds a repository under `%TEMP%/<short-name>` with 50 committed files,
  sets `GIT_TRACE2_EVENT` to an empty directory, and reads every file through one
  `BatchReader`, each answer equals `git show HEAD:<path>`, and `read_info` of `HEAD:absent` is None.
  The trace directory then holds exactly one file whose `cmd_name` event names `cat-file`.
  Red when: the reader spawns per question, so the directory holds 50 or more such files.
  figure: PINNED, one process for 50 questions.
- **AC2** — When the probe kills the reader's process between two `read` calls, and then again
  after the restart, the next `read` of an existing blob still returns its bytes.
  Red when: an end of stream is read as `missing` and `read` answers None.
- **AC3** — When the probe writes an item with `write`, `read` returns its body. It reads None after
  the file is cut one byte short, after its header's tag is changed to `v2`, and, for a fresh store,
  after one byte of a `code_paths` file changes. The probe prints one line per case.
  Red when: a truncated or foreign entry is returned, or a code edit leaves the key unchanged.
- **AC4** — When two processes each write the same 200 keys and 200 keys of their own into one store
  at once, every one of the 600 items reads back with its body, and no `*.tmp` file remains.
  Red when: a write goes to the final path directly, so a reader sees a partial item or a temp is
  left.
- **AC5** — When the probe runs `git worktree add` on its repository, a tip written from each
  worktree reads back only in that worktree, and an item written from one is a hit in the other.
  Red when: the scope is the common dir, so the second tip overwrites the first.
- **AC6** — When the probe plants an item with an mtime 31 days old and one 29 days old and runs
  `store`, the old one is gone and the young one stays. A second old item planted after it
  survives a second `store` within the hour.
  Red when: the prune runs on every call, or removes by name rather than by age.
- **AC7** — When the probe's repository commits `.governance/policy.toml` holding
  `tests.history-verdicts = "regraded"`, the `lookup` CLI prints `miss` for an item written
  under `stored`, and `store` leaves the item tree and the tip unchanged. With the file removed it
  prints `hit`. `python tools/policy/policy.py check` passes over the catalogue.
  Red when: the switch is not read, or its off value still reads or writes.
  fixture: the policy kit beside the module, as `tools/policy/` sits in gov.
- **AC8** — When a bash probe sources `history-store.sh` from `tools/lib/` and reads a blob through
  `read_bh_blob`, `BH_TEXT` equals the blob. A blob holding a NUL returns 3. `read_hs_items` over a
  body holding a tab, a newline and a backslash, stored through `write_hs_items`, prints it back
  escaped and unescapes to the same bytes.
  Red when: the bash face reads characters rather than bytes, or the escape is not reversible.
- **AC9** — When the marked blocks are extracted with the parity table's own `blk` awk from the
  canonical files and from each copy, every pair compares equal. The `git_env_leaks_py` block
  extracted from each of the three `history_store.py` files equals the one in
  `tools/lib/git_env_leaks.py`.
  Red when: a copy drifts by one byte, which the two new `PARITY_ROWS` rows, or the existing
  `git_env_leaks_py` row, then report.
- **AC10** — When the main loop runs `python history_store.py --selftest` in `tools/lib/` at the close, it
  prints one line per arm and a count line, and exits 0. With `read` patched to answer None on an
  end of stream, it exits 1.
  Red when: the selftest passes over the patched reader.
  permission: a role agent runs no `--selftest` (scratch-guard row G3). This is the first `New arm:`
  line's RED and GREEN observation, owed to the main loop. The pass's proxy is AC1 to AC8, whose
  probes call the module's functions and the bash face directly.
- **AC11** — When `python tools/govkit/govkit.py shipped` runs, it lists the copy
  `history_store.py` under both `unattended` and `memory-tree`. When `python tools/govkit/govkit.py check --target C:/projects/incms/main`
  and the same with `C:/projects/nicocares/main` run read-only from gov before and after the unit,
  each prints the same bytes and exit code.
  Red when: a copy is not claimed by its kit, or the check reads differently.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
  fixture: the adopters reach the copies only after a minted version and their own `govkit update`.
- **AC12** — When `grep -n "^history-store selftest" tools/run-gates/selftest-budgets.txt` runs, it
  prints one row whose budget is at least 60 and whose note says it is a PINNED estimate from the
  timed section 6 probes, not a `--selftest` reading, to be re-priced from the first measured run.
  When `grep -n -A12 'name = "history-store selftest"' tools/govkit/registry.toml` runs, it prints
  an `[[exempt_leg]]` row holding `ceiling = 120`, and
  `grep -n -A16 '"name": "history-store selftest"' tools/gate-legs.json` prints the rendered row
  holding `"ceiling": 120`.
  Red when: the held leg lands with no budget row, a budget under the floor, a note that claims a
  direct reading, no ceiling, or a manifest row with no declaration behind it.
  figure: PINNED, the budget from the pass's timed run of the section 6 probes, times 1.5, floored at
  60 s. The re-price from the first measured run of the leg at the close is owed to the main loop,
  as the `leg-factory selftest` and `ratchet selftest` rows' are.
- **AC13** — When
  `grep -n -E "^tools/(lib/history-store\.sh|unattended/lib-unattended\.sh|lib/resolve-python\.test\.sh)\s" memory/project/shell-role.txt`
  runs after the widen, it prints three rows, each ending `widened:<stem>` for one record stem. That
  stem names a file under `memory/builds/dQuietDisk/build/` whose Keys field lists exactly those
  three paths, whose Caused-by is `TOOL-dQuietDisk-1`, and whose Reason gives, for each key, the lines
  this unit adds and the base excess as two numbers. `git diff --stat -- memory/project/shell-role.txt`
  shows those three rows and no other.
  Red when: a row is edited by hand with no record, a row for a file this unit does not touch moves,
  or the Reason folds the base excess into this unit's own figure.

This unit moves no verdict: it adds no reader to any existing leg, so every leg's rc and output stay
as they were. The process saving is each consumer's, counted in units 2, 3 and 4.

## 7. Gates

`kit epoch (shipped bytes move, the version moves)` · `history-store selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `gate-leg conformance` · `python resolver (behaviour + inline parity + idiom ban)` · `every held leg is budgeted, every budget row resolves` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `branch-guard self-test` · `tier2-review self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `drift-audit selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `playbook render selftest` · `portability (shell lines only shrink)` · `ratchet (never gains)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

The leg line names `history-store selftest`, the leg S11 adds, because the module and the bash face
trip its guard. On a tree without this unit's code, `tools/gate-legs.json` holds no such leg, so the
spec-token checker reads that name as unresolved until the pass's code is in the tree. Any
`--dispatch` that widens this pass's write set runs after the code is applied, never before.

New arm: tools/lib/history_store.py · covers AC3 AC10 · the module's --selftest; its failing case is staged by reading an end of stream as missing, or by keying on the index blob of a code path · none
New arm: tools/lib/resolve-python.test.sh · covers AC9 · the two new PARITY_ROWS rows; their failing case is staged by one changed byte in either copy · none

The bar runs once at the close. The new leg's RED and GREEN observation is the main loop's, and so
is the budget row's re-price from that first measured run. No criterion has the pass run a suite,
a `--selftest`, a gate leg or the bar.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Order 1, as briefed: the write set is disjoint from
  TOOL-dQuietDisk-14's, the other order-1 unit, and units 2 to 4 consume it at order 2.
- rev-2 · 2026-11-22 · re-grounded at e4699ee75 (dWitnessedBar's land tip merged), under
  `2026-11-22-prompt-TOOL-dQuietDisk-1-reground-task`. What moved: every `run-gates.sh` citation
  (the `head $RG_HEAD` line to 3553, the cache home to 3651, its writer to 5988 and 6029), the
  registry's `{prefix}/lib` exemption to line 253, and the base to `e4699ee7`. S4 names the
  `mkstemp` staging the reuse cache's writer uses. S11 and AC12 add the leg's ceiling and its
  budget row, which `tools/run-gates/selftest-budgets.txt` demands of every held leg and which
  rev-1 missed. No dWitnessedBar unit built after `609cd40b1` holds a history store or a batch
  reader (section 10), so the design is otherwise unchanged.
- rev-3 · 2026-11-22 · the three divergences the first build pass handed back, under
  `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. (a) Every minted name the lexicon refused
  now leads with a declared verb, each checked by `--suggest`: `open_store` is `resolve_store`; the
  store's `get`, `put` and `prune` are `read`, `write` and `remove_aged`; `BatchReader.info` is
  `read_info`; and the eight shell functions are `init_hs`, `read_hs_tip`, `read_hs_items`,
  `write_hs_items`, `init_bh`, `read_bh_info`, `read_bh_blob` and `remove_bh`. The Inventory names
  each cell. (b) S11 and AC12 price the budget row as a PINNED estimate from a timed run of the
  section 6 probes, floored at 60 s, with the re-price owed to the main loop; AC3 no longer has the
  pass run the `--selftest`, and AC10 is the main loop's observation. (c) The leg is an
  `[[exempt_leg]]` row of `tools/govkit/registry.toml`, which joins Files touched, with
  `tools/gate-legs.json` re-rendered by `leg_factory.py --write`.
- rev-4 · 2026-11-22 · S10 · S12 · §4 · AC9 · AC13 · §7 · the second pass's refusal at `--dispatch`
  check 49, as ruled, under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-2-task`. (1) §7's leg
  line names `history-store selftest`, whose guard the module and the bash face trip, beside
  `portability (shell lines only shrink)` and `ratchet (never gains)`, which grade the ledger S12
  widens. (2) S12 keeps the bash face and widens its three shell-role rows through
  `ratchet.py widen shell-role`. The record states this unit's added lines and the base excess
  `e4699ee75` carried as separate figures, and Files touched gains the ledger and the record. (3) The
  reader's protocol spells the one-shot oid as `git rev-parse --verify --quiet <name>`, never
  `cat-file -t`, and says why neither `^{object}` nor `--batch-check` is used. (4) A new §4
  subsection states that the module carries `git_env_leaks_py` inline and starts every git child,
  including the selftest's, without those names. The block's existing parity row grades the three
  copies, which AC9 now observes, and the Inventory names `derive_git_env`.

## 10. Reuse audit

The seams extended: the reuse cache's home and write rule (`tools/run-gates/run-gates.sh`, the
`REUSE_CACHE` block, TOOL-aSparedSpawn-13), the batch protocol of `upgrade_steps.py#blob_at`, and
the copy rule of `PARITY_ROWS` with `tools/lib/legacy_ledger.py` as its whole-module precedent.
`tools/lib/` holds no `cat-file` reader at the base: `git grep -n "cat-file" e4699ee75 -- tools/lib/`
prints nothing. The three files `tools/lib/` gained since `609cd40b1` are `gov-feed.sh`,
`gov-ref.sh` and `home_graded.py`; none is a store or a reader. The existing readers are `upgrade_steps.py#derive_introduced`'s held process,
`tools/drift-audit/drift_report.py`'s, and the one-shot batches of `routed_commits.py` and
`tools/lexicon/lexicon.py`. The brief's "already hold coprocesses" is stale for the last two: each
sends its whole question set to one `run_git` call and holds no process. No existing seam fits
the store itself beyond the reuse cache's layout, whose directory it must not share (section 4).

`python tools/codebase-map/reuse_lookup.py "cache a history leg verdict by the commit and blob ids it reads"`
ranked only name-token neighbours (`read_text`, `read`, `ids`, `legs`), none a store.
`python tools/codebase-map/reuse_lookup.py "read many git objects through one cat-file batch process"`
ranked `git`, `run_git` and `read_git`, each a one-shot spawn helper.

Recall returned TOOL-dUnstuckLanding-7 and -17, the RANGE-mode history legs, TOOL-aSmoothedDispatch-20,
the routed-commits leg outgrowing its ceiling with no push base, and TOOL-dScopedBuild-14's reuse
scout naming the deviation join's policy read. Owning chain builds: dWitnessedBar (Test: gate
health, the reuse cache) and dScopedBuild (Build: the history-derived exit base), whose legs this
store serves. No dWitnessedBar spec defines a history store, at `609cd40b1` or at `e4699ee75`.
The re-ground read `git log 609cd40b1..ed833f684` over `tools/lib/`, `run-gates.sh`,
`verdict_flow.py`, `lib-unattended.sh` and `routed_commits.py`, and the five dWitnessedBar specs
added since, units 106 to 110. `verdict_flow.py` holds the flake ledger, the quarantine and the
red routing, and none of it keys a verdict by the ids a history item reads. The only file that
newly runs `cat-file --batch` is `tools/unattended/unattended.test.sh`, a one-shot listing in a
fixture. So there is no store to extend and no reader to fold in. Every file this unit writes
outside its new ones also moved on that line: `lib-unattended.sh`, `resolve-python.test.sh`,
`gate-legs.json`, `selftest-budgets.txt`, the policy catalogue and its help page, and the kickoff
manifest. The base now holds those moves. Each write here is additive, one block, two parity rows,
one leg, one budget row and one key, beside the manifest's `last-audit` re-stamp. They are named here so the merge onto dWitnessedBar's
landing can reconcile them.

Recall terms used: history leg verdict cache incremental pass-order brief-recorded routed_commits gate-cache reuse key HEAD cat-file batch
