# TOOL-dSafePassage-95 — the round-6 closing review's nine minors: the floor-bash arms of 94 made self-consistent

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base 0e596709 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-prompt-TOOL-dSafePassage-95-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-95-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-95-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-95-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-95-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-95-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-6 closing diff review of TOOL-dSafePassage-94 confirmed nine items, two medium and seven
low. They all sit in the `check_floor_bash` arms 94 added. The medium that matters most is item 1.
The stand-in's path is spelled `stub92 / "upgrade_steps.py"`, and the suite's own `[dSP-71] AC4`
guard reads that as a hand-picked copy of the engine, so the `govkit selftest` leg is red. This unit
makes those arms agree with the suite's guard and with their own claims. Each item closes at the
fix the review's skeptic judged sound, and item 8 closes at the skeptic's corrected fix.

## 2. Scope (IN)

- **S1** — item 1, the stand-in held in one name. After `stub92` (`tools/govkit/selftest.py:4511`),
  `stand94 = stub92.joinpath("upgrade_steps.py")`. The unlink at `:4523`, the `write_text` at
  `:4525` and the `os.utime` at `:4527` use `stand94`. No line, comments included, joins a bare
  name to the engine's file name in the guarded shape. This is the review's first fix. §4 "S1"
  says why the other one is not used. Observed by AC2 and AC3.
- **S2** — items 2 and 8, the pin and the cache precondition observed. The probe at `:4548-4555`
  captures `pyc94` after `read_stub_tail(absent94)` and before the second call. After the second
  call it captures `mtime94 = os.stat(stand94).st_mtime_ns`. The third `[dSP-94]` check's condition
  gains `pyc94` and `mtime94 == 0`, and its detail names both. `read_stub_tail` itself asserts
  nothing. Observed by AC1 and AC4.
- **S3** — item 4, the restore observed. After the `[dSP-91 L2]` block's two `[dSP-94]` checks
  (`:4500-4503`), a `[dSP-95]` check asserts `us._BASH == bash87`. Observed by AC1 and AC4.
- **S4** — items 5 and 7, the narrowed copy staged by the suite's seam and guarded.
  `steps94` (`:4485-4489`) is staged by `build_staged_copy` (`:3640`) and loaded by
  `spec_from_file_location` and `exec_module`, in the shape of `[dSP-87 AC6]` (`:3176-3185`). The
  build and the load sit in a `try`. A copy that does not load records a `[dSP-95]` FAIL with its
  repr. In `read_fallback_argv`, the memo read (`:4474`) sits in its own `try` and returns an
  `AttributeError`. Observed by AC4.
- **S5** — item 6, the anchor counted. `src94` and `anchor94` name the source and the anchor.
  The replace passes a count of 1. The second `[dSP-94]` check's condition gains
  `src94.count(anchor94) == 1`, and its detail names the count. Observed by AC1 and AC4.
- **S6** — items 3 and 9, and the spec-text halves of items 4, 5 and 7. 94 is CLOSED and is not
  edited. §4 "Corrections to 94's text" carries each correction, and AC3 and AC4 carry the two
  criteria item 3 asks for. Observed by AC3.

## 3. Non-goals (OUT)

- The review's other fix for item 1, narrowing `read_handpicked_copies` to skip a stand-in. That is
  a change to a second arm's predicate, with its own planted cases. §4 "S1" gives the reason.
- Widening `read_handpicked_copies` to see `joinpath` or an in-memory `exec(compile(`, as item 7's
  left-shift note proposes. S4 removes the one in-memory engine staging, so nothing in the tree
  needs it now.
- The review's checklist entries and its spec-citation checker. The review records that no
  checklist is present, so the main loop owns those entries.
- Any edit to `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md`.
- Any change to `test_floor_fallback`, the seven `[dSP-92]` shapes or `check_staged_copies`.
- Product code. `tools/govkit/upgrade_steps.py` and `tools/govkit/steps/python_floor.py` are read
  and not edited.

### Edges

none

## 4. Design

