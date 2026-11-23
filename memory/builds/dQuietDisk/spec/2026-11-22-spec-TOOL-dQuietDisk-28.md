# TOOL-dQuietDisk-28 — the history store's bash face resolves the switch and the git dirs once per calling shell

**Status:** CLOSED · rev-1 · 2026-11-22 · node d · Tier-2 · base 40def53f · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-28-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-28-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-28-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-28-deviation-1.md) | deviation | — |
| [2026-11-22-build-TOOL-dQuietDisk-28-red-fix-7.md](../build/2026-11-22-build-TOOL-dQuietDisk-28-red-fix-7.md) | red-fix | — |
| [2026-11-22-build-TOOL-dQuietDisk-28-widen-8.md](../build/2026-11-22-build-TOOL-dQuietDisk-28-widen-8.md) | widen | — |
| [2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md](../build/2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-prompt-TOOL-dQuietDisk-28-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-28-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-28-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-28-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-28-spec-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-28-spec-task.md) | research | — |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |

<!-- /gen:spec-records -->

## 1. Goal

Each verb of the history store's CLI resolves the store afresh: 7 git processes for the policy read
of `tests.history-verdicts` and 1 `rev-parse` for the git dirs, before it reads or writes an item.
A shell that makes ten verbs pays 80 [PINNED, measured 2026-11-22 under `GIT_TRACE2_EVENT` in a
scratch repository with no remote, with this branch's `tools/` tree, which equals the base's]. This
unit has `init_hs` resolve once and hand that one resolution to every verb its shell makes, through
an environment value keyed by the directory it was resolved for. Every value of the switch, its
default and its fallback stay what they are.

## 2. Scope (IN)

- **S1** — `read_resolved(repo)` in the `history_store_py` block holds today's two reads as one
  answer: the switch's mode, the note the policy read printed where the key did not read, and, under
  `stored`, the absolute git dir and the absolute common dir. It runs `read_policy_mode` and then
  the `rev-parse` exactly as `resolve_store` runs them today, in the same order, and runs no
  `rev-parse` under `regraded`. Observed by AC1, AC3 and AC6.
- **S2** — `resolve_store(repo, leg, code_paths, resolved=None)` takes an optional resolution. Given
  none, it calls `read_resolved`, so every existing caller, unit 4's included, reads as today. Given
  one, it starts no git process. Either way it prints the held policy note, and the `git names no
  git dir` line with its own leg, on each call, so each call's stderr is today's. Observed by AC3,
  AC6 and AC7.
- **S3** — The export. `render_resolved` writes one line, the tag `history-store-resolved v1`, the
  key, the mode, the git dir, the common dir and the escaped note, separated by tabs. The key is
  `os.path.normcase` of the absolute directory the resolution was read for. `parse_resolved(text,
  repo)` answers the resolution only where the tag matches, there are six fields, the key equals
  `repo`'s own key, the mode is one of `MODES`, and under `stored` both dirs are absolute and are
  directories. Any other text answers None. A path holding a tab or a newline is never rendered.
  Observed by AC4 and AC5.
- **S4** — The CLI. A new verb, `resolve`, prints `render_resolved(read_resolved(cwd))` and nothing on
  stderr, and never reads the environment. Every other verb reads `HS_RESOLVED` from its environment
  through `parse_resolved` against its working directory, and passes what it answers to
  `resolve_store`. An absent, malformed or foreign value is None, so that verb resolves afresh, as
  today. Observed by AC1, AC4 and AC5.
- **S5** — The bash face. `init_hs`, after it resolves python, runs the `resolve` verb once and
  exports its line as `HS_RESOLVED`. Where that call fails or prints nothing, it unsets
  `HS_RESOLVED`. `init_hs` never gains a failure: it returns 0 or 2 exactly where it does today. The
  block changes in `tools/lib/history-store.sh` and byte-identically in
  `tools/unattended/lib-unattended.sh`. Observed by AC1, AC2 and AC8.
- **S6** — The three copies. `tools/lib/history_store.py`, `tools/unattended/history_store.py` and
  `tools/memory-tree/history_store.py` stay byte-identical, and the module docstring gains one
  paragraph naming the export, its key and the `resolve` verb. The existing `history_store_py` and
  `history_store_sh` rows of `PARITY_ROWS` grade them, unchanged. Observed by AC8.
- **S7** — The selftest gains arms for S3 and S4: a held line keyed to another directory, or
  malformed, is not read, and a `resolve` line read back in its own directory resolves the same store
  with no git process. Every existing arm stays as it is. Observed by AC3 and AC5.
