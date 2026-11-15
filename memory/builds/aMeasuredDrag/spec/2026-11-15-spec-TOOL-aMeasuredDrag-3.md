# TOOL-aMeasuredDrag-3 — carries coverage derived once per `--check --with-verdicts` call

**Status:** CLOSED · rev-2 · 2026-11-15 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-build-TOOL-aMeasuredDrag-3-1-acceptance-ledger.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-3-1-acceptance-ledger.md) | journal | — |
| [2026-11-15-build-TOOL-aMeasuredDrag-3-red-fix-1.md](../build/2026-11-15-build-TOOL-aMeasuredDrag-3-red-fix-1.md) | red-fix | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-3-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-3-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-3-2-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-3-2-builder.md) | journal | — |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-3-readers-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-3-readers-brief.md) | research | TOOL-aMeasuredDrag-4 |
| [2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md](../reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md) | diff-review | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |

<!-- /gen:spec-records -->

## 1. Goal

A full hygiene run's check 9 calls `gen_build_index.py --check --with-verdicts`, and that one process PINNED 2026-11-15
derives the carries coverage twice: check 29's verb reads it, then `plan()` reads it again under
`cmd_check`. This unit derives it once per `--check --with-verdicts` call. Every verdict, refusal and
printed line stays as it is.

The brief's second half, admitting `--with-verdicts` beside `--staged` so that a staged hygiene run
reads checks 29 and 30 from check 9's process, is not built. F1 resolved as option (b): that half
moves the printed heading of a verb's crash under `--staged`, so it is parked for the owner, and a
staged records commit keeps its three generator processes.

## 2. Scope (IN)

- **S1** — `read_carries_coverage` in `tools/memory-tree/gen_build_index.py` returns a memoised
  value while the module global `_COVERAGE_MEMO` is a dict, keyed on `(root, path, resolve)`, where
  `path` is the carries checker's path the function already computes. With `_COVERAGE_MEMO` at
  `None`, its default, every call derives as today. A refusal is never memoised. Observed by AC1.
- **S2** — `main()` declares `global _COVERAGE_MEMO`, sets `_COVERAGE_MEMO = {}` in its
  `--with-verdicts` block (`gen_build_index.py@5a0864b8:8925`) before `print_check_verdicts` runs,
  and resets it to `None` in that block's `finally`, beside the `sys.stderr` restore. The usage
  refusal, the staged block and every other mode run as today. Observed by AC2 and AC6.
- **S7** — The selftest arms of §4, "The arms", in `tools/memory-tree/gen_build_index.py`.
  Observed by AC1 and AC2.
- **S8** — A measured before and after of `--check --with-verdicts`, beside a spawn baseline,
  written into this unit's acceptance ledger. Observed by AC9.

## 3. Non-goals (OUT)

- A cross-process or content-keyed cache of the coverage, the review's §5 structural item.
- A memo on any path but the `--check --with-verdicts` call. `cmd_write`, `cmd_check` alone,
  `--check --staged` and `--check-coverage` alone each read the coverage at most once and stay
  unmemoised.
- The staged half, parked under F1 (b). `--with-verdicts` beside `--staged` stays refused, with the
  usage refusal at `gen_build_index.py@5a0864b8:8850` and its text unchanged. `print_check_verdicts`,
  `tools/memory-tree/check-memory-hygiene.sh` and `tools/memory-tree/README.md` are not edited, so a
  staged hygiene run still runs the verbs of checks 29 and 30 in processes of their own.
- `check_staged_render`, the render trigger, and the verbs' own staged triggers.
- `memory/HYGIENE.md` and `tools/memory-tree/HYGIENE.template.md`. No route of checks 29 and 30
  moves, so their text stays true. They are governance carriers, so nothing here edits them.
- `tools/memory-tree/gen_build_index.py@5a0864b8:1199-1212`, the per-build grouping, which is
  `TOOL-aMeasuredDrag-6`'s.
- The kit version: the lander's mint moves it.
- Any verdict, refusal or printed line. None moves.

