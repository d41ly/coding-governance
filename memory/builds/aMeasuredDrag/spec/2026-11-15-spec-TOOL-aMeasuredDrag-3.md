# TOOL-aMeasuredDrag-3 — carries coverage derived once per process, and the staged hygiene run reads checks 29 and 30 from check 9's process

**Status:** SPECCED · rev-1 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-3-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-3-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-3-readers-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-3-readers-brief.md) | research | TOOL-aMeasuredDrag-4 |

<!-- /gen:spec-records -->

## 1. Goal

A staged records commit runs the build-index generator three times, for checks 9, 29 and 30, and
the coverage join is derived in two of them. A full hygiene run derives it twice in one process.
This unit derives the coverage once per `--with-verdicts` call and admits `--with-verdicts` beside
`--staged`, so the staged hygiene run reads checks 29 and 30 from check 9's one process. Every
verdict and every line checks 9, 29 and 30 print stays as it is.

## 2. Scope (IN)

- **S1** — `read_carries_coverage` in `tools/memory-tree/gen_build_index.py` returns a memoised
  value while the module global `_COVERAGE_MEMO` is a dict, keyed on `(root, path, resolve)`, where
  `path` is the carries checker's path the function already computes. With `_COVERAGE_MEMO` at
  `None`, its default, every call derives as today. A refusal is never memoised. Observed by AC1.
- **S2** — `main()` admits `--check --staged --with-verdicts`. It sets `_COVERAGE_MEMO = {}` on
  each of the two `--with-verdicts` paths and resets it to `None` in a `finally` on its handler.
  Under `--staged` it prints the verdict sections first, flushes stdout, then runs today's staged
  block unchanged. Without `--staged` the call runs as today. Observed by AC2, AC5, AC6.
- **S3** — `print_check_verdicts(root, conf, staged=False)` calls each verb as
  `verb(root, conf, staged=True)` when `staged` is true, and as `verb(root, conf)` otherwise, so a
  verb under `--staged` prints its held line exactly as its standalone run does. Observed by AC2.
- **S4** — The usage refusal keeps `--with-verdicts` to `--check` alone and drops its `--staged`
  half: its text loses "and never --staged", and the usage line spells `--check [--staged]
  [--with-verdicts]`. Observed by AC3.
  **Readers:**
  by name: `tools/memory-tree/gen_build_index.py` is the only tracked file outside the build
  records that spells the retired text, by a git grep at writing. Its `main` prints the refusal at
  `:8851`, with the text split across two string literals so that no file spells the phrase whole,
  and the comment above it at `:8847` says the flag is never beside `--staged`.
  by value: `read_flag_refusals`, the selftest arm at `:5209`, counts the refusal output's
  `the flag takes --check alone`, a phrase the edit keeps. Its refused tuples and its expected
  count move with §4's A3. AC3 reads the output for `never --staged`. No other reader compares,
  counts or derives from the text.
- **S5** — `tools/memory-tree/check-memory-hygiene.sh`: check 9 passes `--with-verdicts` whenever
  `ONLY` is empty, `--staged` included. Checks 29 and 30 read check 9's section on a full run as
  today, and under `--staged` only when check 9's capture holds the end marker; otherwise they run
  their own verb as today. The comments that say a staged run spawns its own verbs are made true.
  Observed by AC4, AC5, AC7.
- **S6** — The kit README's two paragraphs on `--check-coverage` and `--check-asbuilt`
  (`tools/memory-tree/README.md@86d507b0:373`, `:389`) say the staged form is admitted, and that a
  staged hygiene run reads both verdicts from check 9's process. Observed by AC8.
- **S7** — The selftest arms of §4, "The arms", in `tools/memory-tree/gen_build_index.py`.
  Observed by AC1, AC2, AC3.
- **S8** — A measured before and after of the staged hygiene run and of `--check --with-verdicts`,
  each beside a spawn baseline, written into this unit's acceptance ledger. Observed by AC9.

## 3. Non-goals (OUT)

- A cross-process or content-keyed cache of the coverage, the review's §5 structural item.
- A memo on any path but the two `--with-verdicts` calls. `cmd_write`, `cmd_check` alone and
  `--check-coverage` alone each read the coverage once and stay unmemoised.
