# TOOL-dSafePassage-92 — the floor stub's fallback check grades a crash, not the word bash, over every host shape the bar runs on

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base 2e6d4845 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-prompt-TOOL-dSafePassage-92-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-92-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-92-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-92-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-92-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-92-spec-brief.md) | research | TOOL-dSafePassage-93 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 closing diff review confirmed a high, id 1. `[dSP-91 L2]` requires its tail to name
`bash`, and on a Windows host with the WSL launcher and no distribution, which includes the hosted
`windows-latest` runner, no tail does. It also confirmed a medium on the same predicate, id 3:
the traceback echoes `python_floor.py:36`, and that echo satisfies the needle. One mechanism closes
both. The check's predicate becomes one function that grades the tail for a crash, the skeptic's
corrected fix for id 3. An arm feeds that function every host shape the bar runs on, so a node
with a distribution still grades the hosts without one. This unit takes id 3, and
TOOL-dSafePassage-93 does not.

## 2. Scope (IN)

- **S1** — ids 1 and 3, one predicate for the fallback. In `check_floor_bash`
  (`tools/govkit/selftest.py:4430`), a nested function `test_floor_fallback(tail)` sits beside
  `test_launcher87` (`:4446`). It returns `True` unless the tail shows a crash, the stub's own early
  exit or the `Refusal`. A crash is a traceback, either its header line or a frame line, whose last line is not
  a `FileNotFoundError` or an `OSError`. The `[dSP-91 L2]` check (`:4464-4467`) calls it on the
  witness's tail, in place of its inline needle. The check's comment (`:4457-4461`) and the
  function's docstring name the predicate. §4 "S1". Observed by AC1, AC2 and AC3.
- **S2** — id 1's left-shift gate, an arm over every host shape. After `[dSP-91 L2]`, five
  `[dSP-92]` checks run `test_floor_fallback` on five tails. Two are literal: the launcher's
  no-distribution text in UTF-16, decoded as `run_step_isolated` decodes it, and the empty tail left
  when that text goes to stdout. Three are real runs of a copy of `tools/govkit/steps/python_floor.py`,
  each beside a stand-in step module: a spawn that finds no program, a raise on `:36`, and a raise
  eight frames deeper. The first three must read as the fallback and the last two as a crash. §4 "S2".
  Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Ids 2 and 4 of the review. TOOL-dSafePassage-93 takes them.
- id 1's literal fix: the NUL strip and a third positive needle for the launcher's text. §4
  "Alternatives rejected" gives the measurement.
- A fake System32 directory on `PATH`, the review's first way to stage id 1's case. The Windows loader
  finds the System32 launcher before it searches `PATH` (`tools/govkit/upgrade_steps.py:372-376`).
  Spec 91 measured this: with its fake `bash.exe` first on `PATH`, node a ran the WSL launcher.
- Running the check on the hosted runner. The held job (`.github/workflows/remote-ci.yml:313`) runs
  at the bar, and its comment says it blocks nothing (`:15`). S2's literal tails measure that host's
  shapes on every node.
- Asserting an rc, for the reason spec 91 §3 gives.
- Permanent shapes for the stub's early exit and the `Refusal`. Spec 91's AC6 staged both, and
  `[dSP-91 L2]` keeps both exclusions.
- The checklist entries the review's left-shift notes name. The review records that no checklist is
  present, and this unit's arm is the gate.

### Edges

- **hands-off** `TOOL-dSafePassage-93` — the review's id 2, a hard-link `[dSP-90]` sibling, and
  id 4, the narrowed `set_environ` claim. That unit builds after this one, in the same file.

## 4. Design

Every cited line holds at `2e6d48453`, the build head with TOOL-dSafePassage-90 and -91 landed. Each
measurement was taken on 2026-11-01 on node a, Python 3.15.2, in a scratch tree made by
`git archive 2e6d48453 tools` and committed, with S1 and S2 staged as written below.

### Why the needle cannot work

When `GOV_BASH` is unset and no bash resolves, `resolve_shell_argv` hands the stub the bare argv
(`upgrade_steps.py:437-440`). What runs it is the node's. The witness's tail is the last 20 lines of
stderr (`:1798`), decoded as UTF-8 with `errors="replace"` (`:1795`). Five tails are possible, and
three of them defeat a needle. A launcher answering in UTF-16 leaves a NUL between every character.
A launcher answering on stdout leaves the tail empty. A spawn that finds no program, on Windows,
fills the tail with `subprocess.py` frames: the measured tail has neither its `Traceback` header nor
the echo of `:36`, and its last line, `FileNotFoundError: [WinError 2] ...`, names no program. A raise
on `:36` does the reverse, because the traceback echoes `:36`, and that line holds `"bash"`.

### S1: the predicate

