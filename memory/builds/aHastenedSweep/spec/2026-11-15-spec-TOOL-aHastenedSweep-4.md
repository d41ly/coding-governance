# TOOL-aHastenedSweep-4 — checks 13 to 16 and 17 to 19 run in one Python process over one frozen, memoized walk

**Status:** INPROGRESS · rev-2 · 2026-11-15 · node a · Tier-2 · base f25308f0 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md) | research | TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 |

<!-- /gen:spec-records -->

## 1. Goal

An unscoped hygiene run launches `corpus_ids.py --check` and then `gotchas.py --check`, and each
walks the whole corpus through `corpus_ids.py#walk`: the second walk is `gotchas.py#load_defined_ids`
re-running the first over the same tree. This unit runs both verbs in one interpreter that the
engine launches once, with `walk` memoized inside that process and every caller handed its own deep
copy, so one walk and one interpreter start leave the full run while each check's output bytes,
their order and the exit mapping stay as they are.

## 2. Scope (IN)

- **S1** — `corpus_ids.py` gains a module global `_WALK_MEMO`, `None` at import. When it is a dict,
  `walk(root, conf)` keys on `root` and the sorted `conf` items, stores its result on a miss, and
  returns `copy.deepcopy` of the stored result on every call, the first included. When it is `None`,
  `walk` behaves byte for byte as today. Observed by AC2 and AC3.
- **S2** — `gotchas.py` gains `_load_corpus_ids()`, the importlib load `append_only_re` and
  `load_defined_ids` each spell today, and both call it. Each keeps its own missing-file check and its
  own error wording. Observed by AC1 and AC7.
- **S3** — `gotchas.py` gains a module global `_SHARED_CORPUS_IDS`, `None` at import.
  `load_defined_ids` uses that module when it is set and `grammar_dir` is `None`, and loads a fresh
  one otherwise, so the self-test's absent-kit arm still gets a module of its own. Observed by AC2.
- **S4** — `gotchas.py --check-with-ids` and its `cmd_check_with_ids()`: it loads `corpus_ids`
  once, sets that module's `_WALK_MEMO` to `{}` and `_SHARED_CORPUS_IDS` to it, then runs
  `corpus_ids`' `main(["corpus_ids.py", "--check"])` and this module's `main(["gotchas.py", "--check"])`
  in that order. Each runs with `sys.stdout` and `sys.stderr` redirected to two buffers of its own,
  and an exception out of one prints its traceback into that verb's stderr buffer with rc 1. Its
  stdout carries the frames §4 defines, and it exits 0. Observed by AC1, AC2 and AC6.
- **S5** — The engine's 13 to 16 block, on an unscoped unstaged run, launches the S4 verb once
  instead of `corpus_ids.py --check`. The launch carries `TOOL-aHastenedSweep-3`'s
  `GOV_INDEX_SET_STDIN=$_IXH` prefix and its `<<<"${_IXH:+$INDEX_SET}"` here-string unchanged. The
  shell splits the frames into `ids`, `_idsrc`, `got` and `_gotrc` with parameter expansion only, and
  sets `_onepy=1`. The 17 to 19 block launches `gotchas.py --check` only when `_onepy` is not `1`.
  Under `--only` both blocks launch as today. Observed by AC4 and AC5.
- **S6** — When the S4 verb exits non-zero or its output does not split into two numeric rc fields,
  the shell sets `ids` to the whole capture, `_idsrc=1`, `got=""` and `_gotrc=1`. The run reds and
  prints the capture under the 13 to 16 block. No `status=1` line and no `fail` call is added.
  Observed by AC6 and AC7.
- **S7** — Every line from `# arm-signature: is claimed by` through both blocks' `status=1` and
  offender-key lines stays byte for byte, and the marker stays the nearest one above its site.
  Observed by AC7.
- **S8** — The gotchas row of `tools/memory-tree/README.md` and the usage line of `gotchas.py#main`
  list `--check-with-ids`. The `kit.toml` contract clause whose consumer is `gotchas.py` imports
  `main` beside `ask_shell`. Observed by AC8.