- **S8** — The shell-line ledger. `tools/lib/history-store.sh` and `tools/unattended/lib-unattended.sh`
  each sit at their row, 59 and 1390 [PINNED, measured 2026-11-22 by
  `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ":!memory/"`], so every code line
  S5 adds is widened through `python tools/memory-tree/ratchet.py widen shell-role --key
  tools/lib/history-store.sh --key tools/unattended/lib-unattended.sh --reason <one line> --unit
  TOOL-dQuietDisk-28`, as unit 1 widened them. No row is edited by hand. Observed by AC9.
- **S9** — The adopters. The unattended and memory-tree kits ship the changed files, so they reach
  nc, ic and swydee only through a minted kit version and `govkit update`. Observed by AC10.

## 3. Non-goals (OUT)

- No memo inside `resolve_store` across calls. The selftest's switch arm calls it three times in
  one process across two policy commits and expects each to read afresh
  (`tools/lib/history_store.py@56514f3e36f1:638`), and a python leg already calls it once per run.
- No change to what the policy read costs. Its 7 processes are the policy kit's landed-revision read
  (`tools/policy/policy.py#derive_landed_revision`), which this unit calls as it is.
- No change to the switch: its key, its two values, its default, its catalogue row and its help row.
- No file holds the resolution. It lives in the calling shell's environment and dies with it.
- No change to units 2, 3 and 4. Their warm-run bounds are upper limits, so none moves.
- No change to `BatchReader` or the coprocess. Each answers a question per object, which no
  resolution can hold.
- No kit version bump by hand. `govkit.py mint` writes every owed bump at the lander.

### Edges

- **consumes-from** external — the store, its CLI and its bash face, as TOOL-dQuietDisk-1 built them
  and landed them at the base. That spec is CLOSED and frozen, so it carries no edge back, and this
  unit changes its code in place

## 4. Design

### Where the code was read

Every citation is at `40def53f`, the merge of main at `8b8b1374c`, dWitnessedBar's landing, into
this run. This branch's `tools/` tree equals the base's: `git diff --stat 40def53f HEAD -- tools/`
prints nothing. A citation is written `<path>@<blob>:<line>` or by symbol.

### What a verb pays today

`main` builds the store with `resolve_store(os.getcwd(), leg, code)` for every verb
(`tools/lib/history_store.py@56514f3e36f1:716`). `resolve_store` reads the switch first
(`tools/lib/history_store.py@56514f3e36f1:460`) and then runs one
`rev-parse --absolute-git-dir --git-common-dir` (`tools/lib/history_store.py@56514f3e36f1:463`).
`read_policy_mode` spawns `policy.py get tests.history-verdicts` in the repository
(`tools/lib/history_store.py@56514f3e36f1:238`), and that read resolves the landed revision.

| Verbs from one shell | Git processes today |
|---|---|
| one `tip` | 8: 3 `rev-parse`, 2 `show`, 1 `config`, 1 `remote`, 1 `symbolic-ref` |
| ten `tip` | 80 |