At `selftest.py:4457-4467`, after `path87` (`:4451`) and the `[dSP-87 AC5]` check:

```python
    def test_floor_fallback(tail: str) -> bool:
        # TOOL-dSafePassage-92: the stub reached its spawn unless the tail shows a crash, its own early
        # exit or the Refusal. A crash is a traceback, its header or a frame line, whose last line is not
        # a failed spawn. The word bash is never required: the WSL launcher with no distribution answers
        # in UTF-16 or on stdout, and a failed spawn's frames fill the 20-line tail on Windows.
        last = next((ln for ln in reversed(tail.splitlines()) if ln.strip()), "")
        crashed = ("Traceback" in tail or 'File "' in tail) and not last.startswith(("FileNotFoundError", "OSError"))
        return not crashed and not any(s in tail for s in ("python_floor.py:", "upgrade_steps.Refusal", "Set GOV_BASH"))

    # TOOL-dSafePassage-91: the same PATH with GOV_BASH unset, so no bash resolves and the stub falls
    # back to bare `bash` (python_floor.py:36) rather than dying on resolve_bash's Refusal. What bare
    # `bash` resolves to (on Windows the loader's System32 WSL launcher, elsewhere PATH or nothing), and
    # so the rc, is the node's, so only the tail is graded, by `test_floor_fallback`.
    with set_environ({"PATH": path87, "GOV_BASH": None, "GOV_PYTHON": sys.executable}):
        got = us.run_step_isolated(floor_row, "witness", GOV_ROOT, GOV_ROOT)
    check("[dSP-91 L2] the floor row's witness, no bash resolving and GOV_BASH unset, falls back to bare bash",
          test_floor_fallback(got["tail"]), str(got))
```

The docstring (`:4431-4433`) ends:

```python
    floor stub reaches its fallback to bare `bash`, its tail graded by `test_floor_fallback`, which
    TOOL-dSafePassage-92 grades over every host shape the bar runs on. Called from `check_step_isolation`."""
```

The frame marker `File "` is the measured part of the skeptic's correction. The correction says a
crash is a tail holding `Traceback`. A raise eight frames below `:36` leaves 29 lines on stderr, so
its 20-line tail has no `Traceback` line, and the header alone reads it as the fallback. Every frame
line starts `  File "`, and Python 3.15 cuts a multi-line frame short with `...<n lines>...`. So
every 20-line traceback tail measured here holds a frame line. That is measured on 3.15 only. `FileNotFoundError` and `OSError` are the two spawn failures the
skeptic names. A `PATH` bash that is a text file, as `fake87` is, raises `OSError`, and a missing
program raises `FileNotFoundError`.

### S2: the host-shape arm

After the `[dSP-91 L2]` check. `shutil` is imported at `selftest.py:27`, and `HERE` is the engine
directory (`:68`), so the copy is the stub this engine ships at every prefix:

```python
    # TOOL-dSafePassage-92: the same predicate over every host shape the bar runs on, so a node with a
    # WSL distribution still grades the hosts without one. The three tracebacks are the real stub's, run
    # from a copy beside a stand-in step module whose resolve_shell_argv fails as each shape needs.
    stub92 = tmp / "dsp92" / "govkit"
    (stub92 / "steps").mkdir(parents=True, exist_ok=True)
    shutil.copy2(HERE / "steps" / "python_floor.py", stub92 / "steps" / "python_floor.py")

    def read_stub_tail(resolve_src: str) -> str:
        (stub92 / "upgrade_steps.py").write_text("def resolve_kit_dir(home, script, gov):\n    return gov\n\n\n"
                                                 + resolve_src, encoding="utf-8", newline="\n")
        p = subprocess.run([sys.executable, str(stub92 / "steps" / "python_floor.py"), "floor"],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        return "\n".join(p.stderr.splitlines()[-20:])  # the witness's tail, as run_step_isolated takes it

    wsl92 = "Windows Subsystem for Linux has no installed distributions.\r\n"
    for what, tail92, want in (
            ("the WSL launcher's no-distribution text in UTF-16", wsl92.encode("utf-16-le").decode("utf-8", "replace"), True),
            ("that text on stdout, so the tail is empty", "", True),
            ("a spawn that finds no bash", read_stub_tail(
                'def resolve_shell_argv(argv):\n    return ["dsp92-absent"] + argv[1:]\n'), True),
            ("a raise on python_floor.py:36, which the traceback echoes", read_stub_tail(
                'def resolve_shell_argv(argv):\n    raise RuntimeError("none")\n'), False),
            ("a raise deep enough to push the Traceback line out of the tail", read_stub_tail(
                'def resolve0():\n    raise RuntimeError("none")\n'
                + "".join(f"def resolve{i}():\n    return resolve{i - 1}()\n" for i in range(1, 9))
                + 'def resolve_shell_argv(argv):\n    return [resolve8()] + argv[1:]\n'), False)):
        check(f"[dSP-92] the fallback predicate reads {what} as {'the fallback' if want else 'a crash'}",
              test_floor_fallback(tail92) is want, repr(tail92[-600:]))
```