- **S9** — The three `New arm:` lines of §7. Observed by AC1, AC2, AC3 and AC5 through those arms.
- **S10** — On the live tree, the whole hygiene output and its exit code are `cmp`-equal at this
  unit's parent and at this unit. Observed by AC9.

## 3. Non-goals (OUT)

- No hand bump of `KIT_MEMORY_TREE_VERSION`. The brief puts the build's one version move in this
  unit, but `tools/push-main.sh@c7cd70b96d5b:26-31` mints kit versions at the landing and says a
  branch owes no bump. The landing's mint is that one move (§4, Alternatives rejected).
- No one-process run under `--only` or `--staged`. A scoped run pays two launches as it does today.
- No memo of `ask_shell`. `gotchas.py#append_only_re` still asks the shell for
  `--print-append-only-ere` from a fresh module, and the walk's own ask goes away only with the
  memo hit.
- No arming of the `_gotrc` status branch. It stays pinned in `memory/project/unarmed-branches.txt`
  as a delegated, unmarked site, and the new suite arm adds no `# arm-signature:` marker.
- No change to the standalone `corpus_ids.py --check`, `gotchas.py --check` or `--print-defined-ids`.
- No cache across processes or across commits, and no stamp of any result.
- No edit to `memory/map/features/memory-tree-hygiene.md`: `TOOL-aHastenedSweep-3` edits it, and
  this unit adds no bullet it owes.
- No self-test suite and no bar inside the pass, a sliced suite included.

### Edges

- **consumes-from** `TOOL-aHastenedSweep-3` — the `GOV_INDEX_SET_STDIN=$_IXH` prefix and the
  here-string on the `corpus_ids.py --check` launch. S5 carries both onto the one-process launch, and
  without them the hand-down is lost on every unscoped run.
- **hands-off** external — the live-tree A/B of AC9, the arms' red then green, and the close's legs
  of §7. All are the main loop's, at the close, recorded in this unit's acceptance ledger under a
  `Pass: none` commit.

## 4. Design

### Evidence

Read at base f25308f0 on 2026-11-15.

- The 13 to 16 block opens at `tools/memory-tree/check-memory-hygiene.sh@a55d262d1295:3198` and
  launches `corpus_ids.py --check` at `:3209`. The marker `# arm-signature: is claimed by` is at
  `:3213`, its site `[ "$_idsrc" -ne 0 ] && status=1` at `:3214`, and the 13-16 offender-key line at
  `:3215`. The 17 to 19 block opens at `:3220`, launches `gotchas.py --check` at `:3229`, and its
  status and key lines are `:3232-3233`. Nothing prints between the two blocks.
- `check_selected` (`tools/memory-tree/check-memory-hygiene.sh@a55d262d1295:410-411`) appends to
  `RAN` when `ONLY` is set, so S5 tests `ONLY` directly, as `TOOL-aHastenedSweep-3`'s `_IXH` does.
- `memory/project/unarmed-branches.txt@13893e3983fe:101` pins `[ "$_gotrc" -ne 0 ] && status=1` by
  its text. `tools/memory-tree/check-arms.py` reads a `status=1` line as a branch, and reads the
  nearest `# arm-signature:` above a site as its signature.
- `corpus_ids.py#main` runs `check_read_path`, then `walk` only when `armed(conf)` holds, and prints
  every note and finding at its end. `corpus_ids.py#check_read_path` calls `run("git", "ls-files")`
  once (`tools/memory-tree/corpus_ids.py@d5bd676f034e:700`). `walk` calls it once and asks the shell
  for `--print-append-only-ere` once.
- `walk` returns one dict literal (`tools/memory-tree/corpus_ids.py@d5bd676f034e:623`) whose values
  are sets, lists, dicts, strings and the caller's `conf`. `load_conf` values are all `str`, measured
  by a probe on the live tree.
- `corpus_ids.py#_walk_continues` reads `walk`'s own source with `inspect.getsourcelines(walk)`, and
  the selftest asserts every `continue` in it is reached. A wrapper named `walk` around a renamed body
  would make that population empty, so the memo lives inside `walk`.