- `check_staged_render`, the render trigger, and the verbs' own staged triggers.
- `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`. Their checks 29 and 30 say "A
  full run, `--staged` off and no `--only`, reads this verdict from check 9's generator process",
  and "Under `--staged` the check passes `--staged` through". Both stay true: the staged run passes
  `--staged` to the verb inside check 9's process. They are governance carriers, so nothing here
  edits them.
- `tools/memory-tree/gen_build_index.py:1199-1212`, the per-build grouping, which is
  `TOOL-aMeasuredDrag-6`'s.
- The kit version: the lander's mint moves it.
- Any verdict, refusal or printed line other than the three S4 names, which the brief's item 3
  orders. F1 states the one crash-path difference.

### Edges

- **hands-off** external — a coverage cache that outlives one process is the review's §5 structural
  work, outside this build.

## 4. Design

### Evidence

Read at base `aebbb4a72`. Lines name blobs of that tree.

| Line | What sits there |
|---|---|
| `tools/memory-tree/gen_build_index.py@5a0864b8:1990` | `read_carries_coverage`: blank key returns the off value; else loads the checker and derives |
| `tools/memory-tree/gen_build_index.py@5a0864b8:2748` | `plan()` reads the coverage once per render |
| `tools/memory-tree/gen_build_index.py@5a0864b8:2960` | `cmd_check_coverage` under `staged` prints its held line and returns before any read |
| `tools/memory-tree/gen_build_index.py@5a0864b8:2967` | `cmd_check_coverage` reads the coverage |
| `tools/memory-tree/gen_build_index.py@5a0864b8:3048` | `print_check_verdicts` calls each verb as `verb(root, conf)` under captured stdout and stderr |
| `tools/memory-tree/gen_build_index.py@5a0864b8:8850` | the usage refusal of `--with-verdicts` beside `--staged` or any mode but `--check` |
| `tools/memory-tree/gen_build_index.py@5a0864b8:8919` | the staged block: the render decision, its SKIPPED or owed line, then `cmd_check` |
| `tools/memory-tree/gen_build_index.py@5a0864b8:8925` | the `--with-verdicts` block, `sys.stderr` bound to stdout for the call |
| `tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1496` | check 9 adds `--with-verdicts` only when `STAGED` is 0 and `ONLY` is empty |
| `tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1937` | check 29 reads check 9's section when `_v9on` is 1; check 30's twin is at `:1978` |
| `tools/memory-tree/gen_build_index.py@5a0864b8:2306` | `_SLOT_MODE`, the module's "asked once per run and kept" global |

Under `--staged`, check 9 runs only when `STAGED_MD` is non-empty (`:1494`), so a commit staging
only the conf leaves `_v9on` at 0 and checks 29 and 30 run their own verbs, as today.

### The memo

```python
# TOOL-aMeasuredDrag-3. The coverage, derived once per `--with-verdicts` call. `main()` sets a dict for
# that call alone, where check 29's verb and `plan()` read it over one root and one conf, and resets it
# to None after. None reads through, which the selftest needs: its arms re-read one fixture root after
# changing its tree.
_COVERAGE_MEMO = None
```

In `read_carries_coverage`, after the blank-key return and the `path` line, `key = (root, path,
resolve)` and a hit returns the stored value. The two closing returns become one: the off value or
the derived value is stored under `key` when `_COVERAGE_MEMO` is a dict, then returned. An exception
leaves nothing stored, so a second read raises again, as today.

The key carries `resolve`, the stub the selftest injects (`:4872-4906`), and `path`, which those arms
move by rebinding `CARRIES_CHECKER`. The arms call the function outside `main()`, so the memo is
`None` there and they read through whatever the key says.

Why not a memo for the whole process: the selftest calls `cmd_check_coverage` and `plan()` over one
root and one conf before and after rewriting a spec's status (`gen_build_index.py@5a0864b8:4736-4745`).
A process memo would hand the second read the first tree's value and red those arms.

Neither reader mutates the value. `plan()` stores the off value itself on each build, or builds a new
dict from its fields. `cmd_check_coverage` reads `builds`, `specs`, `findings` and `cutoff`.

### The two `--with-verdicts` paths in `main()`

The refusal keeps one condition, `with_verdicts and mode != "--check"`, with the text
`usage: gen_build_index.py --check --with-verdicts — the flag takes --check alone; given <argv>`.
The usage line's `[--check [--staged|--with-verdicts]|` becomes `[--check [--staged] [--with-verdicts]|`.