Both rows are PINNED, measured 2026-11-22 under `GIT_TRACE2_EVENT=<dir>` by counting the files, in
a scratch repository on `main` with one commit and no remote, running this branch's
`tools/lib/history_store.py`. Units 2 and 4 measured 8 in a fixture and 9 in gov's tree, where the
remote ladder adds one read [PINNED in each unit's section 4, 2026-11-22].

`init_hs` resolves python and starts no git process
(`tools/lib/history-store.sh@9719fc175beb:27`). Each of `read_hs_tip`, `read_hs_items` and
`write_hs_items` is one CLI child, so each pays the 8.

### The resolution

```text
read_resolved(repo) -> (mode, note, git dir, common dir)
  mode, note = the policy read, as read_policy_mode reads it today, the note returned not printed
  under regraded: git dir = common dir = ""              (no rev-parse, as today)
  under stored:   the rev-parse; a failure leaves both "" (resolve_store then prints today's line)

HS_RESOLVED = "history-store-resolved v1" TAB key TAB mode TAB git dir TAB common dir TAB render_escaped(note)
key         = os.path.normcase(str(pathlib.Path(dir).absolute()))
```

`read_policy_mode` returns its note instead of printing it. `resolve_store` is its only caller
(`git grep -n read_policy_mode 40def53f -- tools/` names only the three copies), so the note's text
and the point at which it prints are unchanged: `resolve_store` prints it first, then any
`git names no git dir` line, then the code digest's own line, as today. The common dir is made
absolute as `resolve_store` makes it today, before it is held.

`parse_resolved` deny-defaults. A value it cannot read in full answers None, and None means "resolve
afresh". So the worst a wrong value can cost is a saving, never a verdict. A value that names
another directory is the case the key exists for: a child started in another worktree or another
repository resolves its own switch and its own git dirs.

### The key, and what it does not check

The key is the directory the CLI runs in, which `main` already passes to `resolve_store`. A child in
the same directory resolves the same answer git would give it, because both the parent's and the
child's `rev-parse` run under `derive_git_env`, which drops `GIT_DIR` and its siblings. A child in
a subdirectory of the same worktree misses and resolves afresh. That costs 8 and no verdict, and
units 2 and 3 run every verb from the repository root.

What it does not check: a repository deleted and re-created at the same path while one shell holds
the export. The child then reads the old mode and the same paths. The store's items are keyed by the
ids each reads (unit 1 S3), so a read under a stale `stored` returns only what a regrade would
grade, and the policy is disobeyed for that shell's life. Nothing in gov does that inside a leg.

### The bash face

```bash
init_hs() {
  ...                                   # today's lines, unchanged
  HS_PY=$(resolve_python) || return 2
  if HS_RESOLVED=$("$HS_PY" "$HS_MODULE" "${HS_ARGS[@]}" resolve 2>/dev/null) && [ -n "$HS_RESOLVED" ]
  then export HS_RESOLVED; else unset HS_RESOLVED; fi
}
```

The `resolve` call's stderr is discarded because the verb prints nothing there by contract. A
crash there leaves `HS_RESOLVED` unset, so each verb prints its own lines, as today. `init_hs`
always resolves afresh and overwrites an inherited value, so a leg's run reads the switch at its own
start, never at an ancestor's.

### The consumers

| Unit | Store calls per run | Git processes for the store, before → after | Its bound |
|---|---|---|---|
| TOOL-dQuietDisk-2 | `init_hs`, `read_hs_tip`, two `read_hs_items` warm; one `write_hs_items` more on a moved tip | warm 24 → 8; moved tip 32 → 8 | 45 and 50 plus B, unchanged |
| TOOL-dQuietDisk-3 | `init_hs`, one `read_hs_items` warm; one `write_hs_items` more on a write | warm 8 → 8; a write 16 → 8 | 25, unchanged |
| TOOL-dQuietDisk-4 | one `resolve_store` per run, in process | 8, or 9 in gov's tree, unchanged | its table, unchanged |

The rows are DERIVED from each spec's run section and the 8 per verb above. Unit 3's warm run moves
its one resolve from the lookup into `init_hs`, so it saves nothing warm and saves 8 on a run that
writes. TOOL-dQuietDisk-4 calls `resolve_store` once per process from python and never runs the
bash face, so it gains nothing; its own spec's F1 cost stands. The saving falls to the shell legs.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `read_resolved`, `render_resolved`, `parse_resolved` | Python functions | `py.function`, lexicon `--suggest` OK | the module's `--selftest` |
| `resolved` | keyword parameter of `resolve_store` | none: the lexicon declares no parameter cell | the module's `--selftest` |
| `HS_RESOLVED` | exported shell variable | none: the lexicon declares no shell-variable cell | the module's `--selftest` |
| `resolve` | CLI verb | none: the lexicon declares no cell for a CLI verb | the module's `--selftest` |
| `history-store-resolved v1` | the export's tag | none | `parse_resolved` |

Each function leads with a declared verb, checked by
`python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Files touched (estimate)

`tools/lib/history_store.py` · `tools/unattended/history_store.py` ·
`tools/memory-tree/history_store.py` · `tools/lib/history-store.sh` ·
`tools/unattended/lib-unattended.sh` · `memory/project/shell-role.txt` ·
`memory/map/generated/symbols.json` ·
`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-28-widen-<n>.md`

The widen record's name is the door's. Its number is one past the highest widen record in the build
folder (`tools/memory-tree/build_records.py#write_record`), which holds three [PINNED, counted
2026-11-22], so
`4` unless another unit widens first. The three new functions in each copy join the codebase map's
symbol index, re-rendered by the codebase map's generator, `gen_map.py --write`, never by hand, as unit
1's build commit re-rendered it. No path here is on the kickoff manifest's `watch:` line.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| A memo dict inside `resolve_store` | The switch arm reads afresh three times in one process, and a CLI child is a new process, so a memo saves the shell legs nothing. |
| The resolution in a file under the git dir | The task forbids it, and a file outlives the shell, so a later run would read a stale switch. |
| Keying the export by the git dir found by walking up to `.git` | It re-implements git's discovery without its ceilings and `safe.directory`. The working directory is what `main` already resolves against. |
| A lazy resolve in the first verb | A child cannot export into its parent shell, so the second verb would pay again. |
| `read_resolved` reading the environment too | `resolve` must always read afresh, and so must a python caller such as unit 4. Only the CLI's other verbs read the export. |