- `gotchas.py#load_defined_ids` and `gotchas.py#append_only_re` each load a fresh `corpus_ids`
  module through `importlib.util.spec_from_file_location`. `load_defined_ids` returns
  `set(mod.walk(root, mod.load_conf(root))["defs"])`, so it copies before reading.
- `gotchas.py#cmd_check` reaches `load_defined_ids` only when a `kind: invariant` record exists, and
  the live tree holds 3 (PINNED 2026-11-15, `grep -l '^kind: invariant' memory/gotchas/*.md`).
- `gotchas.py#cmd_check` and `corpus_ids.py#main` each print only at their end. Neither `--check`
  path reaches a `sys.stderr` write: `gotchas.py`'s are in `check_ungated`
  (`tools/memory-tree/gotchas.py@0cb445ff98ba:450`), which only its selftest calls, and in
  `--declares`; `walk` reaches `id_grammar.py` only through `grammar` and `anchor_at`, not the
  recall readers that write stderr.
- `gotchas.py#main` reconfigures `sys.stdout` only when it has `reconfigure`, and `io.StringIO` has
  none, so a redirected nested call skips it.
- On node a, one live-tree `walk` took 22.80 s and `copy.deepcopy` of its result 0.049 s (PINNED
  2026-11-15, base f25308f0, contended).
- The fork-count row `memory-hygiene` holds 192 with slack `max(3, 5 %)`
  (`memory/project/fork-ceilings.txt@b5f87c516520:19`). Its fixture runs the 13 to 19 blocks, and
  this unit removes one command substitution there, inside that slack.
- The suite's `_pykeys` reads only a quoted name opening `[A-Z]`
  (`tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a1a3b:3036`), so `_WALK_MEMO` and
  `_SHARED_CORPUS_IDS` need no `_pyexempt` row.

### The frames

`gotchas.py --check-with-ids` writes, through its own `sys.stdout` reconfigured to UTF-8:

```text
<corpus_ids stderr><corpus_ids stdout>\x1d<rc1>\n<gotchas stderr><gotchas stdout>\x1d<rc2>\n
```

`\x1d` is the group-separator byte. Stderr goes ahead of stdout because the two-process form pipes
`2>&1` from an interpreter whose stdout is block-buffered and whose stderr is not, so a traceback
or warning lands ahead of the buffered prints there too. Every byte passes through the same text
wrapper as the standalone verb's, so the newline translation is the same on every node.

### The shell

In the 13 to 16 block's `STAGED=0` branch, with `_onepy=""` set once above the block:

```bash
if [ -z "$ONLY" ]; then
  _both=$(GOV_INDEX_SET_STDIN=$_IXH "$_PY" "$HERE/gotchas.py" --check-with-ids 2>&1 <<<"${_IXH:+$INDEX_SET}") \
    && <split _both into ids, _idsrc, got, _gotrc> && _onepy=1
  [ "$_onepy" = 1 ] || { ids=$_both; _idsrc=1; got=""; _gotrc=1; _onepy=1; }
else
  <TOOL-aHastenedSweep-3's launch line, unchanged>
fi
```

The split takes the text before the first `\x1d` as one block. The rc runs to the next newline, less
one trailing CR. The second block and rc are read the same way. Each block then loses its trailing
newlines one at a time in a `[[ ]]` loop, which is what `$( )` did to the standalone capture. Both
rc fields must match `^[0-9]+$`, or the split fails. The 17 to 19 block wraps its launch line as
`[ "$_onepy" = 1 ] || { <today's line>; }`. Every other line of both blocks is untouched. The split
uses no command substitution and no pipe.

### Why the bytes are equal

Each verb runs its own `main` with its own argv, so it resolves the same root and conf and takes
the same branches. The memo returns a value equal to a fresh walk, because the process walks one
unchanged tree under one `(root, conf)`. It returns a deep copy, so neither verb can see what the
other did to its result. The frames reproduce the two-process capture, and the shell prints each
block from the same lines as today, in the same order.

### What it does not check

- A verb whose stdout passes the pipe buffer before a later stderr write would interleave there in
  the two-process form. Neither `--check` path reaches a stderr write today.