Under `--staged` with the flag, before the render decision:

```python
            if with_verdicts:
                _COVERAGE_MEMO = {}
                print_check_verdicts(root, conf, staged=True)
                sys.stdout.flush()
```

Then the staged block runs unchanged: SKIPPED and exit 0, or the owed line and `cmd_check`. Its
`sys.stderr` is not rebound. The flush puts the end marker on the pipe before `cmd_check` writes any
stderr line, so the hygiene capture holds, after the marker, exactly what today's `--check --staged`
capture holds, in the same order.

The full path, `--with-verdicts` without `--staged`, keeps its block and its stderr binding, and
sets `_COVERAGE_MEMO = {}` first. The handler's `try` gains `finally: _COVERAGE_MEMO = None`.

The verdict sections print before the render decision. So a staged render that skips still prints
each verb's held line, and a staged render that is owed derives the coverage once: the verb stores it
and `plan()` reads it back.

### Check 9's capture under `--staged`

```
-  [ "$STAGED" = 0 ] && [ -z "$ONLY" ] && { _c9+=(--with-verdicts); _v9on=1; }
+  [ -z "$ONLY" ] && { _c9+=(--with-verdicts); _v9on=1; }
```

Checks 29 and 30 each change one condition:

```
-if [ "${_v9on:-0}" = 1 ]; then
+if [ "${_v9on:-0}" = 1 ] && { [ "$STAGED" = 0 ] || [ "$_v9end" = 1 ]; }; then
```

Under `--staged`, a capture with no end marker is a generator that died before its sections ended.
Each check then runs its own verb as today, so a crash before the marker prints what it prints today.
On a full run the unmarked capture stays the unreadable branch, as dTrueNorth-27 set it.

The shell keeps the three constraints `TOOL-dTrueNorth-27` S4 states: no new `fail` call, no new
`<<<` site, no new spawn-idiom site. Check 9's `if ! drift=$(…)` form is kept.

Comments made true: the block above check 9 (`check-memory-hygiene.sh@d9ce5710:1486`) says the
process prints both verdicts whenever `--only` is empty, `--staged` included, and names the
fallback. Check 29's "UNDER --staged THE VERB DECIDES" paragraph (`:1925`) says the verb decides
inside check 9's process. "ON A FULL RUN THE VERDICT IS CHECK 9'S SECTION" (`:1932`) and check 30's
one-line twin (`:1976`) say the section is read whenever check 9 ran with the flag.

### Output parity

| Run | Check 9 | Checks 29 and 30 |
|---|---|---|
| full | unchanged | unchanged |
| `--staged`, check 9 runs, render skips | the SKIPPED line, as today | each verb's held line, from the section |
| `--staged`, check 9 runs, render owed | today's message, its stderr order unchanged | the verb's lines, from the section |
| `--staged`, check 9 does not run | not run | their own verbs, as today |
| `--staged`, generator dies before the marker | today's failure | their own verbs, as today |
| `--staged`, a verb raises a non-`Problem` | unchanged | the section's `exit 2` line: F1 |
| `--only` set | as today | their own verbs, as today |

A verb's `Problem` prints `build-index: <message>` under exit 2 in-process and standalone alike.

### The arms

In `tools/memory-tree/gen_build_index.py`:

- **A1, the memo** (in `test_coverage_stub`). With `_COVERAGE_MEMO` set to a dict, two reads with
  one counting stub derive once and return one object, and a second stub derives once more. A stub
  raising `ImportError` is a `Problem` on each of two reads and is called twice. With
  `_COVERAGE_MEMO` back at `None`, two reads derive twice. The arm restores `None` in a `finally`.
