# TOOL-dSafePassage-96 — the round-7 closing review's three minors: each restore check reads the path its label names, and a reused tmp stages afresh

**Status:** CLOSED · rev-1 · 2026-11-01 · node a · Tier-2 · base 744d2551 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dSafePassage-96-ledger.md](../build/2026-11-01-build-TOOL-dSafePassage-96-ledger.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-96-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-96-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-96-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-96-build-brief.md) | journal | — |
| [2026-11-01-prompt-TOOL-dSafePassage-96-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dSafePassage-96-spec-brief.md) | research | — |
| [2026-11-01-review-TOOL-dSafePassage-96-closing-diff-round8.md](../reviews/2026-11-01-review-TOOL-dSafePassage-96-closing-diff-round8.md) | diff-review | — |
| [2026-11-01-review-TOOL-dSafePassage-96-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dSafePassage-96-spec-audit-round1.md) | spec-audit | — |
| [2026-11-01-review-TOOL-dSafePassage-97-closing-diff-round9.md](../reviews/2026-11-01-review-TOOL-dSafePassage-97-closing-diff-round9.md) | diff-review | TOOL-dSafePassage-97 |

<!-- /gen:spec-records -->

## 1. Goal

The round-7 closing diff review of TOOL-dSafePassage-95 confirmed three items, one medium and two
low, all in `check_floor_bash`. The two `[dSP-95]` restore checks read only the memo, so each reads
`ok` on a path it did not run. The narrowed copy's staging raises `FileExistsError` on a reused
`tmp`. This unit makes three edits inside `check_floor_bash`, each at the fix the review's skeptic
judged sound.

## 2. Scope (IN)

- **S1** — items 1 and 2 (ids 1 and 4), the raise path. The check at `selftest.py:4517-4518`
  gains `isinstance(cut94, OSError)` ahead of its memo read, and its detail names `cut94`. This is
  item 1's stricter form, which the review says also closes item 2. Observed by AC2, AC3 and AC4.
- **S2** — item 1 (id 1), the return path. The check at `selftest.py:4516` gains
  `argv94 == ["bash", "x"]` ahead of its memo read, and its detail names `argv94`. Observed by AC2
  and AC4.
- **S3** — item 3 (id 2), a reused `tmp`. One line,
  `shutil.rmtree(tmp / "dsp94-narrowed", ignore_errors=True)`, sits after `steps94`'s placeholder
  (`:4493`) and before the `try` that calls `build_staged_copy` (`:4494-4496`).
  `build_staged_copy` itself is not edited. Observed by AC1 and AC5.

## 3. Non-goals (OUT)

- Any change to `build_staged_copy` (`selftest.py:3640-3649`), such as `dirs_exist_ok`. The review
  says to leave its shared semantics unchanged, and the suite calls it from other arms.
- Item 3's left-shift gate, a selftest call that runs `check_floor_bash(tmp)` twice in one
  directory and compares the FAILURES lists. It would be a second mechanism. AC1 makes the same
  observation by hand, and the main loop owns the review's checklist entry.
- A `[dSP-95]` check that reads red apart from its paired `[dSP-94]` check. S1 and S2 add the very
  conjuncts those checks already hold, so no break can split them. §5 risks says so.
- Any edit to `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-95.md`, which is
  CLOSED.
- Product code. `tools/govkit/upgrade_steps.py` is read and not edited.

### Edges

none

## 4. Design

Every cited line holds at `744d2551`. The measurements were taken on 2026-11-01 on node a, Windows,
Python 3.15.2. They ran in a scratch repository made by `git archive 744d2551 tools` and committed
once with `core.longpaths` set. The fenced text below was applied to its working tree as written,
and each break in "Measured" was applied on top of it.

### S1 and S2: each restore check reads its own path

`read_fallback_argv` (`selftest.py:4470-4484`) restores `steps._BASH` in a `finally`
(`:4483-4484`), so the memo comes back whether `resolve_shell_argv` returns or raises. A check
that reads only the memo therefore cannot tell the two paths apart. `us`'s read takes the return
path: its `resolve_shell_argv` catches the `Refusal` and hands back the argv
(`upgrade_steps.py:437-440`). `steps94`'s read takes the raise path, because its narrowed
`check_runs` lets the spawn's `OSError` escape. `argv94` and `cut94` are the two results
(`selftest.py:4509`). The two checks at `:4516-4518` become:

```python
    check("[dSP-95] the read gives the parent's bash cache back",
          argv94 == ["bash", "x"] and us._BASH == bash87, f"argv94 {argv94!r}; {us._BASH!r}")
    check("[dSP-95] the read that raises gives the copy's bash cache back",
          isinstance(cut94, OSError) and getattr(steps94, "_BASH", None) == sentinel94,
          f"cut94 {cut94!r}; {getattr(steps94, '_BASH', None)!r}")
```

`OSError` and not `BaseException`: item 1's form also closes item 2, and it is the class the second
`[dSP-94]` check (`:4514-4515`) already requires of `cut94`.

### S3: the staging directory removed first

