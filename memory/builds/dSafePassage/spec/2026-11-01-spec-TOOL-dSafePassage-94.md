# TOOL-dSafePassage-94 — the round-5 closing review's two minors: the floor stub's fallback read in process, and each stand-in shape run from its own source

**Status:** CLOSED · rev-1 · 2026-11-01 · node a · Tier-2 · base c86d51fa · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dSafePassage-94-ledger.md](../build/2026-11-01-build-TOOL-dSafePassage-94-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-94-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-94-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-94-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-94-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-94-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-94-spec-brief.md) | research | — |
| [2026-11-01-review-TOOL-dSafePassage-94-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dSafePassage-94-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-5 closing diff review confirmed a medium, id 1. `[dSP-91 L2]` grades a tail, and a tail
cannot show which spawn crashed. So a spawn crash inside `resolve_bash` reads as the stub's fallback
at `tools/govkit/steps/python_floor.py:36`. It also confirmed a low, id 2. `read_stub_tail` leaves
the stand-in's bytecode cache between shapes, so a future shape the same size as the one before it
would run that shape's bytecode. Both are test arms inside `check_floor_bash`, and both close at the
skeptic's fix: an in-process read of `resolve_shell_argv` for id 1, its corrected fix, and the cache
removed before each write for id 2. Each fix carries the review's left-shift arm, so its failing
case is staged on every run.

## 2. Scope (IN)

- **S1** — id 1, the fallback read in process. In `check_floor_bash`
  (`tools/govkit/selftest.py:4430`), a nested function `read_fallback_argv(steps)` saves
  `steps._BASH`, sets it to `None`, and returns `steps.resolve_shell_argv(["bash", "x"])` or the
  exception the call raised. It restores `steps._BASH` in a `finally`. Inside the `GOV_BASH`-unset
  `set_environ` block of `[dSP-91 L2]` (`:4474-4475`) it reads `us`. A `[dSP-94]` check asserts
  the read is `["bash", "x"]`. `test_floor_fallback` (`:4458-4467`) is not changed, so it keeps
  grading the tail only. §4 "S1". Observed by AC1, AC2 and AC3.
- **S2** — id 1's left-shift arm, the regression staged in a copy. A module `steps94` is
  `tools/govkit/upgrade_steps.py`'s source with `check_runs`' `except OSError:` (`:399`) narrowed
  to `except ValueError:`, run in this process. The same block reads it, and a second `[dSP-94]`
  check asserts the read is an `OSError`. §4 "S2". Observed by AC1 and AC2.
- **S3** — id 2, the cache cleared. `read_stub_tail` (`selftest.py:4493-4499`) clears
  `stub92 / "__pycache__"` with `shutil.rmtree` before each write or unlink. After each write it pins the stand-in's
  mtime to one value, so only the source's size tells two stand-ins apart. §4 "S3". Observed by
  AC1, AC2 and AC3.
- **S4** — id 2's left-shift arm, the same-length two-body probe. After the `[dSP-92]` loop, two
  stand-ins of one length run in a row: the absent-program body, then a body that raises
  `RuntimeError("dsp94-second")`. A third `[dSP-94]` check asserts the lengths match and the second
  tail names `dsp94-second`. §4 "S4". Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- A `want=False` `[dSP-92]` tail shape for a stand-in that spawns an absent program, as the
  finder's fix for id 1 proposes. The skeptic measured that tail byte-identical to the
  `want=True` "finds no bash" shape, so no tail predicate can tell them apart.
- Any change to `test_floor_fallback` or to the seven `[dSP-92]` shapes.
- id 2's other fix, a nonce line giving each body a unique length. The skeptic judged the cache's
  removal sound, and a nonce leaves the cache in place for the next author to collide with.
- The checklist entries the review's two left-shift notes name. The review records that no
  checklist is present, so the main loop owns those entries, and this unit's arms are the gates.
- The `check_floor_bash` docstring (`selftest.py:4431-4434`). Each new check's comment names this
  unit, and leaving the docstring alone keeps the diff to added lines only.
- Product code. `tools/govkit/upgrade_steps.py` and `tools/govkit/steps/python_floor.py` are read
  and not edited.

### Edges

none

## 4. Design

Every cited line holds at `c86d51fa5`, the build head with TOOL-dSafePassage-92 and -93 landed.
The measurements were taken on 2026-11-01 on node a, Windows, Python 3.15, in a scratch tree made
by `git archive c86d51fa5 tools` and committed. The fenced text below was staged into it as
written, and AC1's command was run green and under each of AC2's breaks.

### Why a tail cannot carry id 1

`resolve_shell_argv` calls `resolve_bash` and falls back to the bare argv only on a `Refusal`
(`upgrade_steps.py:437-440`). `resolve_bash` tests each candidate with `check_runs`
(`:396-400`), which turns a spawn's `OSError` into `False`. Narrow that catch and the `OSError`
escapes `resolve_shell_argv`, so the stub dies before `python_floor.py:36` is reached. On Windows
the `subprocess.py` frames fill the 20-line tail (`upgrade_steps.py:1798`) and push out the frames
that show where the spawn was. `test_floor_fallback` forgives an `OSError` under a
`subprocess.py` frame, so it reads that crash as the fallback. Measured with the regression staged
at `c86d51fa5`: `[dSP-91 L2]` reads `ok`, and no check in `check_floor_bash` goes red.

The read in this process answers it. What the stub's `steps.resolve_shell_argv` hands back is
the gov module's own answer under the same environment. A crash raised there is an exception
here, not a tail.

### S1: the read

Inserted before the `[dSP-91 L2]` comment (`selftest.py:4470`). `types` is imported at `:32`:

```python
    def read_fallback_argv(steps: types.ModuleType) -> object:
        # TOOL-dSafePassage-94: what `steps` hands the stub for a bare bash, read in this process with
        # its cached bash cleared, or the exception the call raised. A spawn crash's tail cannot show
        # which spawn crashed, so this read is what proves the call reaches its fallback.
        held = steps._BASH
        steps._BASH = None
        try:
            return steps.resolve_shell_argv(["bash", "x"])
        except Exception as e:  # noqa: BLE001 - a crash inside resolve_bash is what this reads
            return e
        finally:
            steps._BASH = held
```

The `[dSP-91 L2]` block (`:4474-4477`) gains one line inside its `with`, and two checks follow the
`[dSP-91 L2]` check, which is not changed:

```python
    with set_environ({"PATH": path87, "GOV_BASH": None, "GOV_PYTHON": sys.executable}):
        got = us.run_step_isolated(floor_row, "witness", GOV_ROOT, GOV_ROOT)
        argv94, cut94 = read_fallback_argv(us), read_fallback_argv(steps94)
    check("[dSP-91 L2] the floor row's witness, no bash resolving and GOV_BASH unset, falls back to bare bash",
          test_floor_fallback(got["tail"]), str(got))
    check("[dSP-94] resolve_shell_argv on that PATH, GOV_BASH unset and no bash cached, hands back bare bash",
          argv94 == ["bash", "x"], repr(argv94))
    check("[dSP-94] the same read, check_runs narrowed to catch ValueError, reads the spawn's OSError",
          isinstance(cut94, OSError), repr(cut94))
```

Clearing `_BASH` is load-bearing. `resolve_bash` returns its cache first (`upgrade_steps.py:392-394`),
and `bash87 = us.resolve_bash()` (`selftest.py:4440`) fills it with the parent's bash. Measured:
with the clear cut, the read returns `['C:\\Program Files\\Git\\usr\\bin\\bash.exe', 'x']`. The
`finally` gives the cache back, so the arms after this one read it as before. The memo save, clear
and restore is the shape of the `GOV_BASH` override arm (`selftest.py:18498-18509`).

On that `PATH` the read reaches the fallback. `fake87`'s `bash.exe` and `bash` are text files, so
`check_runs` turns their spawn's `OSError` into `False` (`upgrade_steps.py:417-418`). `keep87` holds
only directories with no bash and the System32 or WindowsApps launchers, which `:414-416` skip.
So `:421` raises the `Refusal`, and `:439-440` hand back the argv unchanged.

The `except Exception` returns the exception rather than letting it abort the suite, so the check
records a `FAIL` with the exception's repr. Measured with the regression staged in
`upgrade_steps.py:399`: `FAIL [dSP-94] resolve_shell_argv ... — OSError(22, "This version of %1 is
not compatible ...")`, which is `[WinError 216]`, while `[dSP-91 L2]` still reads `ok`.

### S2: the regression, staged in a copy

Inserted after `read_fallback_argv`. `HERE` is the engine directory (`selftest.py:68`):

```python
    # TOOL-dSafePassage-94: the regression that read must see, check_runs no longer catching a spawn's
    # OSError, staged in a copy of upgrade_steps.py, so the read is seen red on every run.
    steps94 = types.ModuleType("dsp94_upgrade_steps")
    steps94.__file__ = str(HERE / "upgrade_steps.py")
    exec(compile((HERE / "upgrade_steps.py").read_text(encoding="utf-8").replace(
        "returncode == 0\n        except OSError:", "returncode == 0\n        except ValueError:"),
        steps94.__file__, "exec"), steps94.__dict__)
```

The replaced text occurs once in `upgrade_steps.py`, at `:398-399`, measured. `read_text` folds a
CRLF checkout to `\n`, so the match holds on either line ending. `__file__` is set because
`upgrade_steps.py:134` reads it, and measured without it the `exec` raises `NameError`. The
module's name is not `__main__`, so `:138-139` do not register it in `sys.modules`. The staged
copy follows `selftest.py:7734-7736`, which runs a staged `govkit.py` the same way.

If the replaced text ever moves, the copy is the real module, its read is `["bash", "x"]`, and the
second `[dSP-94]` check reads `FAIL`. Measured. So the staged regression cannot pass vacuously.

### S3: the cache removed

`read_stub_tail` becomes:

```python
    def read_stub_tail(resolve_src: str | None) -> str:
        # TOOL-dSafePassage-94: no shape runs the last one's bytecode, which the stub's loader writes
        shutil.rmtree(stub92 / "__pycache__", ignore_errors=True)
        if resolve_src is None:
            (stub92 / "upgrade_steps.py").unlink(missing_ok=True)
        else:
            (stub92 / "upgrade_steps.py").write_text("def resolve_kit_dir(home, script, gov):\n    return gov\n\n\n"
                                                     + resolve_src, encoding="utf-8", newline="\n")
            os.utime(stub92 / "upgrade_steps.py", ns=(0, 0))  # one mtime for every stand-in: only size parts two
        return us.run_step_isolated(floor_row, "witness", GOV_ROOT, root92)["tail"]
```

The stub loads its step module with `spec_from_file_location` and `exec_module`
(`python_floor.py:26-30`). That loader writes a cache under `-I`, and it accepts the cache when the
source's whole-second mtime and its size both match. Two writes usually land in one second, but
not always. The pinned mtime makes the size the only difference every time, so S4's probe is red
on every run where the cache is left, not only on most. Measured with the removal cut: S4's check
read `FAIL` in 4 of 6 runs without the pin, and in 9 of 9 with it. The pin moves no `[dSP-92]`
shape, because their bodies differ in size.

### S4: the same-length two-body probe

After the `[dSP-92]` loop (`selftest.py:4517`):

```python
    # TOOL-dSafePassage-94: two stand-ins of one size in a row, so the first's bytecode, if left,
    # would run in place of the second.
    absent94 = 'def resolve_shell_argv(argv):\n    return ["dsp92-absent"] + argv[1:]\n'
    second94 = 'def resolve_shell_argv(argv):\n    raise RuntimeError("dsp94-second")\n'
    read_stub_tail(absent94)
    tail94 = read_stub_tail(second94)
    check("[dSP-94] a stand-in the size of the one before it runs its own source, not that one's bytecode",
          len(second94) == len(absent94) and "dsp94-second" in tail94, repr(tail94[-600:]))
```

Both bodies are 69 characters, measured. The length test sits in the check, so an edit to either
body that breaks the match reads red rather than turning the probe into one that cannot move.
With the cache left, the second run's tail ends in the first body's `FileNotFoundError`, measured.

### Measured

AC1's command, about 3 s a run, in the scratch tree:

| Staged | Lines that read `FAIL` |
|---|---|
| `c86d51fa5` | none, and no `[dSP-94]` line prints |
| `c86d51fa5` with `check_runs`' catch narrowed to `ValueError` | none: `[dSP-91 L2]` reads `ok` |
| S1 to S4 as written | none: two, seven, then one more check after `[dSP-91 L2]` read `ok` |
| S1 to S4, `check_runs`' catch narrowed to `ValueError` | the first `[dSP-94]` only |
| S1 to S4, `steps._BASH = None` cut | the first `[dSP-94]` only |
| S1 to S4, S2's replacement given back `except OSError:` | the second `[dSP-94]` only |
| S1 to S4, the `rmtree` line cut | the third `[dSP-94]` only, in 3 of 3 runs |

A Linux node was not measured. There, `fake87`'s text-file bash fails its spawn with
`ENOEXEC`, which is an `OSError`, so S1 and S2 should read as on Windows. That is not measured.

### Inventory

Minted in `selftest.py`, inside `check_floor_bash`: the function `read_fallback_argv`, the locals
`held`, `e`, `steps94`, `argv94`, `cut94`, `absent94`, `second94` and `tail94`, and the check label
`[dSP-94]`. The module name `dsp94_upgrade_steps` and the message `dsp94-second`. The function reads
`OK` from `lexicon.py --suggest read_fallback_argv --as py.function`: `read` is a declared verb. No
`Refusal` site, flag, conf key, gate leg or receipt field.

### Migration

None.

### Rollout

Live at landing, at order 16.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **The finder's fix for id 1, a `want=False` tail shape.** The skeptic rejected it: that tail is
  byte-identical to the "finds no bash" shape.
- **A needle for a `resolve_bash` frame in `test_floor_fallback`.** On Windows the `subprocess.py`
  frames push that frame out of the 20-line tail, so the needle would not see it.
- **S2 as a check that the staged regression turns `[dSP-91 L2]` red.** Measured: it does not, which
  is id 1 itself.
- **The removal without the pinned mtime.** Measured: S4's probe then reads red in only most runs.
- **id 2's nonce line.** §3 gives the reason.
- **A shared factory for the staged copy, used by S2 and `selftest.py:7734-7736`.** §10 gives the
  reason.

## 5. Production-readiness checklist

- security: no write path, spawn or surface. S2 runs a copy of gov's own module source, staged in
  memory, and S4 runs the stub copy 92 already runs under the scratch root.
- perf / scale: two in-process reads of `resolve_shell_argv`, which spawn each text-file bash once,
  and two more stub runs through `run_step_isolated`, about 0.25 s each on node a. AC1 measured
  about 3 s.
- error / empty / loading states: a read that raises is recorded as a `FAIL` with its repr, not a
  crash of the suite.
- observability: each `[dSP-94]` FAIL carries the read's repr or the tail's last 600 characters.
- risks: S2 runs a second copy of `upgrade_steps.py` in this process. It has its own `Refusal`
  class and `_BASH`, and nothing outside `check_floor_bash` holds it. The `finally` restoring
  `_BASH` is not observed by any check: cut, the cache stays empty and the next resolve walks
  `PATH` again. The pinned mtime is the epoch on a scratch file only.
- testing: §7's three New arms, and AC1 to AC3.
- migration: none.
- user docs: none. No page under `help/` describes the selftest's floor checks.

## 6. Acceptance criteria

- **AC1** — When
  `python -c "import pathlib, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; s.check_floor_bash(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`
  runs from the repository root, it prints `ok   [dSP-87 AC5]` and `ok   [dSP-91 L2]`, then two
  `ok   [dSP-94]` lines, then seven `ok   [dSP-92]` lines, then one `ok   [dSP-94]` line, and its
  last line is `[]`.
  Red when: the read and the probe are absent, so no `[dSP-94]` line prints, as at `c86d51fa5`.
  The `[dSP-87 AC5]`, `[dSP-91 L2]` and seven `[dSP-92]` lines are a preservation check: all nine
  read `ok` at `c86d51fa5` on node a, measured.
  cost: about 3 s, measured with S1 to S4 staged as written.
  fixture: a node whose `PATH` holds a bash, as `[dSP-87 AC5]` already needs.
- **AC2** — When each of four breaks is staged and committed in a scratch tree, AC1's command prints
  `FAIL` for one `[dSP-94]` check and `ok` for every other line. With `check_runs`' `except OSError:`
  in `tools/govkit/upgrade_steps.py` narrowed to `except ValueError:`, the first `[dSP-94]` fails
  naming an `OSError`, and `[dSP-91 L2]` still reads `ok`. With `steps._BASH = None` cut from
  `read_fallback_argv`, the first fails naming the cached bash. With S2's replacement given back
  `except OSError:`, the second fails with `['bash', 'x']`. With the `shutil.rmtree` line cut from
  `read_stub_tail`, the third fails, on every run.
  Red when: a break moves no check, so AC1's command still prints `[]`. At `c86d51fa5` the
  `check_runs` break is staged and every line reads `ok`, which is id 1 (§4 "Measured").
  fixture: each break edits a tracked file, so the build stages it in a scratch tree made by
  `git archive HEAD tools` and committed. It runs AC1's command there and records the FAIL lines.
  The tree holds no such scratch tree today.
- **AC3** — When `git diff --numstat c86d51fa5 -- tools` runs, it prints one line, for the
  selftest file, and its deleted-lines count is `0`. And
  `git grep -n -F 'shutil.rmtree(stub92 / "__pycache__", ignore_errors=True)' -- tools/govkit/selftest.py`
  prints one line, inside `read_stub_tail`.
  Red when: the build edits `test_floor_fallback`, a `[dSP-92]` shape or the `[dSP-91 L2]` check,
  which deletes a line, or edits a second file under `tools/`, or puts the removal outside
  `read_stub_tail`. At `c86d51fa5` the first command prints nothing and the grep prints nothing.
  What it cannot see: a change made by added lines alone. AC1's count of seven `[dSP-92]` lines
  sees an added shape.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the first `[dSP-94]` check of `check_floor_bash`, the fallback read in process, staged red by `check_runs` narrowed to catch `ValueError` and by `steps._BASH = None` cut · none
New arm: tools/govkit/selftest.py · covers AC1 AC2 · the second `[dSP-94]` check, the regression staged in a copy of `upgrade_steps.py`, staged red by its replacement given back `except OSError:` · none
New arm: tools/govkit/selftest.py · covers AC1 AC2 · the third `[dSP-94]` check, the same-length two-body probe, staged red by the `shutil.rmtree` line cut from `read_stub_tail` · none

The four `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for `selftest.py`, read
from `tools/gate-legs.json`. Its other guard, `{prefix}/`, is broad. No refusal call site is added,
so `govkit refusal join`'s pin does not move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-94-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-94-spec-brief.md`.
  It closes the round-5 closing diff review,
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-92-93-closing-diff-round5.md`,
  medium id 1 at the skeptic's corrected fix and low id 2 at its sound fix, each with the review's
  left-shift arm. The pinned mtime refines id 2's probe, and the reason is measured. S1 to S4 and
  each staged break were measured in a scratch tree from `c86d51fa5`.

## 10. Reuse audit

S1 to S4 extend `check_floor_bash` (`tools/govkit/selftest.py:4430`), the one home of the floor
checks, and `read_stub_tail`, its stand-in runner. S1 reads the gov module's own
`resolve_shell_argv` (`tools/govkit/upgrade_steps.py:425`), so it copies no resolution logic. Its
memo save, clear and restore has the shape of the override arm at `selftest.py:18498-18509`, and
S2's staged copy has the shape of `selftest.py:7734-7736`.
`python tools/codebase-map/reuse_lookup.py "read a module's function in process with its memo cleared and restored, and stage a regression in a copy of the module's source"`
ranked generic `read_*` functions by name stem, `read_text` and `read_steps` among them, and no
function that clears a memo or runs a staged copy. So no existing seam fits a factory. The two
precedents are three stdlib lines each, inline in other checks, and this repo's facts name kits as
the kind that owes a factory at its second instance. A shared factory would also edit an unrelated
arm. The recall probe ranked this review's item 1 and TOOL-dGroundRules-35, a spec on the guard
trace reading a bytecode cache as its source, which is another kit's surface.

Recall terms used: `python tools/memory-recall/query.py "a check forgives a spawn crash by its tail and cannot tell which spawn crashed; a rewritten module re-imported reads stale bytecode" --terms "dSP-91 L2 check_floor_bash resolve_shell_argv resolve_bash check_runs _BASH memo in-process mutation pycache bytecode stale read_stub_tail"`