- A traceback's frame list differs from the two-process form's. The exit code does not.
- A crash of the wrapper itself puts the whole capture under the 13 to 16 block. The two-process form
  would have named the crashing verb alone.
- A block carrying the `\x1d` byte fails the split, and the run reds loudly.
- An adopter-owned `corpus_ids.py` without `_WALK_MEMO` is walked twice and stays exact. The contract
  clause measures that `main` exists, not its signature.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `cmd_check_with_ids` | function in `gotchas.py` | `py.function`, lexicon `--suggest` OK |
| `_load_corpus_ids` | function in `gotchas.py` | `py.function`, lexicon `--suggest` OK |
| `_SHARED_CORPUS_IDS` | module global in `gotchas.py` | no constant cell is declared |
| `_WALK_MEMO` | module global in `corpus_ids.py` | no constant cell is declared |
| `--check-with-ids` | CLI flag of `gotchas.py` | none |
| `_onepy`, `_both` | shell globals | none; underscore-led as the engine's private globals |

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/README.md`
- `tools/memory-tree/kit.toml`
- `memory/map/generated/symbols.json`
- `memory/builds/aHastenedSweep/build/2026-11-15-build-TOOL-aHastenedSweep-4-1-acceptance-ledger.md`
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, which the pre-commit manifest ratchet owes whenever the hygiene shell, a watched file, is staged

### Rollout

One pass at order 3, after `TOOL-aHastenedSweep-2` and `TOOL-aHastenedSweep-3` are CLOSED: they
edit `walk`, `gotchas.py` and the 13 to 16 launch line this unit rewrites. The pass runs
`python tools/codebase-map/gen_map.py --write` for the new symbols. The spec lands in a records
commit before the code. The status flip to CLOSED is the pass's last change.

### Alternatives rejected

- **Bump `KIT_MEMORY_TREE_VERSION` here, as the brief says.** The lander mints every kit version the
  landing owes and states that a branch owes none (`tools/push-main.sh@c7cd70b96d5b:26-31`). Whether
  a hand bump makes the mint move it twice is UNVERIFIED, so the code's rule wins.
- **The memo as a wrapper around a renamed walk body.** It empties `_walk_continues`' population and
  turns its arm into a pass that finds nothing.
- **A memo on by default.** Only the one-process verb walks twice over one tree. On by default, every
  other caller of `walk` would share one cache, the selftest's many `walk` calls over the same
  fixture root included, so an arm that edits a fixture between two walks would read a stale result.
- **Freezing with `MappingProxyType` and `frozenset`.** The values nest sets inside dicts, so a
  shallow freeze still lets a caller mutate them. A deep freeze is more code than one `deepcopy` that
  costs 0.049 s (PINNED, above).
- **The verb in `corpus_ids.py`, or in a new module.** `gotchas.py` already loads `corpus_ids`, and
  the reverse import would add an edge. A new module is owed only when neither file can hold the
  entry, and `gotchas.py` can.
- **Two outputs through a temp file.** It needs a `mktemp`, a cleanup and the crash trap. One stdout
  with frames needs none of those.
- **A silent fallback to two launches when the split fails.** A broken verb would then cost speed
  and nothing would say so. The loud form reds, and it adds no new branch.
- **The one-process run whenever both blocks are selected.** It costs a second `check_selected`,
  which writes `RAN`, for a scope only `--only 13,17` reaches. The full bar is unscoped.
- **A dead anchor as the fixture's 17 to 19 failure, as the brief words it.** Check 19's dead-anchor
  line is an advisory at exit 0 (`gotchas.py#cmd_check`), so it reds nothing. A class record naming
  no gate reds check 18.

## 5. Production-readiness checklist

- security — No new write path, surface or grant. The verb reads what the two verbs read today.
- perf / scale — One walk, 22.80 s on node a (PINNED, above), and one interpreter start leave each
  full run. The memo adds one deep copy per call. The leg is re-measured once at the build's close.
- error / empty / loading states — An exception in one verb is framed with rc 1 under its own
  block. A wrapper failure reds under 13 to 16 (S6). An unarmed tree or one with no invariant
  never walks, as today.