`build_staged_copy` calls `shutil.copytree` without `dirs_exist_ok` (`selftest.py:3646`), so a
second call on one `tmp` raises `FileExistsError` inside the guarded load. The other writes
`check_floor_bash` makes under `tmp` already tolerate a reused directory: `mkdir(exist_ok=True)`
at `:4442` and `:4528`, and `rmtree(ignore_errors=True)` at `:4537`. S3 uses the last idiom:

```python
    steps94 = types.ModuleType("dsp94_upgrade_steps")
    shutil.rmtree(tmp / "dsp94-narrowed", ignore_errors=True)  # TOOL-dSafePassage-96: a reused tmp stages afresh
    try:
```

The bar is unaffected either way. Its one call reaches `check_floor_bash` through
`check_step_isolation` (`:4427`) inside a fresh `TemporaryDirectory` (`:5523`).

### Measured

The command is AC1's, which runs `check_floor_bash` twice on one `tmp`, about 7 s. Each row is
one break and names the lines that read `FAIL`. Every other line printed reads `ok`. Each row ran
once.

| Tree | Break | Lines that read `FAIL` |
|---|---|---|
| `744d2551` | none | first run none; second run `[dSP-95] the staged copy ... loads` (`FileExistsError`), the second `[dSP-94]` and the raise-path `[dSP-95]` |
| S1 to S3 | none | none on either run |
| `744d2551` | `steps._BASH = None` cut from `read_fallback_argv` | both `[dSP-94]`; both `[dSP-95]` read `ok` |
| S1 to S3 | `steps._BASH = None` cut | both `[dSP-94]` and both `[dSP-95]`, naming `argv94` with the parent's bash and `cut94 ['dsp95-sentinel', 'x']` |
| `744d2551` | S4's replacement of 95 given back `except OSError:` | the second `[dSP-94]`; both `[dSP-95]` read `ok` |
| S1 to S3 | that break | the second `[dSP-94]` and the raise-path `[dSP-95]`, naming `cut94 ['bash', 'x']`; the return-path `[dSP-95]` reads `ok` |
| `744d2551` | the `finally` cut | both `[dSP-95]`, each naming `None` |
| S1 to S3 | the `finally` cut | both `[dSP-95]`, naming `argv94 ['bash', 'x']; None` and an `OSError` `cut94` |
| S1 to S3 | S3's line cut | first run none; second run the same three as `744d2551` |

The `steps._BASH = None` row is the review's probe for item 1. The `except OSError:` row is item 2's,
a copy whose `resolve_shell_argv` returns. Over S1 to S3, `read_handpicked_copies` still returns
`([], 1)`, so S3's line is not read as a hand-picked copy. A Linux node was not measured.

### Inventory

No local, function, constant, type, file, check label, flag, conf key, gate leg or receipt field is
minted. Two check conditions change and one line is added, so the naming lexicon grades nothing new.

### Migration

None.

### Rollout

Live at landing, at order 16.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **Staging under a fresh `tempfile.mkdtemp(dir=tmp)`.** The review allows it. It leaves one copy
  of the kit per run under a reused `tmp`, and `:4537` already sets the `rmtree` idiom.
- **`isinstance(cut94, BaseException)` for item 2.** Item 1's `OSError` form satisfies item 2, and
  the second `[dSP-94]` check already names that class.
- **`dirs_exist_ok=True` in `build_staged_copy`.** It would leave a stale engine copy in place for
  every caller. §3 gives the reason.

## 5. Production-readiness checklist

- security: no write path, spawn or surface. S3 removes a directory the same function creates under
  the scratch root.
- perf / scale: one `rmtree` of a directory absent on the bar's run. AC1 measured about 7 s for two
  calls.
- error / empty / loading states: an `rmtree` that cannot remove a file is ignored, and the
  `copytree` that follows then records the labelled `[dSP-95] ... loads` FAIL, as at `744d2551`.
- observability: each restore check's detail names `argv94` or `cut94`.
- risks: S1 and S2 add the conjuncts the first two `[dSP-94]` checks already hold, so each
  `[dSP-95]` check reads red only beside its paired `[dSP-94]` check. What S1 and S2 buy is that a
  `[dSP-95]` ok, read alone, now shows its path ran. A `[dSP-95]` check is not seen red by itself.
- testing: §7's New arms, and AC1 to AC5.
- migration: none.
- user docs: none. No page under `help/` describes the selftest's floor checks.

## 6. Acceptance criteria

- **AC1** — When
  `python -c "import pathlib, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; t = pathlib.Path(tempfile.mkdtemp()); s.check_floor_bash(t); print(s.FAILURES); s.check_floor_bash(t); print(s.FAILURES)"`
  runs from the repository root, both printed lists are `[]`, and every check line of both runs
  reads `ok`.
  Red when: the staging directory is not removed first. At `744d2551` the second list names
  `[dSP-95] the staged copy of upgrade_steps.py loads`, the second `[dSP-94]` check and the
  raise-path `[dSP-95]` check, measured. The first list is a preservation check: it is `[]` at
  `744d2551`, measured.
  cost: about 7 s, measured.
  fixture: a node whose `PATH` holds a bash, as `[dSP-87 AC5]` already needs.