### Edges

- **hands-off** external — a coverage cache that outlives one process is the review's §5 structural
  work, outside this build.
- **hands-off** external — the staged half, `--check --staged --with-verdicts` with checks 29 and 30
  reading check 9's section, parked for the owner by F1 (b) with the price F1 states.

## 4. Design

### Evidence

Read at base `aebbb4a72`. Lines name blobs of that tree.

| Line | What sits there |
|---|---|
| `tools/memory-tree/gen_build_index.py@5a0864b8:1990` | `read_carries_coverage`: blank key returns the off value; else loads the checker and derives |
| `tools/memory-tree/gen_build_index.py@5a0864b8:2748` | `plan()` reads the coverage once per render |
| `tools/memory-tree/gen_build_index.py@5a0864b8:2967` | `cmd_check_coverage` reads the coverage |
| `tools/memory-tree/gen_build_index.py@5a0864b8:3048` | `print_check_verdicts` calls each verb as `verb(root, conf)` under captured stdout and stderr |
| `tools/memory-tree/gen_build_index.py@5a0864b8:8850` | the usage refusal of `--with-verdicts` beside `--staged` or any mode but `--check` |
| `tools/memory-tree/gen_build_index.py@5a0864b8:8925` | the `--with-verdicts` block, `sys.stderr` bound to stdout for the call |
| `tools/memory-tree/check-memory-hygiene.sh@d9ce5710:1496` | check 9 adds `--with-verdicts` only when `STAGED` is 0 and `ONLY` is empty |
| `tools/memory-tree/gen_build_index.py@5a0864b8:2306` | `_SLOT_MODE`, the module's "asked once per run and kept" global |

`:2748` and `:2967` are the only callers of `read_carries_coverage` outside the selftest at base. In
a `--check --with-verdicts` call, check 29's verb reads it first, under `print_check_verdicts`, and
`plan()` reads it second, under `cmd_check`. `cmd_check_asbuilt` does not read the coverage. Both
readers call it with `resolve` at `None`, so they share one key.

### The memo

```python
# TOOL-aMeasuredDrag-3. The coverage, derived once per `--check --with-verdicts` call. `main()` sets a
# dict for that call alone, where check 29's verb and `plan()` read it over one root and one conf, and
# resets it to None after. None reads through, which the selftest needs: its arms re-read one fixture
# root after changing its tree.
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

### The `--with-verdicts` block in `main()`

`main()` gains `global _COVERAGE_MEMO` as its first statement. The block becomes:

```python
        if with_verdicts:
            held = sys.stderr
            sys.stderr = sys.stdout
            _COVERAGE_MEMO = {}
            try:
                print_check_verdicts(root, conf)
                return cmd_check(root, conf)
            finally:
                sys.stderr = held
                _COVERAGE_MEMO = None
```

Check 29's verb derives the coverage and stores it, and `plan()` under `cmd_check` reads it back.
Nothing else in the block moves, so the sections, their order and the stderr binding are today's.

### Output parity

Both readers receive the one value a fresh derivation would give, because nothing writes between
them (§4, "What the design does not check") and neither mutates it. So `--check --with-verdicts`
prints what it prints today, and every other mode reads through. AC6 compares the outputs.

### The arms

In `tools/memory-tree/gen_build_index.py`:

- **A1, the memo** (in `test_coverage_stub`). With `_COVERAGE_MEMO` set to a dict, two reads with
  one counting stub derive once and return one object, and a second stub derives once more. A stub
  raising `ImportError` is a `Problem` on each of two reads and is called twice. With
  `_COVERAGE_MEMO` back at `None`, two reads derive twice. The arm restores `None` in a `finally`.
- **A2, the memo's lifetime** (beside `_read_ordered31`). A child, built as `child31` is, stubs
  `cmd_check_coverage`, `cmd_check_asbuilt` and `cmd_check` to record whether the memo was set, and
  runs `main(['x', '--check', '--with-verdicts'])` in its scratch repository. All three saw the memo
  set, and `_COVERAGE_MEMO` is `None` after `main` returns.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`

