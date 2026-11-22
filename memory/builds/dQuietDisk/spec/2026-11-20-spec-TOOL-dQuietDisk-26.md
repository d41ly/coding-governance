# TOOL-dQuietDisk-26 — `check-wiring.sh` lists the tree once per invocation

**Status:** CLOSED · rev-3 · 2026-11-22 · node d · Tier-2 · base c3c0811b · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-28 |
| [2026-11-22-build-TOOL-dQuietDisk-26-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-26-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-26-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-26-deviation-1.md) | deviation | — |
| [2026-11-22-build-TOOL-dQuietDisk-26-widen-12.md](../build/2026-11-22-build-TOOL-dQuietDisk-26-widen-12.md) | widen | — |
| [2026-11-22-build-TOOL-dQuietDisk-26-widen-13.md](../build/2026-11-22-build-TOOL-dQuietDisk-26-widen-13.md) | widen | — |
| [2026-11-22-build-TOOL-dQuietDisk-26-widen-17.md](../build/2026-11-22-build-TOOL-dQuietDisk-26-widen-17.md) | widen | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md) | research | TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task.md) | research | TOOL-dQuietDisk-11 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 |
| [2026-11-22-prompt-TOOL-dQuietDisk-26-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-26-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-26-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-26-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-wiring.sh` asks git about the tracked tree once per question: fourteen `ls-files`, four
`ls-tree` and three `check-attr` processes in one `--check` over gov's own tree, of 44 git processes
in all. This unit lists the index once with `git ls-files -s`, reads every attribute once with one
batched `git check-attr --stdin`, reads the four hooks' `HEAD` entries with one `git ls-tree`, and
answers every check from those three reads in-process. Every finding and the exit code stay
byte-identical, and the saving is counted on one run over the real tree and on the whole suite.

### The saving, re-grounded at c3c0811b8

This unit changes the checker, not a suite's fixtures, so the template cache is not in play: no
suite moves onto it, and nothing here reads `tests.fixture-templates`.

- **Today, one `--check` over gov's tree:** 44 git processes, of them 14 `ls-files`, 4 `ls-tree` and
  3 `check-attr`, rc 1, about 6.0 s, and 0 residual temp entries.
  figure: PINNED, measured 2026-11-22 at `c3c0811b8` in a scratch `git clone --shared` (section 4).
- **After:** at most one of each of the three, so at most 26 git processes, a saving of at least 18
  per invocation. No temp entry is added.
  figure: DERIVED from section 4's table.
- **The suite:** its `ls-files`, `ls-tree` and `check-attr` processes fall to at most half of today's.
  Today they are 1,679, 186 and 421, which is 2,286 of its 3,786.
  figure: PINNED by the analysis's measured run at gov `608aa364c`, its representative-runs section.
  TOOL-dQuietDisk-10 changed only the suite's `config` processes, so those three stand.

## 2. Scope (IN)

- **S1** — `read_tree_listing` runs ONE `git ls-files -s` per invocation, in the parent shell,
  right after the settings view's one no-argument `matchers_of` call
  (`tools/check-wiring.sh@49c697eccc63:964`) and before the first arm. It keeps the output in `_LS`
  and its path column, every line kept in order, unmerged stages included, in `_LS_NAMES`. The
  listing is usable only when the call exits 0 and no path in it begins with `"`. Observed by AC1,
  AC2 and AC4.
- **S2** — `check_listed <path> [exact]` answers "is this tracked" from `_LS_NAMES`. Plain, it is
  git's rule for a literal pathspec: an entry equal to the path or under `<path>/`, and only under it
  when the path ends in `/`. With `exact`, only an entry equal to the path. It serves the four
  hook-tracked tests of `check_hook_blobs`, the entry test of `check_hooks`, the kit test of
  `check_skill_install` and both `ROUTED_PATHS` tests of `check_routed`, the directory form plain and
  the file form `exact`. With the listing unusable it makes today's
  `git --literal-pathspecs ls-files -- <path>` call and applies the same rule to its output.
  Observed by AC2, AC3 and AC5.
- **S3** — `read_listed_attrs` runs ONE `git check-attr --stdin eol merge` over `_LS_NAMES`, right
  after S1, and keeps its lines in `_LS_ATTRS`. It makes no call when the listing is unusable.
  `read_listed_attr <attr>` prints that attribute's lines in listing order. `check_eol`,
  `check_merge_rows` and `check_merge_ours` read their attribute through it, `check_eol` applying its
  sed capture and then its existing ERE filter. When the listing or the batched read is unusable,
  `read_listed_attr` runs today's `git ls-files | git check-attr --stdin <attr>`. Observed by AC1,
  AC2, AC3 and AC5.
- **S4** — `check_hook_modes` takes its entries from `_LS` when the directory's checkout is this
  one (`[ "$top" -ef "$ROOT" ]`), neither `GIT_DIR` nor `GIT_WORK_TREE` is set, and the listing is
  usable: the lines whose path begins with the directory's prefix, each path read relative to that
  prefix, as `git -C "$dir"` prints it. Otherwise it runs today's `git -C "$dir" ls-files -s`. The
  `--fix` read-back after `git update-index` stays a live call. Observed by AC2, AC3 and AC5.
- **S5** — `check_hook_blobs` runs ONE `git ls-tree HEAD --` over the four `GOV_WIRING_HOOKS` paths,
  at its first tracked hook, and reads each hook's blob id from the line naming that hook. A tree
  that tracks no hook spawns none. Observed by AC1, AC2 and AC5.
- **S6** — Every line the checker prints, on stdout and stderr, and its exit code, are byte-identical
  to the checker at the build base, over the real tree and over the fixture corpus of AC3.
  Observed by AC2, AC3 and AC6.
- **S7** — The saving is counted: git processes of one `--check` over the real tree, and of the
  whole check-wiring suite, before and after. Observed by AC1 and AC6.
- **S8** — The seven new state variables are reset at file scope, so a value inherited from the
  environment never stands in for a read this run did not make. Observed by AC4.
- **S9** — No new temp entry. Every read of `_LS`, `_LS_NAMES` or `_LS_ATTRS` feeds a pipe from
  `printf '%s\n'`, never a here-string or a heredoc, because bash writes a large one to a temp file
  (section 4, "Pipes, never here-strings"). Observed by AC1 and AC5.

## 3. Non-goals (OUT)

- The other per-question reads the analysis counts: `config` (400 of the suite's 3,786), `rev-parse`
  (511), `hash-object` (178) and `remote` (94), PINNED in
  `memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`, its
  representative-runs section. Each asks a different question, and `--fix` writes config between two
  of the reads, so they are not a listing.
- The suite's own fixtures and their git processes: TOOL-dQuietDisk-10, CLOSED. This unit adds arms
  to the suite and no fixture machinery.
- The template cache. No suite moves onto it, so `read_template_mode` and `template_cache_sh` are
  not called, and the suite carries no inline block it does not carry today.
- No cache and no switch. The three reads answer, inside one process, exactly what each per-site
  call answered, so they are reads and not stored answers, the reasoning TOOL-dQuietDisk-5 records
  in its non-goals for its one guard diff. Nothing persists between invocations.
- No change to the settings view, `matchers_of`, the fragment reader or any inline canonical block.
  `tools/settings-merge.py`'s selftest lifts `matchers_of` alone, and it is untouched.
- No change to which arms run, their order, or any message.
- No kit version bump by hand. `govkit.py mint` writes every owed bump at the lander.
- The owned, swept scratch root: TOOL-dQuietDisk-9.

### Edges

- **consumes-from** `TOOL-dQuietDisk-10` — the check-wiring suite as unit 10 built it: its one seed per run, and `newrepo wired`, which writes the wired config unit 10 captures once per run into `NEWREPO_WIRED_CONFIG`. This unit's two new arms build their fixtures with `newrepo wired`. Without it the arms would spend a `git config` per fixture and miss unit 10's form.
- **hands-off** `TOOL-dQuietDisk-19` — the suite's after readings, which then hold this unit's listing.
- **consumes-from** external — dWitnessedBar's landed tip, merged at `685a7a522`, which this unit is built on. Its unit 27 added the inline `refuse_wrong_shell` block to `tools/check-wiring.sh`.

## 4. Design

### The reads today

All citations are read at `c3c0811b8`, where `tools/check-wiring.sh` is blob `49c697eccc63`. Since
rev-2's base `59e882afd` the file moved by its version line alone, so no cited line moved. The
predicate below names the enclosing function of every `git … ls-files`, `ls-tree` and `check-attr`
spawn outside comments and `echo` strings. Run over the file at that blob, it found fourteen spawn
sites in eight functions.

```awk
/^[A-Za-z_][A-Za-z0-9_]*\(\) *\{/ { fn=$1; sub(/\(\).*/,"",fn) }
/^[[:space:]]*#/ { next }
{ line=$0; gsub(/echo "[^"]*"/,"",line)
  while (match(line, /git( -C "[^"]*"| --literal-pathspecs)* (ls-files|ls-tree|check-attr)/)) {
    s=substr(line,RSTART,RLENGTH); sub(/.* /,"",s); printf "%s:%d %s\n", fn, NR, s
    line=substr(line,RSTART+RLENGTH) } }
```

| Function | Read | Line | Per `--check` on gov's tree |
|---|---|---|---|
| `check_hook_blobs` | `ls-files --error-unmatch .githooks/$hook` | `tools/check-wiring.sh@49c697eccc63:803` | 4 |
| `check_hook_blobs` | `ls-tree HEAD -- .githooks/$hook` | `tools/check-wiring.sh@49c697eccc63:809` | 4 |
| `check_hook_modes` | `git -C "$dir" ls-files -s` | `tools/check-wiring.sh@49c697eccc63:859` | 1 |
| `check_hook_modes` | the `--fix` read-back | `tools/check-wiring.sh@49c697eccc63:877` | 0 |
| `check_hooks` | `ls-files --error-unmatch .githooks/pre-commit` | `tools/check-wiring.sh@49c697eccc63:902` | 1 |
| `check_eol` | `ls-files <4 pathspecs> \| grep -E \| check-attr --stdin eol` | `tools/check-wiring.sh@49c697eccc63:1322`, `:1324` | 1 + 1 |
| `check_merge_rows` | `ls-files \| check-attr --stdin merge` | `tools/check-wiring.sh@49c697eccc63:1434` | 1 + 1 |
| `check_merge_ours` | `ls-files \| check-attr --stdin merge` | `tools/check-wiring.sh@49c697eccc63:1629` | 1 + 1 |
| `check_routed` | `--literal-pathspecs ls-files -- "$c"`, directory form, then file form | `tools/check-wiring.sh@49c697eccc63:1846`, `:1848` | 4 |
| `check_skill_install` | `ls-files --error-unmatch -- "$rel/SKILL.md"` | `tools/check-wiring.sh@49c697eccc63:1972` | 1 |

Measured on 2026-11-22, PINNED: `bash tools/check-wiring.sh --check` in a scratch
`git clone --shared` at `c3c0811b8` with `core.hooksPath=.githooks`, under `GIT_TRACE2_EVENT` and
with `TEMP`, `TMP` and `TMPDIR` at one scratch dir, spent 44 git processes, of them 14 `ls-files`,
4 `ls-tree` and 3 `check-attr`, rc 1, 5.97 s, and left 0 entries in the scratch dir. Rev-2's reading
at `59e882afd` was the same 44, 14, 4 and 3. The four `check_routed` calls are this repository's four
`ROUTED_PATHS` entries (`.memory-tree.conf`), two directories and two files.

Every invocation that reaches the `matchers_of` line runs every arm in order: no top-level `exit`
sits between it and the dispatch, and no arm exits. `--resolve-fragment` exits before it
(`tools/check-wiring.sh@49c697eccc63:771`), as does a directory that is not a repository.
`check_eol` and `check_merge_ours` reach their listing calls unconditionally, while
`check_merge_rows`, `check_routed` and `check_skill_install` can return first.

### The three reads after

```bash
_LS=""; _LS_NAMES=""; _LS_OK=""; _LS_ATTRS=""; _LS_ATTRS_OK=""; _LT=""; _LT_READ=""   # file scope (S8)
read_tree_listing   # S1, right after `matchers_of || :`, in the parent shell
read_listed_attrs   # S3, right after it
```

- `_LS_NAMES` is framed by a newline at each end, so `check_listed` is a quoted `case` match:
  `*"$nl$p$nl"*` for an equal entry and `*"$nl$p/"*` for one under it. Bash quoting makes every
  character of `$p` literal, which is the `--literal-pathspecs` rule.
- The path column comes from `printf '%s\n' "$_LS" | cut -f2-`, a process but not a git one. Probed
  again on 2026-11-22 under git 2.54.0.windows.1, PINNED: on an index holding stages 1 to 3 of one
  path after a conflicted merge, `git ls-files -s | cut -f2-` and plain `git ls-files` print the same
  lines, so the merge arms keep seeing duplicates exactly as today.
- `read_listed_attr <attr>` keeps the lines matching `: <attr>: [^ ]*$`. An attribute value holds no
  whitespace in `.gitattributes`, so an `eol` line can never match the `merge` filter, nor the
  reverse. The same probe showed the batched call prints each path's `eol` line then its `merge`
  line, and that its `eol` lines and its `merge` lines are each identical (`diff`) to what the two
  separate calls print.
- `check_eol` today filters the path list by its ERE and then asks `check-attr` about the survivors.
  After, it asks about every path and applies the same ERE to the captured paths. Each ERE
  alternative sits inside one of the four pathspecs, so the population and its order are the same.
- The same probe showed one `git ls-tree HEAD --` over the four hook paths prints one line for each
  tracked one and none for the rest, and `git -C <dir> ls-files -s` from a subdirectory prints only
  that directory's entries, relative to it, in index order.

### Pipes, never here-strings

Probed on 2026-11-22 under GNU bash 5.3.9 (x86_64-pc-cygwin), PINNED: ten `wc -c <<< "$big"` over a
3,000,000-byte string, with a watcher listing `TMPDIR` in a loop, caught two distinct `sh-thd.*`
files there. Bash writes a large here-string to a temp file, which is the file create this build
counts. The same read fed by `printf '%s\n' "$big" |` is a pipe. S9 therefore feeds every read of
the three strings through a pipe. `check_hook_modes` keeps its existing heredoc over its own
`ls`, which after S4 holds only the hooks directory's few lines, as it does today.

### Why the listing may be read after the run's one index write

The only index write in the file is `--fix`'s `git update-index --cacheinfo` in `check_hook_modes`
(`tools/check-wiring.sh@49c697eccc63:876`;
`grep -nE 'git (add|rm|update-index|checkout|commit|mv|reset|restore)'` finds no other outside an
`echo` string). It changes a hook's mode, never a path. `check_hook_modes` runs once per
invocation, from one of the two branches of `check_hooks` (`tools/check-wiring.sh@49c697eccc63:913`,
`:936`). Its read-back stays live, and no later reader reads a mode. `.gitattributes` is written by
no arm, so the attribute read made before the first arm is the one each arm would have made.

### Why a quoted path disables the listing

With `core.quotePath` at its default, `ls-files` prints a path holding non-ASCII or control bytes
in C quotes. A per-site pathspec matches the raw name and prints the quoted line, so
`check_routed`'s directory test passes for a directory whose only tracked file is `docs/é.md`.
Probed again on 2026-11-22, PINNED: with `docs/é.md` tracked, `git ls-files -s | cut -f2-` printed
`"docs/\303\251.md"` and `git --literal-pathspecs ls-files -- docs/` printed the same quoted line. A
string prefix test over the quoted line would not match `docs/`. Rather than unquote in bash, a
listing holding any quoted line is unusable and every site makes today's call. Gov's tree holds no
quoted path: `git ls-tree -r --name-only c3c0811b8 | grep -c '^"'` printed 0 on 2026-11-22, DERIVED.
An adopter tree that holds one keeps today's cost plus one `ls-files -s`, and today's answers.

### Case

Pathspec matching ignores `core.ignorecase`. Probed again on 2026-11-22 with git 2.54.0.windows.1,
PINNED: with `core.ignorecase=true` and `Foo/a` tracked, `git ls-files --error-unmatch foo/a` exited
1 and `git --literal-pathspecs ls-files -- foo/` printed nothing. So the case-sensitive `case` match
is git's own rule, and AC3 holds a fixture on it. AC3's routed fixtures start from the armed routed
fixture the suite builds today: its `.memory-tree.conf` write at
`tools/check-wiring.test.sh@0ccb1cbf38ee:605`, inside the block guarded at
`tools/check-wiring.test.sh@0ccb1cbf38ee:540`. The checker's routed arm needs `node` on `PATH`
(`tools/check-wiring.sh@49c697eccc63:1798`).

### The bound

One `--check` over gov's tree spends at most one `ls-files`, one `ls-tree` and one `check-attr`
against 14, 4 and 3, so its git processes fall from 44 by at least 18. Each `--fix` read-back adds
one `ls-files`, and so does a hooks directory another checkout supplies; today spends both of those
too. Both bounds are DERIVED from the table above.

Per invocation in the suite:
- a tree with no tracked hook spends at least two `ls-files` and two `check-attr` today, from
  `check_eol` and `check_merge_ours`, against one of each after: exactly half;
- a `newrepo wired` copy, which tracks `.githooks/pre-commit` alone, spends at least eleven today:
  `check_hooks` one, `check_hook_blobs` four `ls-files` and one `ls-tree`, `check_hook_modes` one,
  and `check_eol` and `check_merge_ours` two each. After, it spends three;
- an invocation whose listing is unusable spends today's reads plus the one `ls-files -s`. Only the
  quoted-path arm of section 7 does so, and it is new.

So the suite's three together fall to at most half of the before reading, at most 1,143 against
2,286. The wired copies' slack, eight of eleven, covers the two new arms many times over.
figure: DERIVED from this section's per-invocation counts and the PINNED suite figures of section 1.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `read_tree_listing` | shell function in `check-wiring.sh` | `sh.function`, lexicon `--suggest` OK | AC1 |
| `read_listed_attrs` | shell function | `sh.function`, lexicon `--suggest` OK | AC1 |
| `read_listed_attr` | shell function | `sh.function` | AC5 |
| `check_listed` | shell function | `sh.function`, lexicon `--suggest` OK | AC3 |
| `_LS`, `_LS_NAMES`, `_LS_OK`, `_LS_ATTRS`, `_LS_ATTRS_OK`, `_LT`, `_LT_READ` | file-scope shell variables | none | AC4 |

### The shell-line rows

Both files sit exactly at their shell-role rows today, 1306 and 1660 code lines by the leg's own
counter, `tools/gate-lint/sh_hygiene.py#measure_code_lines`, PINNED on 2026-11-22 at `c3c0811b8`.
The four new functions and the two new arms add lines to both, so both rows widen. They grow only
through `python tools/memory-tree/ratchet.py widen shell-role`, which the main loop runs, and each
widen writes its record.

### Files touched (estimate)

`tools/check-wiring.sh` · `tools/check-wiring.test.sh` · `memory/project/shell-role.txt` (both rows
widen) · one widen record under `memory/builds/dQuietDisk/build/`.

No other order-4 unit, 11, 15 or 16, names any of these paths in its Files touched as read at
`c3c0811b8`. A sibling whose re-ground adds a shell file would share `memory/project/shell-role.txt`,
a row-per-file ledger, with this unit.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| `git ls-files -z` into a temp file | Bash cannot hold a NUL in a string, and the file is one more temp entry per invocation, the cost this build counts. |
| A here-string over the listing | Bash writes a large one to a temp file, as section 4 measured; a pipe costs none. |
| Unquote C-quoted lines in bash | A second unquoter beside git's; the quoted-line fallback costs one process on a tree that holds such a path, and none elsewhere. |
| A listing persisted across invocations | Its key would be the index, which every commit and every `git add` moves; nothing a second run could reuse safely. |
| Lazy reads at each arm's first use | Several sites sit inside `$(…)`, where a lazily set variable does not survive; the parent-shell call is the idiom `matchers_of` already uses. |
| The suite on the template cache | Not this unit's mechanism; unit 10's ruling kept the suite on its own seed, and this unit changes no fixture. |

## 5. Production-readiness checklist

- security: N/A — reads of the repository's own index and attributes; no input, write path or surface added.
- perf / scale: per `--check` on gov's tree, 21 listing processes become 3; on a tree with a quoted
  path, today's cost plus one. On gov's 15,184 paths, DERIVED by
  `git ls-tree -r --name-only c3c0811b8 | wc -l`, the three strings hold 2,019,606, 1,260,406 and
  2,960,598 bytes, PINNED on 2026-11-22 over this worktree's index. A probe on 2026-11-22, PINNED,
  timed 200 command substitutions at 1,272 to 1,573 ms with the strings held and without, so the
  fork cost does not move. Six `check_listed`-shaped `case` matches over the name column took 72 to
  83 ms, so the ten per `--check` cost about 130 ms, DERIVED, against eighteen git processes saved.
- error / empty / loading states: a failed listing or a quoted line falls back to every per-site call
  (S1); a failed batched attribute read falls back per attribute (S3); an empty index gives empty
  reads, exactly as the per-site calls did.
- observability: none added; the checker's lines are unchanged.
- risks: a site reading the listing where git's pathspec answers differently. AC3's corpus holds the
  cases where the two could part: stages, quoting, case, a trailing slash, another checkout, a
  `--fix` write, a nested hooks directory.
- testing: the real-tree count (AC1), the equivalence runs (AC2, AC3), the fallback (AC4), the
  spawn-site and here-string predicates (AC5), and the suite (AC6, main loop).
- migration: N/A — no state between runs.
- user docs: N/A — no message changes; `help/` describes no check-wiring internals.

## 6. Acceptance criteria

The probes run in a scratch `git clone --shared` of the repository at the build base, under
`%TEMP%` with its own `TEMP`, `TMP` and `TMPDIR`, never in the worktree. "Old" is the clone's own
`tools/check-wiring.sh`; "new" is the unit's file copied over it at the same path, so every printed
path is the same in both runs.

- **AC1** — When `bash tools/check-wiring.sh --check` runs in the clone with `core.hooksPath` set to
  `.githooks` under `GIT_TRACE2_EVENT=<dir>`, old then new, the new trace holds exactly one
  `ls-files`, one `ls-tree` and one `check-attr` `cmd_name` event, and its file count is at least 18
  below the old one. With `TEMP`, `TMP` and `TMPDIR` at one fresh scratch dir per run, sampled by a
  0.5 s watcher, the new run's peak entries are no more than the old run's, and both leave 0.
  Red when: any per-site listing call survives, the batched attribute read runs twice, or the new
  run's peak or residual entries exceed the old run's.
  figure: the old counts were PINNED on 2026-11-22 at `c3c0811b8` as 44, 14, 4 and 3, with 0
  residual entries; both runs are DERIVED at observation.
- **AC2** — When old and new each run `--check` and `--session` in the clone, with `core.hooksPath`
  unset and then set, and `--fix` in a clone re-made at the same path before each run, every pair's
  stdout, stderr and exit code are byte-identical, compared with `cmp`.
  Red when: any byte or any rc differs.
- **AC3** — When a probe builds each fixture below with `git init` in the scratch dir and runs old and
  new in it, `--check` and `--fix` each in a fresh copy, every pair compares equal under `cmp`, and
  the new run's trace shows the listing path taken in every fixture but (b).
  - (a) an index holding stages 1 to 3 of a `merge=rows` path after a conflicted merge;
  - (b) a `ROUTED_PATHS` directory entry whose only tracked file has a non-ASCII name, with
    `core.quotePath=true` set locally;
  - (c) a `ROUTED_PATHS` entry `docs/` beside a tracked FILE named `docs`, and an entry `lib`
    beside tracked `lib/x`;
  - (d) a `ROUTED_PATHS` entry that differs from its tracked directory only in case, with
    `core.ignorecase=true`;
  - (e) `core.hooksPath` naming, by absolute path, the `.githooks` of another worktree of the same
    repository;
  - (f) `.githooks/pre-commit` tracked 100644, under `--fix`;
  - (g) `core.hooksPath` naming a subdirectory `ci/hooks` of this checkout, holding one hook-named
    and one other file.
  Red when: any fixture's two runs differ, or a fixture other than (b) falls back.
  fixture: (b) to (d) take the armed routed fixture the suite already builds, cited in section 4
  under "Case", which needs `node` on `PATH`.
- **AC4** — When a stub `git` placed first on `PATH` exits 128 for `ls-files -s` and runs the real
  git for everything else, and separately when `_LS_OK=1` and `_LS_NAMES=x` are exported into a run
  over the clone, the new checker's output is byte-identical to the old one's in the same state, and
  under the stub the trace shows every per-site call and no `check-attr --stdin eol merge`.
  Red when: a failed listing is read in-process, the batched attribute read runs over an unusable
  listing, or an inherited variable stands in for a read.
- **AC5** — When the spawn-site predicate of section 4 runs over the new `tools/check-wiring.sh`,
  every `ls-files`, `ls-tree` and `check-attr` spawn it prints sits in `read_tree_listing`,
  `read_listed_attrs`, `read_listed_attr`, `check_listed`, `check_hook_modes` (its other-checkout
  read and the `--fix` read-back) or `check_hook_blobs` (one `ls-tree`). Run over blob
  `49c697eccc63` it prints the fourteen sites of section 4. An `awk` that prints the bodies of the
  four new functions, piped to `grep -c '<<'`, prints 0.
  Red when: `check_eol`, `check_hooks`, `check_merge_rows`, `check_merge_ours`, `check_routed` or
  `check_skill_install` still spawns a listing, or a new function reads a string through a
  here-string or a heredoc.
- **AC6** — When the main loop runs the check-wiring suite before and after the unit in a scratch
  `git clone --shared` under `GIT_TRACE2_EVENT`, with `bash tools/lib/extract-arms.sh` taken over the
  suite at both shas, every arm present before is present after with the same verdict, the two new
  arms of section 7 are added, and the after run's `ls-files`, `ls-tree` and `check-attr` events
  together number at most half of the before run's.
  Red when: an arm is lost or changes verdict, or the three do not fall to half.
  permission: a role pass may not run a self-test suite (`tools/unattended/gate-guard.js` row D4);
  the main loop observes this at VERIFYING.
  cost: two suite runs, about 300 s each [PINNED] (the analysis's representative-runs section).
  figure: the bound is DERIVED from section 4; the counts are DERIVED at observation and recorded in
  this unit's acceptance ledger.
- **AC7** — When `python tools/govkit/govkit.py check --target C:/projects/incms/main` and the same
  for `C:/projects/nicocares/main` run read-only from gov before and after this unit, each prints the
  same lines and exits the same.
  Red when: an adopter's check reading moves.
  fixture: `tools/govkit/fixtures/` holds no adopter tree carrying `check-wiring.sh`: its `release-0`
  deploy list and the `adopter-ic-2cff5855` receipt name the kit, and neither holds the script. The
  shipped half is a scratch target that `python tools/govkit/govkit.py apply` installs the
  check-wiring kit into, where old and new run as in AC2. Nothing runs in either `gov-upgrade`
  worktree.

## 7. Gates

`check-wiring self-test` · `transition-audit arms` · `straggler-guard arms` · `kit epoch (shipped bytes move, the version moves)` · `shell hygiene (a loop fed by a command substitution)` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/check-wiring.test.sh · covers AC1 · a `newrepo wired` fixture run under `GIT_TRACE2_EVENT` counts one `ls-files`, one `ls-tree` and one `check-attr`; its failing case restores one per-site `git ls-files --error-unmatch` in a scratch copy of the checker · none
New arm: tools/check-wiring.test.sh · covers AC3 · the armed routed fixture with `ROUTED_PATHS` naming a directory whose one tracked file has a non-ASCII name, `core.quotePath=true` set locally, reads `ok routed`; its failing case reads the quoted listing in-process · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, from the spec task
  `2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task`, with code read at `59e882afd`.
- rev-2 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  5 and section 6 the listing's shell-string size is marked DERIVED from the path count, and the suite
  cost from the analysis PINNED. Design, scope and acceptance unchanged.
- rev-3 · 2026-11-22 · §1 · §2 · §3 · §4 · §5 · §6 · §7 · §10 · S1 · S3 · S9 · AC1 · AC4 · AC5 · AC7 ·
  re-grounded at c3c0811b8 (orders 1 to 3 built), under `2026-11-22-prompt-TOOL-dQuietDisk-11-reground-task`.
  The checker moved by its version line alone, so every citation re-pins to blob `49c697eccc63`
  with no line moved; the predicate finds the fourteen sites in eight functions, not nine, and it is
  now written out. The real-tree count, re-measured, is unchanged at 44, 14, 4 and 3. The path count
  moved to 15,184. Section 5 now states the three strings' sizes as the byte counts measured at
  `c3c0811b8`, in place of rev-2's estimate, and a probe shows the fork cost does not move. The
  consumes-from edge on unit 10 now names its captured config and `newrepo wired`, since unit 10's
  ruling kept the suite off the template cache, and the AC1 arm builds with it. The
  dWitnessedBar edge names its landing merge. S9 and its AC1 and AC5 clauses are added. Why: a probe
  found bash writes a large here-string to a temp file, the cost this build counts. S3 and AC4 now
  say the batched attribute read makes no call over an unusable listing. The bound's per-invocation
  reasoning is restated from the arms that run unconditionally, and the suite figure is stated as
  2,286. The shell-line ledger, where both files sit at their rows, joins the files touched, and
  the gates add the legs that guard it and the shell-line leg.

## 10. Reuse audit

The seam extended is the checker's own read-once idiom: the settings view `matchers_of` builds once in
the parent shell before any arm, and the one python start `resolve_kit_files`
(`tools/check-wiring.sh#matchers_of`, `tools/check-wiring.sh#resolve_kit_files`), both from
TOOL-aBriskPreflight-2, and TOOL-aBriskPreflight-1's one `--stdin` attribute read per site. This unit
applies that idiom to the listing, the attributes and the hooks' tree entries; it adds no second
idiom. TOOL-dQuietDisk-7's template cache and its one switch reader, `read_template_mode` in
`template_cache_sh`, serve suite fixtures, and this unit changes none, so neither is a seam here.

The chain build owning the area is dWitnessedBar (Test: gate health and budgets). It landed at
`685a7a522`, and of its changes this file carries the inline `refuse_wrong_shell` block of its
unit 27 (`tools/check-wiring.sh@49c697eccc63:618`), which this unit does not touch.

`python tools/codebase-map/reuse_lookup.py "list the tracked tree once and answer every tracked-path question in-process"`
returned name-token neighbours only (`tree`, `tracked`, `remove_tree`, `read_memory_tree`); none
lists a git index for a shell consumer. Recall returned TOOL-aBriskPreflight-1 and -2 and their
baseline record, whose traced run named the per-site reads this unit removes; the source agreed.

Recall terms used: `python tools/memory-recall/query.py "how does check-wiring read the tracked tree and attributes once per run" --terms "check-wiring ls-files check-attr stdin listing once per run spawn aBriskPreflight matchers_of view eol merge rows"`