Every cited line holds at `0e5967090`. `tools/` there is byte-identical to 94's build commit
`638be1f8b`. The measurements were taken on 2026-11-01 on node a, Windows, Python 3.15.2. They ran
in a scratch tree made by `git archive 0e5967090 tools` and committed with `core.longpaths` set,
because one fixture path is longer than Windows allows. The fenced text below was staged into that
tree as written. AC1's command was then run green and under each break in "Measured".

### S1: one name for the stand-in

`read_handpicked_copies` (`selftest.py:3652-3660`) flags every line outside `build_staged_copy`
that joins a bare local name other than `HERE` to `"upgrade_steps.py"`. At the base it returns
`([4523, 4525, 4527], 1)`, measured in process. So both `[dSP-71] AC4` checks read FAIL, the first
at `:3670-3672` and the planted one at `:3673-3676`. The planted check fails because its `named`
list carries those three lines ahead of the planted line. The review names only the first, and one
fix closes both.

```python
    stub92 = root92 / "govkit"
    stand94 = stub92.joinpath("upgrade_steps.py")  # TOOL-dSafePassage-95: the stand-in, one name
```

```python
    def read_stub_tail(resolve_src: str | None) -> str:
        # TOOL-dSafePassage-94: no shape runs the last one's bytecode, which the stub's loader writes
        shutil.rmtree(stub92 / "__pycache__", ignore_errors=True)
        if resolve_src is None:
            stand94.unlink(missing_ok=True)
        else:
            stand94.write_text("def resolve_kit_dir(home, script, gov):\n    return gov\n\n\n"
                               + resolve_src, encoding="utf-8", newline="\n")
            os.utime(stand94, ns=(0, 0))  # one mtime for every stand-in: only size parts two
        return us.run_step_isolated(floor_row, "witness", GOV_ROOT, root92)["tail"]
```

After the edit the guard returns `([], 1)`, measured over the staged file. This fix works because
`joinpath` is in the guard's declared blind spot (`selftest.py:3666`). The fix is sound because the
stand-in is not a copy of the engine. It is a two-function module that the floor stub loads from
beside itself (`python_floor.py:26-30`), and the copy-hygiene class the guard owns does not include
it. The guard's other fix would edit the predicate of a second arm, which is a second mechanism.

### S2: the pin and the bytecode precondition in the third check

```python
    read_stub_tail(absent94)
    pyc94 = any((stub92 / "__pycache__").glob("upgrade_steps.*.pyc"))  # TOOL-dSafePassage-95: the red's precondition
    tail94 = read_stub_tail(second94)
    mtime94 = os.stat(stand94).st_mtime_ns
    check("[dSP-94] a stand-in the size of the one before it runs its own source, not that one's bytecode",
          len(second94) == len(absent94) and pyc94 and mtime94 == 0 and "dsp94-second" in tail94,
          f"pyc {pyc94}; mtime_ns {mtime94}; tail {tail94[-600:]!r}")
```

On node a an mtime pinned to `ns=(0, 0)` reads back as `st_mtime_ns == 0`, measured. `pyc94` sits
in the check and not in `read_stub_tail`. A bare `assert` there would crash the suite and is
stripped under `-O`. A `check()` there would print on each of its nine calls. That is the skeptic's
correction on id 21.

### S3 and S5: the restore and the anchor count

```python
    check("[dSP-94] the same read, check_runs narrowed to catch ValueError, reads the spawn's OSError",
          src94.count(anchor94) == 1 and isinstance(cut94, OSError), f"anchor count {src94.count(anchor94)}; {cut94!r}")
    check("[dSP-95] the read gives the parent's bash cache back", us._BASH == bash87, repr(us._BASH))
```

`bash87 = us.resolve_bash()` (`selftest.py:4440`) fills the memo, and `resolve_bash` returns it
first (`upgrade_steps.py:393-394`). With the `finally` cut, the memo stays `None`, because the
Refusal at `:421` assigns nothing. With the restore in place the check reads `ok`, measured, so
nothing between `:4440` and the check moves the memo on node a.

### S4: the copy staged by `build_staged_copy`