- observability — Output unchanged. A broken verb prints its capture rather than falling back
  silently.
- risks — A later edit that prints before a stderr write, or that mutates a walk result in place;
  AC1's arm and AC3's arm red on those.
- testing — The pass runs AC1 to AC8 by hand over fixtures built under `%TEMP%/hs4f`, plus
  `bash -n`, `python -m py_compile`, `check-arms` and the lexicon. The arms and AC9 run at the close.
- migration — N/A — no data, conf key or adopter step changes.
- user docs — N/A — no output or exit code an adopter sees changes. The kit README row names the
  new flag (S8).

## 6. Acceptance criteria

`$SCRATCH` is the run's scratch directory. The fixtures F1 and F2 are git repositories built by the
probe under `%TEMP%/hs4f`, a short path. F1 holds `ORPHAN_ID_PIN` set with no orphan, and one class
record that names no gate. F2 is F1 plus a file citing an id nothing defines, plus one
`kind: invariant` record in the shape `gotchas.py#cmd_selftest` builds. `$KIT` is the worktree's
`tools/memory-tree` as an absolute path.

- **AC1** — When `python "$SCRATCH/t4-frame.py" F1` and then `F2` run, each runs
  `gotchas.py --check-with-ids`, `corpus_ids.py --check` and `gotchas.py --check` in the fixture.
  They print `frame F1 same 0 1` and `frame F2 same 1 1`: each framed block equals that verb's
  standalone capture with its trailing newlines stripped, and each rc field equals its exit code.
  Red when: the rc fields swap, a verb's stderr is dropped, or the two blocks change places.
  fixture: built by the probe; no tree holds one today.
- **AC2** — When `python "$SCRATCH/t4-walk.py" F2` runs `cmd_check_with_ids` in-process with the
  loaded module's `run` wrapped to count `git ls-files` calls, it prints `ls-files 2`. With the
  `_WALK_MEMO = {}` assignment removed as a staged break, it prints `ls-files 3`.
  Red when: the memo is never switched on, or `load_defined_ids` loads a module of its own.
  figure: DERIVED, one call in `check_read_path` and one in the single walk.
- **AC3** — When `python "$SCRATCH/t4-memo.py" F2` runs, it prints `default None`, then
  `frozen yes`: a second `walk` does not show an id added to the first result's `defs`. It prints
  `hit yes`: after a commit adding a defining file, a memoized `walk` lacks the new id. It prints
  `off sees new`: with `_WALK_MEMO` back to `None`, `walk` has it. Last it prints `conf keyed yes`:
  a `walk` under a conf with another `ORPHAN_ID_PIN` returns that conf in `w["conf"]`.
  Red when: the memo hands back its stored object, is on at import, or keys on `root` alone.
- **AC4** — When `env SHELLOPTS=xtrace BASH_XTRACEFD=9 bash "$KIT/check-memory-hygiene.sh"` runs in
  F2 with fd 9 open on a trace file in `$SCRATCH`, `grep -c 'gotchas.py --check-with-ids'` over
  the trace prints 1, and that trace line carries `GOV_INDEX_SET_STDIN=`. No trace line launches
  `corpus_ids.py --check` or `gotchas.py --check` alone. With `--only 13,14,15,16,17,18,19`, the
  trace holds no `--check-with-ids` line and one launch of each standalone verb.
  Red when: the 17 to 19 block launches again after the one-process run, a scoped run takes the
  one-process path, or the hand-down prefix is dropped.
- **AC5** — When `bash "$KIT/check-memory-hygiene.sh"` runs unscoped in F2, it exits 1 and prints a
  `check 14:` line and a `check 18:` line. With `--offenders`, the check 14 line is keyed
  `check 13-16` and the check 18 line `check 17-19`.
  Red when: a block is dropped, the two blocks swap, or one block's rc is read for the other.
- **AC6** — With a `raise RuntimeError` staged as the first line of `cmd_check_with_ids`, the AC5
  run exits 1 and prints the traceback, and `--offenders` keys it under `check 13-16`. Restored, AC5
  holds again.
  Red when: the break leaves the run at exit 0, prints nothing, or launches the two verbs as well.
