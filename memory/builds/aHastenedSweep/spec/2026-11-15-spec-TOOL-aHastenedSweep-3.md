# TOOL-aHastenedSweep-3 — the hygiene shell hands `corpus_ids.py --check` its index set when checks 1 to 5 ran clean

**Status:** INPROGRESS · rev-2 · 2026-11-15 · node a · Tier-2 · base f25308f0 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md) | research | TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-4 |

<!-- /gen:spec-records -->

## 1. Goal

When `check-memory-hygiene.sh` launches `corpus_ids.py --check`, check 16 asks for the index set by
spawning that same shell again in `--print-index-set` mode, which re-runs the prologue and checks 1
to 5 only to print a set the parent already holds. This unit hands the parent's `INDEX_SET` down on
the child's stdin whenever the parent's own checks 1 to 5 ran and recorded no failure, so the spawn
is skipped and every verdict, output byte and exit code stays as it is today.

## 2. Scope (IN)

- **S1** — The shell computes one eligibility flag, `_IXH`, right after its `--print-index-set`
  print-mode line: `1` when the run is unscoped (`ONLY` empty), unstaged (`STAGED=0`) and `status`
  is still `0`, else empty. Observed by AC1, AC2 and AC3.
- **S2** — The shell's one launch of `corpus_ids.py --check` sets `GOV_INDEX_SET_STDIN=$_IXH` as a
  command prefix on every run, eligible or not, and feeds `${_IXH:+$INDEX_SET}` as a here-string.
  Observed by AC1 and AC2.
- **S3** — `corpus_ids.py#check_read_path` reads its index set from stdin when
  `GOV_INDEX_SET_STDIN` is exactly `1`, decoded UTF-8 with the newline translation the
  `ask_shell` capture applies, and otherwise calls `ask_shell("--print-index-set", root)` as today.
  Observed by AC1 and AC4.
- **S4** — The hygiene suite's python parity exemption list, `_pyexempt`, names
  `GOV_INDEX_SET_STDIN` with its reason, because `_pykeys` derives that name from the new
  `os.environ.get` read. Observed by AC5.
- **S5** — `check-memory-hygiene.test.sh` gains the arms §7 declares, over the existing `_b1`
  fixture tree. Observed by AC1 to AC4 through the `New arm:` lines of §7.
- **S6** — The memory-tree hygiene dossier's `--print-index-set` bullet says the engine hands the set
  down to its own launch of `corpus_ids.py` and that the print mode stays the standalone route.
  Observed by AC6.
- **S7** — On the live tree, the hygiene run's checks 13 to 16 block is byte-identical with and
  without the hand-down. Observed by AC7.

## 3. Non-goals (OUT)

- No change to `ask_shell`, to `--print-append-only-ere`, or to `walk`: the append-only ask in
  `corpus_ids.py#walk` and `gotchas.py#append_only_re` is out of this unit.
- No hand-down under `--only`, even when the list names checks 1 to 5: a scoped run takes today's
  path. The `--only 13,14,15,16` run pays the spawn as it does now.
- No change to the standalone CLI's default: `corpus_ids.py --check` with no hand-down spawns the
  shell's print mode as today.
- No merge of the 13 to 16 and 17 to 19 launches. That is `TOOL-aHastenedSweep-4`'s mechanism, and
  rewrites this same launch line; whichever of the two is built second carries the other's change to
  it, and this unit's prefix and here-string must survive the merge.
- No memory-tree kit version move: the brief places the one move in `TOOL-aHastenedSweep-4`.
- No new CLI flag, no temp file and no exported variable.

### Edges

- **hands-off** `TOOL-aHastenedSweep-4` — the `GOV_INDEX_SET_STDIN=$_IXH` prefix and the
  here-string on the `corpus_ids.py --check` launch, which that unit carries onto its one-process
  launch.

## 4. Design

### Evidence

- The print mode exits right after checks 1 to 5:
  `tools/memory-tree/check-memory-hygiene.sh@a55d262d12:1184`, after `INDEX_SET` is computed once at
  `tools/memory-tree/check-memory-hygiene.sh@a55d262d12:1176`. Check 1 opens at `:821` and check 5 at
  `:1083` of the same blob. Nothing assigns `INDEX_SET` after `:1176`.
- `status` starts at `0` (`tools/memory-tree/check-memory-hygiene.sh@a55d262d12:315`) and moves only
  through `fail()` (`tools/memory-tree/check-memory-hygiene.sh@a55d262d12:406`), which echoes
  `HYGIENE check <n> FAILED` unless `--offenders` is set and sets `status=1` either way. Between the
  python resolution at `:615` and `:1184` no line assigns `status`, and the only `fail` calls sit in
  checks 1 to 5.
- `corpus_ids.py#ask_shell` refuses a print-mode answer carrying a line that opens `HYGIENE `, with
  the "answered with findings" message. In the child, such a line comes from `fail()` in checks 1
  to 5, so in an unscoped, unstaged run the parent's `status` at `:1184` is `0` exactly when the
  child would answer without findings.