The launcher's text is the census's (`memory/builds/aMendedFleet/build/2026-10-04-build-TOOL-aMendedFleet-7-1-held-red-census.md:39`).
The predicate reads no word of it, so its exact wording does not matter. The stub loads its step
module from `parents[1]` (`python_floor.py:26`), so the copy loads the stand-in. The stand-in's
`resolve_kit_dir` answers the gov root, and the stub's `:32` reads no kit. The chain of eight
distinct functions is deliberate: a recursive raise is folded to `[Previous line repeated ...]`,
measured, and its tail keeps the `Traceback` header. The arm reads the stub as it ships, so a stub
edited away from `steps.resolve_shell_argv` is seen there too.

### Measured

The 91 predicate and `test_floor_fallback` over the five tails:

| Shape | Must read | 91 predicate | `test_floor_fallback` |
|---|---|---|---|
| the launcher's text in UTF-16 | fallback | crash | fallback |
| the empty tail | fallback | crash | fallback |
| a spawn that finds no program | fallback | crash | fallback |
| a raise on `:36` | crash | fallback | crash |
| a raise eight frames deeper | crash | crash | crash |

AC1's command, about 1.5 s a run, at `2e6d48453` and staged:

| Staged | Lines |
|---|---|
| `2e6d48453` | `ok   [dSP-87 AC5] ...`, `ok   [dSP-91 L2] ...`, `[]` |
| S1 and S2 as written | the same two, five `ok   [dSP-92] ...` lines, `[]` |
| the return given back 91's `("bash" in tail or "python-floor.sh" in tail) and` | `FAIL [dSP-92]` for the UTF-16, empty and spawn shapes |
| `crashed = False` | `FAIL [dSP-92]` for the two raise shapes |
| the frame marker cut, so `"Traceback" in tail` alone | `FAIL [dSP-92]` for the deep raise only |
| `python_floor.py:36` as `[steps.resolve_bash(), (kit / FLOOR_SCRIPT).as_posix(), *argv]` | `FAIL [dSP-91 L2]` with `upgrade_steps.Refusal` in its tail, and `FAIL [dSP-92]` for the spawn shape, whose stand-in has no `resolve_bash` |
| `python_floor.py:32` resolving `"no-such-floor.sh"` | `FAIL [dSP-87 AC5]` and `FAIL [dSP-91 L2]`, each tail `python_floor.py: no lib kit holding no-such-floor.sh ...` |

On node a the real `[dSP-91 L2]` tail is the WSL launcher's `No such file or directory` for the
floor script, which reads `ok` under both predicates. A Linux node was not measured. There, the
spawn shape's shorter traceback may keep the echo of `:36`, so the first staged break may read that
shape `ok`. The UTF-16 and empty shapes still read `FAIL`.

### Inventory

Minted in `selftest.py`, inside `check_floor_bash`: the functions `test_floor_fallback` and
`read_stub_tail`, the locals `last`, `crashed`, `stub92`, `wsl92`, `what`, `tail92`, `want` and
`p`, and the check label `[dSP-92]`. The scratch directory `dsp92` and the stand-in names
`dsp92-absent` and `resolve0` to `resolve8`. Both functions read `OK` from
`lexicon.py --suggest <name> --as py.function`: `test` and `read` are declared verbs. The local
`tail` that 91 minted at `:4464` is not kept. No `Refusal` site, flag, conf key, gate leg or
receipt field.

### Migration

None.

### Rollout

Live at landing, at order 16, before TOOL-dSafePassage-93.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **id 1's fix as the finder wrote it.** That fix strips NULs and adds the launcher's text as a
  third needle. It still reads the empty tail and the spawn shape as a crash, as the table shows,
  and the review itself names the stdout case. id 3's corrected fix has no needle left for the
  strip to serve.
- **id 3's correction with the `Traceback` header alone.** Measured: it reads the deep raise as the
  fallback.
- **Typed traceback strings in the arm.** A typed copy can see neither the stub's `:36` nor a change
  in Python's traceback layout. The real stub costs about 0.1 s a shape.
- **`test_floor_fallback` at module level.** Its one caller is `check_floor_bash`, and AC1 reaches
  it through that function, as spec 91's AC5 does.

## 5. Production-readiness checklist

- security: no write path, spawn or surface. The arm runs the stub copy under the scratch root.
- perf / scale: three spawns of the stub, about 0.2 s together on node a.
- error / empty / loading states: an empty tail reads as the fallback by design, because it is the
  launcher on stdout. A crash, the early exit and the `Refusal` read red.