- **A2, the staged verdicts** (beside `_read_ordered31`). A child, built as `child31` is, stubs the
  three verbs to record whether `staged` came in true and whether the memo was set, and runs
  `main(['x', '--check', '--staged', '--with-verdicts'])` in its scratch repository, which stages
  nothing. Its merged output opens `build-index: verdict 29 exit 0`, the stub's line, `build-index:
  verdict 30 exit 0`, the stub's line and `build-index: verdicts end`, then the SKIPPED line. Both
  verbs saw `staged` true with the memo set, and `_COVERAGE_MEMO` is `None` after `main` returns.
- **A3, the usage refusal** (`read_flag_refusals`). The `("--check", "--staged", "--with-verdicts")`
  tuple leaves the refused list, and the expectation becomes `[2, 2] 2`. The arm's label drops
  "beside --staged".

The hygiene suite's staged arms (`tools/memory-tree/check-memory-hygiene.test.sh@4c50ac3a:4489` and
`:4554`) now reach the held lines through check 9's section and assert them unchanged.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/README.md`

### Inventory

| Identifier | Kind | Note |
|---|---|---|
| `_COVERAGE_MEMO` | module global | named as `_SLOT_MODE` and `_SLOT_DATA_DIR` are; not at base; no declared lexicon cell grades it, since `lexicon.py --suggest _COVERAGE_MEMO --as py.constant` answers that cell is undeclared |

`print_check_verdicts` gains a keyword parameter. No function is added, so
`memory/map/generated/symbols.json` does not move.

### Rollout

Live, with no switch: no verdict moves, and a dark path would be exercised by no commit.

### Alternatives rejected

- **`functools.lru_cache` on the reader.** The conf is a dict, which does not hash, and a
  process-lifetime cache reds the selftest's re-reads (§4, "The memo").
- **Handing the value from `print_check_verdicts` to `cmd_check`.** It threads a parameter through
  `cmd_check` and `plan()`, which the three unlanded branches the build README names also edit.
- **Rebinding `sys.stderr` under `--staged` as the full path does.** It reorders check 9's red
  message under `--staged`: today the stderr notices of `cmd_check` precede its buffered stdout.
- **No fallback in checks 29 and 30.** A generator that dies before the marker under `--staged`
  would then red checks 29 and 30 as unreadable, where today they run in processes of their own.