- `corpus_ids.py#check_read_path` is the only caller of `ask_shell("--print-index-set", root)`; the
  shell's launch at `tools/memory-tree/check-memory-hygiene.sh@a55d262d12:3209` is the only launch of
  `corpus_ids.py --check` under `tools/`, `.githooks/` and `skills/` (`grep -rn`).
- `check_selected` (`tools/memory-tree/check-memory-hygiene.sh@a55d262d12:410`) records into `RAN`
  as a side effect, so the flag tests `ONLY` directly rather than calling it again.
- The suite's `_pykeys` (`tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a1a:3036`) derives
  every upper-case name read through `.get(` or `[`, and `_pyexempt` at `:3078` of that blob lists the
  environment names it must not demand in the example conf.
- The `_b1` fixture (`tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a1a:3311`) is clean, has
  no pin set, and tracks `AGENTS.md` citing `memory/README.md`, which is an `index_set` member.
- `gotchas.py#append_only_re` asks the shell only when the catalogue exists, and `_b1` has none.

### The shell

One line after the print-mode line:

```bash
_IXH=""; [ "$STAGED" = 0 ] && [ -z "$ONLY" ] && [ "$status" = 0 ] && _IXH=1   # TOOL-aHastenedSweep-3
```

The launch line becomes:

```bash
ids=$(GOV_INDEX_SET_STDIN=$_IXH "$_PY" "$HERE/corpus_ids.py" --check 2>&1 <<<"${_IXH:+$INDEX_SET}"); _idsrc=$?
```

The prefix is written on every run, so a `GOV_INDEX_SET_STDIN=1` inherited from the caller's
environment is overwritten with an empty value whenever the run is not eligible. A here-string is
not a pipeline, so `_idsrc` stays the interpreter's exit code. `<<<` appends one newline, which is
the byte `printf '%s\n' "$INDEX_SET"` adds in print mode. When not eligible the child reads no
stdin, and a defect that read it anyway would get an empty set, which check 16 rule 3 reports
loudly rather than passing.

A comment above the flag names why the snapshot sits at the print-mode line: checks 6 onward also
call `fail`, so the launch site's `status` no longer answers "did checks 1 to 5 fail".

### The module

In `check_read_path`, the `capped` line reads:

```python
if os.environ.get("GOV_INDEX_SET_STDIN") == "1":   # handed down by check-memory-hygiene.sh
    raw = sys.stdin.buffer.read().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
else:
    raw = ask_shell("--print-index-set", root)
capped = {l for l in raw.split("\n") if l.strip()}
```

The decode and the two replacements are what `subprocess` text mode applies to the `ask_shell`
capture, which passes `encoding="utf-8"` and no `errors`, so a handed set and an asked set parse
to the same members. Stdin is read once per process; `check_read_path` runs once per `--check`.

### Inventory

| Identifier | Kind | Lexicon |
|---|---|---|
| `GOV_INDEX_SET_STDIN` | environment name | no environment cell; `GOV_` prefix as `GOV_BASH` and `GOV_PYTHON` |
| `_IXH` | shell global | no shell-variable cell; leading underscore as the engine's other private globals |

Neither name occurs in the tree at base outside this build's records, by `git grep -w`.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/map/features/memory-tree-hygiene.md`

### Alternatives rejected

- The set in an environment variable's value: the index set is about 17 KB, PINNED at f25308f0 by a
  `git ls-files` count of its member kinds. Windows caps one variable at 32767 characters, PINNED
  from its platform documentation, and the set grows with every build README.
- A temp file named by an environment variable: Git-Bash's `mktemp` path is a POSIX path, and whether
  MSYS converts it on the way to a native interpreter is UNVERIFIED; stdin carries the bytes with no
  path at all, and `gotchas.py --declares` already reads its input from stdin.
- A CLI flag on `corpus_ids.py`: it reaches only the argv it is written on, so `TOOL-aHastenedSweep-4`'s
  one-process entry would have to re-thread it, where an environment read inside `check_read_path`
  reaches every entry that calls it.
- Hand-down under `--only` when the list holds 1 to 5: a per-id test over `ONLY` for a scope nobody
  runs with 13 to 16; the unscoped test is a strict subset of "checks 1 to 5 ran", so it stays exact.

## 5. Production-readiness checklist

- security: no new write path; the read is the process's own stdin, honoured only on the exact value
  `1`, and the shell sets that value on its own launch line, never exported.
- perf / scale: one fewer bash spawn of the prologue and checks 1 to 5 per full hygiene run; the
  saving is re-measured once at the build's close against the whole leg, not per unit.
- error / empty / loading states: an empty handed set behaves as an empty asked set; a failed checks
  1 to 5 run takes today's path, so the "answered with findings" refusal still fires (AC2, AC3).
- observability: unchanged output; the dossier names the hand-down (AC6).
- risks: a later edit that drops the prefix or the here-string; AC1's arm reds on both.
- testing: the `New arm:` lines of §7 over the `_b1` fixture; the pass verifies by running the AC1 to
  AC4 commands by hand over a copy of that fixture, and the suite and the live-tree parity run at the
  close.