- observability: each `[dSP-92]` FAIL carries the tail's last 600 characters.
- risks: the predicate no longer requires evidence that the stub spawned. A stub that returned
  without spawning and wrote nothing would read `ok`. The skeptic's correction accepts that, and
  the early exit, the stub's one non-spawning return, stays a named red.
- testing: §7's two New arms, and AC1 to AC3.
- migration: none.
- user docs: none. No page under `help/` describes the selftest's floor checks.

## 6. Acceptance criteria

- **AC1** — When
  `python -c "import pathlib, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; s.check_floor_bash(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`
  runs from the repository root, it prints `ok   [dSP-87 AC5]`, `ok   [dSP-91 L2]`, then five
  `ok   [dSP-92]` lines, and its last line is `[]`.
  Red when: the arm is absent, so no `[dSP-92]` line prints, as at `2e6d48453`. The `[dSP-87 AC5]`
  and `[dSP-91 L2]` lines are a preservation check: both read `ok` at `2e6d48453` on node a.
  cost: about 1.5 s, measured at rev-1.
  fixture: a node whose `PATH` holds a bash, as `[dSP-87 AC5]` already needs.
- **AC2** — When each of three breaks is staged in `test_floor_fallback` and committed in a scratch
  tree, AC1's command prints `FAIL [dSP-92]` for the shapes §4 "Measured" names. With the return given
  back 91's `"bash" in tail` needle, the UTF-16 and empty shapes fail. With `crashed = False`, both
  raise shapes fail. With the frame marker `'File "' in tail` cut, the deep raise fails.
  Red when: a shape no break moves, so a staged break reads all five `ok`. At `2e6d48453` there is no
  `test_floor_fallback` to stage, and 91's predicate reads the first three shapes as a crash and the
  raise on `:36` as the fallback (§4 "Measured").
  fixture: each stage edits a tracked file, so the build stages it in a scratch tree made by
  `git archive HEAD tools` and committed. It runs AC1's direct `check_floor_bash` call there and
  records the FAIL lines. The tree holds no such scratch tree today.
- **AC3** — When `git grep -n -F "test_floor_fallback(" -- tools/govkit/selftest.py` runs, it prints
  three lines inside `check_floor_bash`: the `def`, the `[dSP-91 L2]` call and the `[dSP-92]` call.
  And `git grep -n -F '"bash" in tail' -- tools/govkit/selftest.py` prints nothing.
  Red when: `[dSP-91 L2]` keeps its inline needle, so the first grep prints nothing and the second
  prints `:4466`, as at `2e6d48453`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the five `[dSP-92]` checks of `check_floor_bash`, staged red by `test_floor_fallback` given back 91's bash needle, by `crashed = False`, and by the frame marker cut · none
New arm: tools/govkit/selftest.py · covers AC1 · the `[dSP-91 L2]` check, now graded by `test_floor_fallback`, staged red by `python_floor.py:36` calling `steps.resolve_bash()` directly and by `:32` resolving a script no lib kit holds · none

The four `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for `selftest.py`. Its
other guard, `{prefix}/`, is broad. No refusal call site is added, so `govkit refusal join`'s pin
does not move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-92-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-92-spec-brief.md`.
  It closes the round-4 closing diff review,
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-90-91-closing-diff-round4.md`,
  high id 1 and medium id 3, with one predicate at id 3's corrected fix. The frame marker refines
  that fix, and the reason is measured. Ids 2 and 4 are TOOL-dSafePassage-93's. S1 and S2 and each
  staged break were measured in a scratch tree from `2e6d48453`.

## 10. Reuse audit

S1 extends `check_floor_bash` (`tools/govkit/selftest.py:4430`), the one home of the floor checks,
and puts its predicate beside that function's `test_launcher87`. S2 runs the shipped stub
`tools/govkit/steps/python_floor.py` from a copy, and decodes and cuts its tail as
`run_step_isolated` does (`tools/govkit/upgrade_steps.py:1795`, `:1798`). It types no traceback.
`python tools/codebase-map/reuse_lookup.py "grade a child process's stderr tail for a crash rather than for a word, across every host shape"`
ranked `read_stderr_tail` (`tools/unattended/unattended.sh`), a shell function of another kit that
reads a tail and grades none. So no existing seam fits the predicate itself, and it lives in the
one function that reads this tail. The recall probe ranked TOOL-aMendedFleet-98, whose evidence
records the launcher's UTF-16 answer, and this review's item 1.

Recall terms used: `python tools/memory-recall/query.py "a check greps a child's stderr for the word bash and goes red falsely where the WSL launcher has no distribution" --terms "dSP-91 L2 check_floor_bash python_floor resolve_shell_argv WSL launcher distribution UTF-16 traceback tail fallback"`