### Inventory

| Identifier | Kind | Note |
|---|---|---|
| `_COVERAGE_MEMO` | module global | named as `_SLOT_MODE` and `_SLOT_DATA_DIR` are; not at base; no declared lexicon cell grades it, since `lexicon.py --suggest _COVERAGE_MEMO --as py.constant` answers that cell is undeclared |

No function is added and no signature changes, so `memory/map/generated/symbols.json` does not move.

### Rollout

Live, with no switch: no verdict moves, and a dark path would be exercised by no commit.

### Alternatives rejected

- **`functools.lru_cache` on the reader.** The conf is a dict, which does not hash, and a
  process-lifetime cache reds the selftest's re-reads (§4, "The memo").
- **Handing the value from `print_check_verdicts` to `cmd_check`.** It threads a parameter through
  `cmd_check` and `plan()`, which the three unlanded branches the build README names also edit.
- **Skipping the coverage read when no chain spec is INPROGRESS** (githooks-2's second fix). The
  region renders the coverage whatever the statuses, so `plan()` still owes the read.

### What the design does not check

- That a later edit leaves a write between the verdicts and `plan()`. The verbs write nothing at
  base. A writer added there would let `plan()` read a value derived before the write.
- A call of `main()` from inside another `main()`. Nothing does that today.

## 5. Production-readiness checklist

- security — no new input, write path or surface; the generator reads the same files.
- perf / scale — removes one coverage derivation per `--check --with-verdicts` call, which a full
  hygiene run makes once, through check 9.
  records-3 profiled `read_carries_coverage` at 31.1 s of 89.9 s, PINNED 2026-11-15.
  AC9 measures this unit's code.
- error / empty / loading states — a `Problem` is never memoised, and the `finally` resets the memo
  on every exit of the block.
- observability — no line moves.
- risks — a writer later added between the verdicts and `plan()` (§4, "What the design does not
  check").
- testing — AC1, AC2, AC6, AC9 and the arms on the `New arm:` lines in §7.
- migration — N/A: no data or record shape moves.
- user docs — N/A: no flag, line or behaviour a user sees moves; no page under `help/` describes
  checks 29 and 30.

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
  def cov(root, conf, staged=False): seen.append(('29', g._COVERAGE_MEMO is not None)); return 0
  def ab(root, conf, staged=False, here=None): seen.append(('30', g._COVERAGE_MEMO is not None)); return 0
  def chk(root, conf): seen.append(('9', g._COVERAGE_MEMO is not None)); return 0
  g.cmd_check_coverage, g.cmd_check_asbuilt, g.cmd_check = cov, ab, chk
  with contextlib.redirect_stdout(io.StringIO()): rc = g.main(['x', '--check', '--with-verdicts'])
  assert rc == 0 and seen == [('29', True), ('30', True), ('9', True)] and g._COVERAGE_MEMO is None, seen
  seen.clear()
  with contextlib.redirect_stdout(io.StringIO()): g.main(['x', '--check-coverage'])
  assert seen == [('29', False)] and g._COVERAGE_MEMO is None, seen
  print('OK')"
  ```
  Red when: `main()` sets no memo for the `--with-verdicts` call, sets one on another mode, or the
  memo outlives `main`.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --check --with-verdicts` and
  `python tools/memory-tree/gen_build_index.py --check-coverage` run in a clone of this repository at
  `%TEMP%/md3`, once at the unit's parent commit and once at the unit's commit, each checkout first
  running `python tools/memory-tree/gen_build_index.py --write` and ending with `git reset -q --hard`,
  each pair's stdout and exit compare equal by `diff`.
  Red when: the memoised value differs from a fresh derivation, which the second read would show.
  fixture: the clone; it holds every build of this tree, a chain build under `SPEC_CARRIES_CUTOFF`
  included, so the coverage is armed and not empty.
  cost: each checkout renders the whole index once.
- **AC9** — When the AC6 `--check --with-verdicts` run is timed with `time`, at the parent and at the
  unit's commit, and `time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)` is timed beside
  each, the acceptance ledger records the four wall times and the after-run is shorter than the
  before-run.
  Red when: the after-run is not shorter than the before-run.
  figure: every time is DERIVED at observation and recorded in the ledger with its date.

## 7. Gates

`memory hygiene` · `memory hygiene (the pass checks)` · `memory-hygiene self-test` · `build-index selftest` · `tier2-review self-test` · `policy fixtures` · `harness arms (fail branches armed or pinned)` · `kit/dogfood doc parity` · `spec tokens (a spec's own names resolve)` · `docs`

New arm: tools/memory-tree/gen_build_index.py --selftest · covers AC1 · `read_carries_coverage` at base, which has no memo, so the set-memo reads derive twice; and a key without `resolve`, under which the second stub reads the first stub's value · none
New arm: tools/memory-tree/gen_build_index.py --selftest · covers AC2 · `main()` at base, which sets no memo, so every stub records it unset · none

## 8. Open questions

- **F1 — Under `--staged`, may a verb's own crash print the in-process heading?**
  RESOLVED (agent, 2026-11-15, delegated): (b) — (a) changes the printed heading of a verb's crash
  under --staged, a printed line under the README's rule (M3 veto 1); the memo ships alone and the
  --staged --with-verdicts half is parked for the owner.
  A verb raising anything but a `Problem` prints today, standalone, a traceback with exit 1, which
  check 29 files under "a chain build's spec is INPROGRESS while its build's coverage is red". In PINNED 2026-11-15
  check 9's process it prints `build-index: <type>: <message>` under exit 2 (`TOOL-dTrueNorth-31`
  S12), which check 29 files under "the coverage could not be read". The check fails either way, and PINNED 2026-11-15
  the hygiene exit does not move. (a) Accept: the in-process heading is the truthful one, the full
  run already prints it, and the brief's item 3 orders this route. (b) Park the flag half and ship
  the memo alone, which keeps the staged path's two extra processes. Recommendation: (a).

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.
- rev-2 · 2026-11-15 · §1 · S2 · S3 · S4 · S5 · S6 · S8 · §3 · §4 · §5 · AC2 · AC3 · AC4 · AC5 · AC6 ·
  AC7 · AC8 · AC9 · §7 · §8 · §10 · F1 resolved as (b) under the run's delegation
  (`2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief`): the staged half is parked for the owner
  and the memo ships alone. S3 to S6 are removed, S4's Readers clause with them, and so are AC3, AC4,
  AC5, AC7, AC8 and the A3 arm; no removed number is reused. S2, S8, AC2 and AC9 are cut to the
  `--check --with-verdicts` call, and AC6 carries its own clone fixture. S1 and AC1 are unchanged.

## 10. Reuse audit

The seam is `read_carries_coverage` in `tools/memory-tree/gen_build_index.py`, the one reader the
region and check 29's verb share, edited in place as the brief's Reuse names; the memo follows
`_SLOT_MODE` and `read_slot_mode` in the same module, its "asked once per run and kept" global, and
it is set inside the existing `--with-verdicts` block of `main()` rather than on a new path.
`tools/codebase-map/reuse_lookup.py`, given "memoise a derived value once per process", ranked
`read_policy_value`, `derive_kit_prefix` and other `derive_*` names by name stem, none a memo, so no
existing seam fits a shared cache and the module's own global is the precedent. Recall returned
`TOOL-dTrueNorth-27` S4, whose refusal of the staged form this unit keeps under F1 (b).
`gotchas.py --for-paths` selected `swallowed-delegate-reads-as-clean`, which no longer applies
because no capture route moves, and `fixture-passes-by-finding-nothing`, answered by AC6's clone,
whose coverage is armed over a chain build.

Recall terms used: `python tools/memory-recall/query.py "carries coverage derived twice in the staged
hygiene run, and with-verdicts refused beside staged" --terms "carries coverage memo with-verdicts
staged check 29 check 30 verdict sections generator process"`