- migration: N/A — no data, conf key or adopter step changes.
- user docs: N/A — no flag, output or exit code an adopter sees changes; the dossier is updated.

## 6. Acceptance criteria

- **AC1** — When `GOV_BASH=<a path that does not exist> bash check-memory-hygiene.sh` runs in the
  `_b1` fixture tree, its output carries no `corpus_ids: GOV_BASH is set` line and no
  `check 16 rule 3` line.
  Red when: the launch has no `GOV_INDEX_SET_STDIN` prefix or no here-string, or `check_read_path`
  ignores the variable, so `ask_shell` resolves the missing bash; or the handed set is empty, so rule 3
  names `memory/README.md`.
  fixture: `_b1` in the hygiene suite, at its base conf; at base f25308f0 the arm is red.
- **AC2** — When a copy of the `_b1` tree stages a stray `stray.md` at the memory root, which the root-file check refuses, and
  `bash check-memory-hygiene.sh` runs there, once plain and once with `GOV_INDEX_SET_STDIN=1`
  exported, both outputs carry that check's `FAILED` line and `answered with findings`.
  Red when: `_IXH` ignores `status`, or the launch sets the variable only when eligible so the
  exported value reaches the child.
- **AC3** — When `bash check-memory-hygiene.sh --only 16` runs in the AC2 tree, its output carries
  `answered with findings`.
  Red when: `_IXH` ignores `ONLY`, so a set is handed down although checks 1 to 5 never ran.
- **AC4** — When `GOV_BASH=<a path that does not exist> python corpus_ids.py --check` runs in the
  clean `_b1` tree with `GOV_INDEX_SET_STDIN` unset, its output carries
  `corpus_ids: GOV_BASH is set`.
  Red when: `check_read_path` reads stdin with the variable unset or set to anything but `1`.
- **AC5** — When the `_pykeys` ERE runs over `tools/memory-tree/*.py`, it yields
  `GOV_INDEX_SET_STDIN`, and `grep -n GOV_INDEX_SET_STDIN` over the hygiene suite finds it in
  `_pyexempt` and in the comment above it.
  Red when: `_pyexempt` omits it, which the suite's `_pyparity` reports as an undeclared key.
- **AC6** — When `grep -n GOV_INDEX_SET_STDIN memory/map/features/memory-tree-hygiene.md` runs, it
  finds the sentence in the `--print-index-set` bullet.
  Red when: the dossier still says `corpus_ids.py` only asks through the print mode.
- **AC7** — When the full `check-memory-hygiene.sh` runs on the live tree at the shipped engine and at
  this unit's engine, the checks 13 to 16 blocks are `cmp`-equal and the exit codes match.
  Red when: the handed set differs from the asked one in a member check 16 reads.
  cost: two full hygiene runs, minutes each on node a.
  permission: the main loop's at the close, recorded in this unit's acceptance ledger under a
  `Pass: none` commit; a unit pass does not run it.
  fixture: the live tree at the close's tip.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `corpus-ids selftest` · `gotchas selftest` · `policy fixtures` · `playbook render selftest` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 · the shipped engine at base f25308f0, whose `corpus_ids` resolves the missing `GOV_BASH`; then the here-string emptied, which makes rule 3 name `memory/README.md` · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 · `_IXH` set with the `status` test dropped, then with the `ONLY` test dropped, then with the prefix written only when `_IXH` is `1` · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC4 · `check_read_path` testing `!= "1"` · none

A pass checks its own change with `bash -n` on both shell files, `python -m py_compile` on
`corpus_ids.py`, `check-arms`, the lexicon, and the AC1 to AC5 commands run by hand over a copy of
the `_b1` tree. The close runs the merge bar once and observes each arm red then green; AC7's parity
is the main loop's at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.
- rev-2 · 2026-11-15 · AC2 names the stray-file refusal by what it checks, not by its number, which the positional leg reds as an unlisted citation (main loop, pass legs after unit 1).

## 10. Reuse audit

The seams this unit extends: the shell's own `INDEX_SET` and its one launch of `corpus_ids.py`, and
`corpus_ids.py#check_read_path`, the only reader of `--print-index-set`. The stdin hand-down follows
`gotchas.py --declares`, which reads its input as UTF-8 bytes from stdin. The suite arms extend the
`_b1` fixture rather than building a tree. `tools/codebase-map/reuse_lookup.py "hand a set the parent
shell already computed to a child python checker"` ranked `check`, `checks`, `set_env_aside` and
`resolve_python` first; none hands a computed set across a process boundary, so no existing seam fits
the hand-down itself. Recall surfaced the dSpentCeiling review's M1, which is why the refusal exists,
and the aMeteredSweep research naming this spawn's cost.

Recall terms used: `python tools/memory-recall/query.py "how does corpus_ids get the index set from
the hygiene shell without re-running it" --terms "corpus_ids ask_shell print-index-set INDEX_SET
hygiene check 16 read path stdin hand-down checks 1-5 answered with findings"`