- **Skipping the coverage read when no chain spec is INPROGRESS** (githooks-2's second fix). The
  region renders the coverage whatever the statuses, so `plan()` still owes the read.

### What the design does not check

- That a later edit leaves a write between the verdicts and `plan()`. The verbs and
  `check_staged_render` write nothing at base. A writer added there would let `plan()` read a value
  derived before the write.
- A call of `main()` from inside another `main()`. Nothing does that today.

## 5. Production-readiness checklist

- security — no new input, write path or surface; the generator reads the same files.
- perf / scale — removes one coverage derivation per `--with-verdicts` call, and two generator
  processes per staged hygiene run that reaches check 9.
  records-3 profiled `read_carries_coverage` at 31.1 s of 89.9 s, PINNED 2026-11-15.
  githooks-2 measured `--check-coverage --staged` at 19.5 s, PINNED 2026-11-15.
  AC9 measures this unit's code.
- error / empty / loading states — a `Problem` is never memoised; a crash before the marker falls
  back to today's processes; a commit that leaves check 9 unrun is unchanged.
- observability — no line moves outside S4 and the F1 case.
- risks — an adopter with a new hygiene script beside an old generator reds check 9 under
  `--staged` on the usage refusal; the kit installs both files together, and checks 29 and 30 fall
  back to their own verbs on that capture.
- testing — AC1 to AC9 and the arms on the `New arm:` lines in §7.
- migration — N/A: no data or record shape moves.
- user docs — the kit README (S6); no page under `help/` describes checks 29 and 30.

## 6. Acceptance criteria

- **AC1** — When the probe below runs from the repository root, it prints `OK`.
  ```
  python -c "
  import sys; sys.path.insert(0, 'tools/memory-tree'); import gen_build_index as g
  n = []; v = {'state': 'armed', 'cutoff': 'x', 'builds': {}}
  def mk(tag): return lambda p: (n.append(tag), (lambda root, conf=None: v))[1]
  def bad(p): n.append('bad'); raise ImportError('planted')
  conf = {'MEMORY_ROOT': 'memory', g.CARRIES_KEY: '2026-01-01'}; one, two = mk('one'), mk('two')
  g._COVERAGE_MEMO = {}
  a = g.read_carries_coverage('.', conf, one); b = g.read_carries_coverage('.', conf, one)
  g.read_carries_coverage('.', conf, two)
  for _ in (1, 2):
      try: g.read_carries_coverage('.', conf, bad)
      except g.Problem: pass
  g._COVERAGE_MEMO = None
  g.read_carries_coverage('.', conf, one); g.read_carries_coverage('.', conf, one)
  assert a is b is v and n == ['one', 'two', 'bad', 'bad', 'one', 'one'], n; print('OK')"
  ```
  Red when: the memo ignores `resolve`, stores a refusal, or reads through while set.
- **AC2** — When the probe below runs from the repository root, it prints `OK`.
  ```
  python -c "
  import sys, io, contextlib; sys.path.insert(0, 'tools/memory-tree'); import gen_build_index as g
  seen = []
  def cov(root, conf, staged=False): seen.append(('29', staged, g._COVERAGE_MEMO is not None)); print('c29'); return 0
  def ab(root, conf, staged=False, here=None): seen.append(('30', staged, g._COVERAGE_MEMO is not None)); print('c30'); return 0
  def chk(root, conf): seen.append(('9', g._COVERAGE_MEMO is not None)); print('drift'); return 0
  g.cmd_check_coverage, g.cmd_check_asbuilt, g.cmd_check = cov, ab, chk
  out = io.StringIO()
  with contextlib.redirect_stdout(out): rc = g.main(['x', '--check', '--staged', '--with-verdicts'])
  head = out.getvalue().splitlines()[:5]
  assert head == ['build-index: verdict 29 exit 0', 'c29', 'build-index: verdict 30 exit 0', 'c30', 'build-index: verdicts end'], head
  assert seen[:2] == [('29', True, True), ('30', True, True)] and g._COVERAGE_MEMO is None, seen
  seen.clear()
  with contextlib.redirect_stdout(io.StringIO()): g.main(['x', '--check', '--with-verdicts'])
  assert seen == [('29', False, True), ('30', False, True), ('9', True)] and g._COVERAGE_MEMO is None, seen
  print('OK')"
  ```
  Red when: `--staged` is still refused, the verbs are not handed `staged`, the sections print after
  the render decision, or the memo outlives `main`.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --write --with-verdicts` and
  `python tools/memory-tree/gen_build_index.py --check-coverage --with-verdicts` run, each exits 2
  printing `the flag takes --check alone`, and neither output carries `never --staged`.
  Red when: the refusal is lifted for any mode but `--check`, or its text still names `--staged`.
- **AC4** — When `bash -x tools/memory-tree/check-memory-hygiene.sh --staged` runs in the AC5 clone
  over case B, its trace carries one line spelling `gen_build_index.py --check --staged
  --with-verdicts`, and `grep -c` for `gen_build_index.py --check-coverage` and for
  `gen_build_index.py --check-asbuilt` over it prints 0 each.
  Red when: check 9 still withholds the flag under `--staged`, or check 29 or 30 still spawns.
  fixture: as AC5.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh --staged > out 2>&1; echo $? >> out`
  runs in a clone at `%TEMP%/md3`, once at the unit's parent commit and once at the unit's commit,
  over each case below, `diff` of the two `out` files prints nothing for each case. In each
  checkout, `python tools/memory-tree/gen_build_index.py --write` runs first, then the case's edit is
  made and staged, and `git reset -q --hard` follows.
  - case A, render skips: `printf '\n' >> memory/README.md && git add memory/README.md`.
  - case B, render owed: `printf '\n' >> memory/builds/aBriskDeclaration/README.md`, then `git add`.
  Red when: any line or the exit differs, such as a held line missing from check 29 or 30.
  fixture: the clone; it holds every build of this tree, a chain build under `SPEC_CARRIES_CUTOFF`
  included.
  cost: case B renders the whole index.
  githooks-1 timed a whole staged hygiene run at 78.7 s, PINNED 2026-11-15.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --check --with-verdicts` and
  `python tools/memory-tree/gen_build_index.py --check-coverage` run in the AC5 clone at the parent
  and at the unit's commit, after the same `--write`, each pair's stdout and exit compare equal by
  `diff`.
  Red when: the memoised value differs from a fresh derivation, which the second read would show.
  fixture: as AC5.
- **AC7** — When, in the AC5 clone at the unit's commit over case B, `gen_build_index.py` is edited
  in the work tree to raise `RuntimeError("planted")` at the top of `main()` whenever
  `--with-verdicts` is in its argv, `bash tools/memory-tree/check-memory-hygiene.sh --staged` prints
  check 9's failure carrying `planted`, and its `memory-hygiene: check 29:` and `check 30:` lines equal
  those of the unplanted case B run.
  Red when: the fallback condition is missing, so checks 29 and 30 read the unmarked capture and
  fail as unreadable.
  fixture: as AC5, the edit unstaged.
- **AC8** — When `grep -c 'beside \`--staged\`' tools/memory-tree/README.md` runs it prints 0, and
  `grep -c -- '--check --staged --with-verdicts' tools/memory-tree/README.md` prints at least 1.
  Red when: the README still states the staged form is refused, or never names it.
- **AC9** — When the AC5 case B run and the AC6 `--check --with-verdicts` run are each timed with
  `time`, at the parent and at the unit's commit, and `time (for i in 1 2 3 4 5 6 7 8 9 10; do
  /usr/bin/true; done)` is timed beside each, the acceptance ledger records the eight wall times and
  each after-run is shorter than its before-run.
  Red when: an after-run is not shorter than its before-run.
  figure: every time is DERIVED at observation and recorded in the ledger with its date.

## 7. Gates

`memory hygiene` · `memory hygiene (the pass checks)` · `memory-hygiene self-test` · `build-index selftest` · `tier2-review self-test` · `policy fixtures` · `harness arms (fail branches armed or pinned)` · `kit/dogfood doc parity` · `spec tokens (a spec's own names resolve)` · `docs`

New arm: tools/memory-tree/gen_build_index.py --selftest · covers AC1 · `read_carries_coverage` at base, which has no memo, so the set-memo reads derive twice; and a key without `resolve`, under which the second stub reads the first stub's value · none
New arm: tools/memory-tree/gen_build_index.py --selftest · covers AC2 · `main()` at base, which refuses `--check --staged --with-verdicts` with exit 2 and prints no section · none
New arm: tools/memory-tree/gen_build_index.py --selftest · covers AC3 · the refusal at base, which also refuses the staged tuple, so the list reads `[2, 2, 2] 3` · none

The close's hygiene suite run re-observes, unchanged, the check 29 and check 30 staged held-line arms,
which now read check 9's section.

## 8. Open questions

- **F1 — Under `--staged`, may a verb's own crash print the in-process heading?** A verb raising
  anything but a `Problem` prints today, standalone, a traceback with exit 1, which check 29 files
  under "a chain build's spec is INPROGRESS while its build's coverage is red". In check 9's process
  it prints `build-index: <type>: <message>` under exit 2 (`TOOL-dTrueNorth-31` S12), which check 29
  files under "the coverage could not be read". The check fails either way, and the hygiene exit
  does not move. (a) Accept: the in-process heading is the truthful one, the full run already prints
  it, and the brief's item 3 orders this route. (b) Park the flag half and ship the memo alone,
  which keeps the staged path's two extra processes. Recommendation: (a).

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.

## 10. Reuse audit

The seam is `read_carries_coverage` in `tools/memory-tree/gen_build_index.py`, the one reader the
region and check 29's verb share, edited in place as the brief's Reuse names; the memo follows
`_SLOT_MODE` and `read_slot_mode` in the same module, its "asked once per run and kept" global. The
staged route extends `print_check_verdicts` and check 9's existing section split
(`TOOL-dTrueNorth-27` S4) rather than adding a reader. `tools/codebase-map/reuse_lookup.py`, given
"memoise a derived value once per process", ranked `read_policy_value`, `derive_kit_prefix` and
other `derive_*` names by name stem, none a memo, so no existing seam fits a shared cache and the
module's own global is the precedent. Recall returned `TOOL-dTrueNorth-27` S4, whose refusal of the
staged form this unit lifts for the reason that spec gave: the staged skip would print no verdict,
and here the sections print before the skip. `gotchas.py --for-paths` selected
`swallowed-delegate-reads-as-clean`, answered by checks 29 and 30 reading the section only under the
end marker, and `fixture-passes-by-finding-nothing`, answered by AC5's case B, which renders.

Recall terms used: `python tools/memory-recall/query.py "carries coverage derived twice in the staged
hygiene run, and with-verdicts refused beside staged" --terms "carries coverage memo with-verdicts
staged check 29 check 30 verdict sections generator process"`