`steps94` at `:4485-4489` becomes:

```python
    # TOOL-dSafePassage-95: staged by build_staged_copy, its anchor replaced once, and a copy that
    # does not load is a labelled FAIL rather than a crash of the suite.
    src94 = (HERE / "upgrade_steps.py").read_text(encoding="utf-8")
    anchor94 = "returncode == 0\n        except OSError:"
    steps94 = types.ModuleType("dsp94_upgrade_steps")
    try:
        spec94 = importlib.util.spec_from_file_location("dsp94_upgrade_steps", build_staged_copy(
            tmp / "dsp94-narrowed", src94.replace(anchor94, "returncode == 0\n        except ValueError:", 1)))
        steps94 = importlib.util.module_from_spec(spec94)
        spec94.loader.exec_module(steps94)
    except Exception as e:  # noqa: BLE001 - a copy that does not load is what this records
        check("[dSP-95] the staged copy of upgrade_steps.py loads", False, repr(e))
```

In `read_fallback_argv`, the memo read at `:4474` becomes:

```python
        try:
            held = steps._BASH
        except AttributeError as e:  # TOOL-dSafePassage-95: a copy that did not load has no memo
            return e
```

A copy that fails to compile or exec leaves `steps94` without `_BASH`. The read then returns the
`AttributeError`, and the second `[dSP-94]` check records it as a FAIL. `tmp` is fresh per run, and
no other arm in the suite stages to `dsp94-narrowed`, so `copytree` cannot collide.

### Corrections to 94's text

94 is CLOSED and frozen. Each row is the reading that holds at `0e5967090`.

| Item | 94 says, at | Correct reading | Carried by |
|---|---|---|---|
| 9 | S1, line 37: `test_floor_fallback` (`:4458-4467`) | `:4458-4468`: the `return` is at 4468 | this row |
| 4 | S1, line 38: S1 "Observed by AC1, AC2 and AC3" | the `finally` was not observed at 94; §5 risks at lines 271-273 said so | S3 |
| 5 | §5, lines 267-268: a read that raises is a FAIL, not a crash | true only for the `resolve_shell_argv` call; the staging and the memo read were unguarded | S4 |
| 7 | §4, lines 160-161, and §10, line 345: the copy follows `selftest.py:7734-7736` | that site, now `:7772-7774`, stages `govkit.py`; the engine's seam is `build_staged_copy` | S4, §10 |
| 3 | AC3, lines 302-305: greps only the `rmtree` line | the `os.utime` line has its own grep | AC3 |
| 3 | lines 188 and 222, and AC2 at line 296: 9 of 9, 3 of 3, "every run" | one figure at a fixed N, stated in AC4 | AC4 |

### Measured

AC1's command, about 3 s a run, in the scratch tree with S1 to S5 staged. Each row is one break,
staged and committed, and names the lines that read FAIL. Every other line read `ok`.

| Break | Runs | Lines that read `FAIL` |
|---|---|---|
| none | 1 | none, and the guard's two `[dSP-71] AC4` checks read `ok` |
| `check_runs`' anchor in `upgrade_steps.py` narrowed once to `ValueError` | 1 | the first and second `[dSP-94]`, the second naming `anchor count 0`; `[dSP-91 L2]` reads `ok` |
| `steps._BASH = None` cut | 1 | the first `[dSP-94]` |
| S4's replacement given back `except OSError:` | 1 | the second `[dSP-94]`, naming `anchor count 1` |
| the `finally` cut | 1 | `[dSP-95] the read gives the parent's bash cache back` |
| S4's replacement loses its colon, so the copy does not compile | 1 | `[dSP-95] the staged copy ... loads` and the second `[dSP-94]`; all twelve other lines print |
| that break with S4's memo guard also cut | 1 | `[dSP-95] the staged copy ... loads`, then an `AttributeError` traceback ends the run |
| a second anchor appended to `src94` | 1 | the second `[dSP-94]`, naming `anchor count 2` |
| `__pycache__` removed between the probe's first read and `pyc94` | 1 | the third `[dSP-94]`, naming `pyc False` |
| the `shutil.rmtree` line cut | 6 | the third `[dSP-94]`, naming `pyc True; mtime_ns 0` |
| the `os.utime` line cut | 6 | the third `[dSP-94]`, naming a non-zero `mtime_ns` |