- **AC2** — When the line `steps._BASH = None` is cut from `read_fallback_argv` in a scratch
  repository made by `git archive HEAD tools`, AC1's command prints `FAIL` for both `[dSP-94]`
  checks and both `[dSP-95]` restore checks, and the two `[dSP-95]` details name `argv94` and
  `cut94 ['dsp95-sentinel', 'x']`.
  Red when: a restore check reads only the memo. At `744d2551` both `[dSP-95]` lines read `ok`
  under this break, measured. The two `[dSP-94]` FAILs are a preservation check: they read `FAIL`
  at `744d2551`, measured.
  cost: about 7 s, plus the scratch repository.
  fixture: on Windows the scratch commit needs `core.longpaths` set. The tree holds no such scratch
  repository today.
- **AC3** — When the narrowed copy's replacement text is given back `except OSError:` in the same
  kind of scratch repository, AC1's command prints `FAIL` for the second `[dSP-94]` check and for
  `[dSP-95] the read that raises gives the copy's bash cache back`, whose detail names
  `cut94 ['bash', 'x']`, and `ok` for the return-path `[dSP-95]` check.
  Red when: the raise-path check does not require `cut94` to be an `OSError`. At `744d2551` it reads
  `ok` under this break, measured. The second `[dSP-94]` FAIL and the return-path `ok` are a
  preservation check: both read so at `744d2551`, measured.
  cost: about 7 s, plus the scratch repository.
- **AC4** — When the `finally` and its restore line are cut from `read_fallback_argv` in the same
  kind of scratch repository, AC1's command prints `FAIL` for both `[dSP-95]` restore checks and
  `ok` for every other line.
  Red when: S1 or S2 drops the memo read. This is a preservation check: at `744d2551` both
  `[dSP-95]` lines read `FAIL` under this break, each naming `None`, measured.
  cost: about 7 s, plus the scratch repository.
- **AC5** — When
  `git grep -n -F 'shutil.rmtree(tmp / "dsp94-narrowed", ignore_errors=True)' -- tools/govkit/selftest.py`
  runs, it prints one line, inside `check_floor_bash` and above the `try` that calls
  `build_staged_copy`. And `git diff --numstat 744d2551 -- tools` prints one line, for the selftest
  file.
  Red when: the line is missing or the build edits a second file under the tools directory. At
  `744d2551` the grep and the diff both print nothing, measured. The diff reads `tools` alone, so a
  records block the generator re-renders under `memory` does not move it.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 AC3 AC4 · `[dSP-95] the read that raises gives the copy's bash cache back`, staged red by the `except OSError:` replacement and by the `steps._BASH = None` cut · none
New arm: tools/govkit/selftest.py · covers AC2 AC4 · `[dSP-95] the read gives the parent's bash cache back`, staged red by the `steps._BASH = None` cut · none

The leg line names the five legs whose guard covers the selftest file in `tools/gate-legs.json`:
the four guarded by the govkit directory, and `policy fixtures`, guarded by the file itself. The
rest are 95's, unchanged, because 96 touches the same one file. No refusal call site is added, so
`govkit refusal join`'s pin does not move. AC1's twice-run is not an arm. The bar runs
`check_floor_bash` once, and §3 says why no arm runs it twice.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-96-1-spec-writer.md` and
  its brief `memory/builds/dSafePassage/prompts/2026-11-01-prompt-TOOL-dSafePassage-96-spec-brief.md`.
  It closes the round-7 closing diff review,
  `memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-95-closing-diff-round7.md`:
  items 1 and 2 at the skeptic's sound fix in S1 and S2, and item 3 at its `rmtree` fix in S3. Each
  break in §4 "Measured" was run in a scratch repository from `744d2551`.

## 10. Reuse audit

S1 to S3 extend `check_floor_bash` (`tools/govkit/selftest.py:4430`), the function 94 and 95 built,
and S3 reuses its own `rmtree(ignore_errors=True)` idiom at `:4537`. That seam was found by reading
the function. `python tools/codebase-map/reuse_lookup.py "clear a scratch directory before staging a copy so a rerun on a reused tmp does not collide"`
ranked scratch helpers by name stem, such as `build_scratch_gov` and `remove_scratch_tree`. None
of them removes a staging directory inside this suite, so no existing seam fits better than the
function's own idiom. The recall probe's one relevant decision is `TOOL-aBranchedMandate-6`:
`rmtree(ignore_errors=True)` cannot remove read-only git objects on Windows. The staged copy holds
no `.git`, and §5 says what a file it cannot remove does. The other hits were this review and its
briefs.

Recall terms used: `python tools/memory-recall/query.py "a selftest arm that writes under tmp fails when rerun on the same directory; a restore check passes on a path it did not run" --terms "check_floor_bash build_staged_copy copytree dirs_exist_ok FileExistsError rmtree ignore_errors dsp94-narrowed cut94 argv94 sentinel94 raise path"`