- **AC7** — When `python tools/memory-tree/check-arms.py --check` runs it exits 0.
  `grep -cxF '  [ "$_gotrc" -ne 0 ] && status=1' tools/memory-tree/check-memory-hygiene.sh` prints 1,
  and the same grep for the `_idsrc` line prints 1. `bash -n` on both shell files and
  `python -m py_compile` on both modules exit 0.
  Red when: the edit rewrites a pinned or armed status line, adds a `status=1` or `fail` site, or
  moves the claimant marker off its site.
- **AC8** — When `grep -c -- '--check-with-ids' tools/memory-tree/README.md` runs it prints at least
  1 on the `gotchas.py` row, `python tools/memory-tree/gotchas.py --nope` prints a usage line naming
  `--check-with-ids`, and the `kit.toml` clause above `consumer = "gotchas.py"` reads
  `imports = ["ask_shell", "main"]`.
  Red when: the verb ships unlisted, or the contract omits the name it calls.
- **AC9** — When the whole `check-memory-hygiene.sh` runs from the worktree root on the live tree,
  once from this unit's parent's `tools/` extracted with `git archive` under `%TEMP%/hs4a` and once
  from the unit's own, `cmp` of the two outputs exits 0 and the exit codes match.
  Red when: any byte of any check's output moves, checks 13 to 19 included.
  cost: two full hygiene runs, each about 805–1093 s on node a (PINNED, 2026-11-15 bar ledgers).
  permission: the main loop's at the close, under a `Pass: none` commit; a unit pass does not run it.
  fixture: the live tree at the close's tip.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `corpus-ids selftest` · `gotchas selftest` · `harness arms (fail branches armed or pinned)` · `spawn budget (forks per hot entrypoint)` · `shell hygiene (a fork spent on builtin work)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `playbook render selftest` · `policy fixtures`

New arm: tools/memory-tree/gotchas.py --selftest · covers AC1 AC2 · the frame's rc fields swapped, then the `_WALK_MEMO = {}` assignment removed · none
New arm: tools/memory-tree/corpus_ids.py --selftest · covers AC3 · `walk` returning its stored object, then `_WALK_MEMO` set to `{}` at import, then a key on `root` alone · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 · the shell split assigning the 17 to 19 block to `ids` and the 13 to 16 block to `got` · `FLOOR_ASSERTIONS` raised by the arm's assertion count

A pass checks its own change with `bash -n`, `python -m py_compile`, `check-arms`, the lexicon and
the AC1 to AC8 commands over its fixtures. The close runs the bar once and observes each arm red
then green. AC9 is the main loop's at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft from `prompts/2026-11-15-prompt-TOOL-aHastenedSweep-1-brief.md`,
  grounded at f25308f0 and against `TOOL-aHastenedSweep-3`'s rev-1 launch line.
- rev-2 · 2026-11-15 · Files touched names the kickoff manifest's `last-audit` re-stamp, which editing the
  hygiene shell owes; the builder's divergence return of 2026-11-15 found it missing. The version move stays
  the lander's mint, as section 3 states.

## 10. Reuse audit

The seams this unit extends: `tools/memory-tree/corpus_ids.py#walk`, memoized in place, and
`tools/memory-tree/gotchas.py#load_defined_ids`, which already reaches `walk` in-process. The verb
sits beside `gotchas.py#cmd_check`, and the shell keeps both blocks' print, status and offender-key
lines. `python tools/codebase-map/reuse_lookup.py "run two corpus checkers in one process sharing
one memoized walk"` ranked `run`, `check` and `walk` first, the last being this seam. No existing
seam frames two verbs' output in one process, so that part is new, and it reuses `main` of both
modules unchanged.
Recall named `TOOL-dTotalRecall-23` (the walk runs twice per hygiene run) and `TOOL-aReplayedCard-10`
(a walk plus the shell probe per call).

Recall terms used: `python tools/memory-recall/query.py "how do the hygiene shell's python
delegations share one corpus walk" --terms "hygiene corpus_ids walk gotchas load_defined_ids
delegation one process memoized shared state checks 13-19"`