At 94 the `check_runs` break failed only the first check. It now fails the second as well, because
the narrowed text leaves the anchor at zero. A Linux node was not measured.

### Inventory

Minted in `selftest.py`, inside `check_floor_bash`: the locals `stand94`, `pyc94`, `mtime94`,
`src94`, `anchor94` and `spec94`, and the check label `[dSP-95]` with its two checks. No function,
constant, type or file is minted, so the naming lexicon grades nothing new. No `Refusal` site, flag,
conf key, gate leg or receipt field.

### Migration

None.

### Rollout

Live at landing, at order 16.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **Narrowing `read_handpicked_copies` for item 1.** §4 "S1" gives the reason.
- **The pin as its own `[dSP-94]` check.** The review allows it. Folding it into the third check
  keeps the probe to one line and puts the pin beside the red it makes certain.
- **The finder's fix for item 8, an assertion inside `read_stub_tail`.** The skeptic rejected it,
  and §4 "S2" gives the reason.
- **Rewording 94's S1 instead of adding S3's check.** It would leave the restore unobserved.

## 5. Production-readiness checklist

- security: no write path, spawn or surface. S4 stages a copy of gov's own kit under the scratch
  root, as `[dSP-87 AC6]` does.
- perf / scale: one `copytree` of the kit directory. AC1 measured about 3 s, the same as at 94.
- error / empty / loading states: a copy that does not load and a module with no memo are each a
  labelled FAIL. Measured in "Measured".
- observability: the second and third checks' details name the anchor count, `pyc94` and the mtime.
- risks: S1 depends on `joinpath` being in the guard's declared blind spot. A later widening of
  `read_handpicked_copies` to see `joinpath` would flag `stand94`, and that would be a loud red.
  `pyc94` turns the third check red on a node whose stub writes no bytecode. The review's skeptics
  on ids 6 and 34 found no such node.
- testing: §7's New arms, and AC1 to AC4.
- migration: none.
- user docs: none. No page under `help/` describes the selftest's floor checks.

## 6. Acceptance criteria

- **AC1** — When
  `python -c "import pathlib, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; s.check_floor_bash(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`
  runs from the repository root, it prints `ok   [dSP-87 AC5]`, `ok   [dSP-91 L2]`, two
  `ok   [dSP-94]` lines, then `ok   [dSP-95] the read gives the parent's bash cache back`, then
  seven `ok   [dSP-92]` lines and one `ok   [dSP-94]` line, and its last line is `[]`.
  Red when: the restore check is absent, so the two `[dSP-94]` lines run straight into the
  `[dSP-92]` lines, as at `0e5967090`, measured. The other twelve lines are a preservation check:
  all read `ok` at `0e5967090` on node a, measured.
  cost: about 3 s, measured.
  fixture: a node whose `PATH` holds a bash, as `[dSP-87 AC5]` already needs.
- **AC2** — When
  `python -c "import pathlib, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; print(s.read_handpicked_copies((s.HERE / 'selftest.py').read_text(encoding='utf-8'))); s.check_staged_copies(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`
  runs from the repository root, it prints `([], 1)`, then `ok` for both `[dSP-71] AC4` lines and
  for `[dSP-71] AC3`, and its last line is `[]`.
  Red when: the stand-in is spelled in the `<name> / "upgrade_steps.py"` shape. At `0e5967090` it
  prints `([4523, 4525, 4527], 1)`, and both `[dSP-71] AC4` lines read FAIL, the first naming
  `outside: [4523, 4525, 4527]`, measured. The `[dSP-71] AC3` line is a preservation check: it reads
  `ok` at `0e5967090`, measured.