## 5. Production-readiness checklist

- security: `HS_RESOLVED` is read only by the store's own CLI, only for the directory it names, and
  only where both dirs it names are existing directories. Anyone who can set it can already set
  `GIT_DIR` for the leg. A wrong value costs a saving, never a verdict, because a miss regrades.
- perf / scale: a shell making N verbs pays 8 git processes and one more python process, in
  `init_hs`, in place of 8 times N.
- error / empty / loading states: a failed `resolve`, an empty line, a malformed or foreign value all
  fall back to today's per-verb resolve. The switch's own fallbacks are unchanged.
- observability: each verb prints the same stderr lines as today, the policy note included.
- risks: a repository re-created at the same path inside one exporting shell (section 4). The gotcha
  classes `suite-invalidated-by-a-commit-under-it` and `test-oracle-read-from-a-historical-sha` were
  read: the selftest's switch arm is why no memo crosses calls, and every probe below reads the
  policy from the commit it plants.
- testing: the module's `--selftest`, and the probes of section 6.
- migration: N/A — no stored data changes; a shell without the export behaves as today.
- user docs: N/A — the switch's help row does not change, and `HS_RESOLVED` is no knob.

## 6. Acceptance criteria

- **AC1** — When a probe builds a repository under `%TEMP%/<short-name>` on `main` with one commit
  and no remote, sources `tools/lib/history-store.sh` with `resolve_python` defined, sets
  `GIT_TRACE2_EVENT` to an empty directory, and runs `init_hs probe a` and one `read_hs_tip`, the
  directory holds 8 files [PINNED] before the change and at most 8 [PINNED] after. With ten
  `read_hs_tip` calls after one `init_hs`, it holds 80 [PINNED] before and at most 8 [PINNED] after.
  So the after count for ten verbs is at most the before count for one verb, plus one process per
  item read through git, which these verbs do not do.
  Red when: a verb still resolves, so ten verbs hold more than 8 files [PINNED, AC1's bound].
  figure: 8 and 80 PINNED as measured on 2026-11-22; the after counts DERIVED at observation.
- **AC2** — When the probe of AC1 runs `init_hs` and then `env | grep -c '^HS_RESOLVED='` in a child,
  it prints 1, and the value's fourth field is the repository's absolute git dir. When `init_hs` runs
  with `HS_MODULE`'s `resolve` call made to fail, `HS_RESOLVED` is unset and `init_hs` returns 0.
  Red when: the value is not exported, or a failed resolve makes `init_hs` fail.
- **AC3** — When the main loop runs `python tools/lib/history_store.py --selftest` at the close, every
  arm line the base's module prints is printed again with `ok`, the new arms print `ok`, and it exits 0.
  Red when: an existing arm changes or fails, which a memo inside `resolve_store` causes in the switch
  arm.
  permission: a role agent runs no `--selftest` (scratch-guard row G3). This is the `New arm:` line's
  RED and GREEN observation, owed to the main loop. The pass's proxy is AC1, AC2 and AC4 to AC7.
- **AC4** — When the probe makes a second repository whose `main` commits
  `.governance/policy.toml` holding `tests.history-verdicts = "regraded"`, runs `init_hs` in the
  first, then `cd`s into the second and runs `write_hs_items` with one item and a tip, the second
  repository's `history-verdicts/` directory and the first's item tree are both unchanged, and
  `read_hs_tip` there prints nothing. From a `git worktree add` of the first repository, which shares
  its landed revision and so its mode, a tip written there reads back there and not in the first
  worktree, and the first worktree's tip is unchanged.
  Red when: `parse_resolved` skips the key comparison, so the child in the second repository reads the
  first's `stored` and writes into the first's store, and the child in the worktree writes its tip
  under the first worktree's scope. The pass observes this red first, with the comparison removed,
  and then green.
- **AC5** — When a verb runs with `HS_RESOLVED` set to a value with a foreign tag, five fields, a mode
  of `kept`, or a git dir that is not a directory, its stdout and stderr are byte-identical to the
  same verb run with `HS_RESOLVED` unset, and its trace directory holds 8 files [PINNED, measured
  2026-11-22 as AC1's one-verb count].
  Red when: a malformed value is read, or turns the store on or off.
- **AC6** — When the probe's repository commits `tests.history-verdicts = "regraded"` on `main`, the
  verbs after `init_hs` print `miss` for an item written while it read `stored`, and write no item and
  no tip. When the same value is committed only on a branch `feature` that is checked out, and `main`
  does not hold it, the store stays on. Both answers equal the base module's answers to the same
  probe.
  Red when: the switch is read from another source than the landed revision, or its off value still
  reads or writes.
  fixture: the policy kit beside the module, as `tools/policy/` sits beside `tools/lib/` in gov.
- **AC7** — When the probe commits `tests.history-verdicts = "bogus"` on `main`, so the key does not
  read, each of `read_hs_tip`, `read_hs_items` and `write_hs_items` after one `init_hs` prints on
  stderr exactly what the base module prints for that verb, the `did not read, so stored holds` note
  included, and the store stays on. `init_hs` itself prints nothing.
  Red when: the note is lost from a verb, printed twice, or printed by `init_hs`.
- **AC8** — When `cmp tools/lib/history_store.py tools/unattended/history_store.py` and
  `cmp tools/lib/history_store.py tools/memory-tree/history_store.py` run, both exit 0. When the
  `history_store_sh` block is extracted with the parity table's own `blk` awk from
  `tools/lib/history-store.sh` and `tools/unattended/lib-unattended.sh`, the two compare equal.
  Red when: a copy drifts by one byte, which the existing `history_store_py` and `history_store_sh`
  rows of `PARITY_ROWS` then report.
- **AC9** — When
  `grep -n -E "^tools/(lib/history-store\.sh|unattended/lib-unattended\.sh)\s" memory/project/shell-role.txt`
  runs after the widen, it prints two rows, each ending `widened:<stem>` for one record stem. That
  stem names a file under `memory/builds/dQuietDisk/build/` whose Keys field lists exactly those two
  paths and whose Caused-by is `TOOL-dQuietDisk-28`. `git diff --stat -- memory/project/shell-role.txt`
  shows those two rows and no other.
  Red when: a row is edited by hand, or a row for a file this unit does not touch moves.
- **AC10** — When `python tools/govkit/govkit.py shipped` runs, it lists `history_store.py` under both
  `unattended` and `memory-tree`. When `python tools/govkit/govkit.py check --target C:/projects/incms/main`,
  and the same with `C:/projects/nicocares/main`, run read-only from gov before and after the unit,
  each prints the same bytes and exit code.
  Red when: a copy is not claimed by its kit, or a check reads differently.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
  fixture: the adopters reach the change only after a minted version and their own `govkit update`.

This unit moves no verdict. A store that is on or off, warm or cold, gives each consumer the same
rc and output, and the switch resolves to the same value from the same source.

## 7. Gates

`kit epoch (shipped bytes move, the version moves)` · `history-store selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `portability (shell lines only shrink)` · `ratchet (never gains)` · `recall floor` · `recall floor arms` · `routed-commits selftest` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `line length`

New arm: tools/lib/history_store.py · covers AC3 AC4 AC5 · the module's --selftest; its failing case is staged by dropping the key comparison in parse_resolved, or by reading HS_RESOLVED in the resolve verb · none

The bar runs once at the close. The new arms' RED and GREEN observation is the main loop's. No
criterion has the pass run a suite, a `--selftest`, a gate leg or the bar.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-22 · initial draft, under `2026-11-22-prompt-TOOL-dQuietDisk-28-spec-task`. Order
  3: its write set meets units 2 and 3 only through the shell face they call, and is disjoint from
  the other order-3 units' Files touched, units 6, 10, 12, 13 and 18.

## 10. Reuse audit

The seam extended is the store itself: `tools/lib/history_store.py#resolve_store`, its CLI `main`
and the bash face's `init_hs`, with their copies held by the existing `PARITY_ROWS` rows. No existing
seam holds a resolved policy value across processes: `tools/playbook/policy_value.py#read_policy_value`
spawns `policy.py get` per call, and `git grep -n "environ\[" 40def53f -- tools/lib tools/policy`
shows no exported resolution, only `tools/policy/check_policy.py` setting `GOV_REMOTE` for a run.
`python tools/codebase-map/reuse_lookup.py "hold a resolved policy value once per process and hand it to child processes through the environment"`
ranked `resolve`, `resolve_kit_dir`, `read_policy_value` and `resolve_remote`, each a per-call
resolver, none a held one. So no existing seam fits a held resolution, and the store's own resolver
is split rather than a second one added.

Owning chain build: dWitnessedBar (Test: gate health), whose legs units 2 and 3 serve. No
dWitnessedBar spec defines the history store or a held policy read.

Recall terms used: history store policy switch resolve once per process export environment init_hs rev-parse git dir tests.history-verdicts