- **AC3** — When
  `git grep -n -F 'os.utime(stand94, ns=(0, 0))' -- tools/govkit/selftest.py` runs, it prints one
  line, inside `read_stub_tail` and after its `stand94.write_text` line. And
  `git grep -n -F 'stub92 / "upgrade_steps.py"' -- tools/govkit/selftest.py` prints nothing. And
  `git diff --numstat 0e5967090 -- tools memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-94.md`
  prints one line, for the selftest file.
  Red when: the pin is dropped or spelled in the old shape, a stand-in use is missed, or the build
  edits 94's spec or a second file under the tools directory. At `0e5967090` the first grep prints nothing and
  the second prints lines 4523, 4525 and 4527, measured.
- **AC4** — When each break in §4 "Measured" is staged and committed in a scratch tree made by
  `git archive HEAD tools`, AC1's command prints `FAIL` for the lines that row names and `ok` for
  every other line. The `shutil.rmtree` break and the `os.utime` break each run N = 6 times and fail
  in all 6.
  Red when: a break moves no check, so AC1's command still prints `[]`. At `0e5967090` the
  `os.utime` cut and the `finally` cut both move no check, per the review's probes on ids 24, 30, 2
  and 26.
  figure: N = 6 and 6 of 6 are PINNED, measured on 2026-11-01 on node a. This is the one place the
  rate is stated.
  cost: about 3 s a run, 21 runs.
  fixture: on Windows the scratch commit needs `core.longpaths` set. The tree holds no such scratch
  tree today.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 · `[dSP-71] AC4` in `check_staged_copies`, red at `0e5967090` on lines 4523, 4525 and 4527 and green once S1 lands · none
New arm: tools/govkit/selftest.py · covers AC1 AC4 · `[dSP-95] the read gives the parent's bash cache back`, staged red by the `finally` cut · none
New arm: tools/govkit/selftest.py · covers AC4 · `[dSP-95] the staged copy of upgrade_steps.py loads`, which prints only when it fails, staged red by S4's replacement losing its colon · none
New arm: tools/govkit/selftest.py · covers AC1 AC4 · the second `[dSP-94]` check with the anchor count, staged red by a second anchor appended to `src94` · none
New arm: tools/govkit/selftest.py · covers AC1 AC4 · the third `[dSP-94]` check with `pyc94` and the pinned mtime, staged red by the `os.utime` cut, the `shutil.rmtree` cut and the cache removed before `pyc94` · none

The four `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for `selftest.py`, read
from `tools/gate-legs.json`. No refusal call site is added, so `govkit refusal join`'s pin does not
move. The first New arm is item 1's left-shift: the closing run records the `govkit selftest` leg
going from red to green.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-95-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-95-spec-brief.md`.
  It closes the round-6 closing diff review,
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-94-closing-diff-round6.md`:
  items 1 to 7 and 9 at the skeptic's sound fix, and item 8 at its corrected fix. S1 to S5 and each
  break were measured in a scratch tree from `0e5967090`.

## 10. Reuse audit

S1 to S5 extend `check_floor_bash` (`tools/govkit/selftest.py:4430`) and `read_stub_tail`, the
arms 94 added. S4 moves the narrowed copy onto the suite's existing seam for staging the engine,
`build_staged_copy` (`selftest.py:3640-3649`). The suite calls it on 23 lines at `0e5967090`, by
`grep`, and the `[dSP-87 AC6]`
arm (`:3176-3185`) shows the in-process load shape S4 copies. That seam was found by reading the
suite. `python tools/codebase-map/reuse_lookup.py "stage a copy of the engine module with one anchor replaced once and load it in process"`
ranked generic `load*` functions by name stem and did not name `build_staged_copy`, which is
private to the suite. The recall probe named no prior decision on a stand-in path, a pinned mtime
or a memo restore. It ranked only this review and its briefs.

Recall terms used: `python tools/memory-recall/query.py "a staged engine copy guard names a stand-in path; a pinned mtime nothing observes" --terms "dSP-71 AC4 read_handpicked_copies build_staged_copy stand-in read_stub_tail os.utime st_mtime_ns pycache _BASH finally anchor count"`
