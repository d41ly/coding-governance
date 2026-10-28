# TOOL-dSafePassage-71 — govkit selftest's staged-break copies of upgrade_steps.py take the whole govkit directory through one helper, and an arm reds a copy that hand-picks its files

**Status:** CLOSED · rev-1 · 2026-10-28 · node d · Tier-2 · base c9baa97c · streams tooling · order 10 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-42

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dSafePassage-71-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-71-ledger.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-71-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-71-1-spec-writer.md) | research | — |
| [2026-10-28-prompt-TOOL-dSafePassage-71-2-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-71-2-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-71-build-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-71-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Four arms of `tools/govkit/selftest.py` write a patched `upgrade_steps.py` into a scratch directory
and run it. Each one picks by hand which sibling files go beside it. `upgrade_steps.py` loads
`fixture_target` from its own directory (`tools/govkit/upgrade_steps.py:3176-3183`), and the
isolation fixture calls that loader (`:2610`). So the `[dSP-36]` copy, which holds only `govkit.py`
(`tools/govkit/selftest.py:3630-3642`), dies on `ModuleNotFoundError: No module named
'fixture_target'` and never prints the `isolation: FAILED` its check needs. This unit routes every
such copy through one helper that copies the whole kit directory, and adds an arm that reds the
next arm to hand-pick its files. TOOL-dSafePassage-42's builder found the defect
(`memory/builds/dSafePassage/RUN.md`, the `rescope` line of 2026-10-28T03:13:19Z).

## 2. Scope (IN)

- **S1** — The helper. `build_staged_copy(root: pathlib.Path, text: str) -> pathlib.Path` in
  `tools/govkit/selftest.py` copies `HERE` to `root / HERE.name` with
  `shutil.copytree(..., ignore=shutil.ignore_patterns("__pycache__"))`. It then writes `text` as
  that copy's `upgrade_steps.py`, UTF-8 with `newline="\n"`, and returns the path of that file. It
  sits beside `check_step_isolation`, above it. Observed by AC1 and AC3.
- **S2** — The four arms route through it. Each one keeps its own replace text, its anchor count
  and its check, and loses its `mkdir`, its `shutil.copy(HERE / ...)` lines and its
  `write_text` of `upgrade_steps.py`.

  | Arm | Site at base | Fixture it runs | Today |
  |---|---|---|---|
  | `[dSP-36]` a walk copy rooted at the common dir | `:3630-3642` | `isolation`, two plants | red: `ModuleNotFoundError` |
  | `[dSP-42] AC5` a walk copy reading the index first | `:3656-3666` | `isolation --plant submodule-fsmonitor` | green: copies `fixture_target.py` by hand |
  | `[dSP-7] AC6` a planted spawn of `row["up"]` | `:3715-3723` | `isolation --plant callers` | green |
  | `[dSP-35] AC4` a judge copy reading the clock late | `:3916-3936` | `lock --plant lock-live-slow-census` | green |

  The `[dSP-35]` arm keeps its own copy of `tools/process-monitor/census.py` into
  `pathlib.Path(td) / "process-monitor"`, which `resolve_kit_dir` probes as the copy's
  `here.parent / home` (`tools/govkit/upgrade_steps.py:315-318`). Observed by AC1, AC2 and AC5.
- **S3** — The class predicate. `read_handpicked_copies(text: str) -> tuple[list[int], int]` returns
  two things. The first is the line numbers of `text` outside `build_staged_copy`'s body that carry
  a bare local name, other than `HERE`, followed by `/ "upgrade_steps.py"`. The second is how many
  lines inside that body carry the same shape. The body is located by `_ast`, as the `FunctionDef`
  named `build_staged_copy` from its `lineno` to its `end_lineno`, never by searching for a literal.
  Observed by AC4.
- **S4** — The class arm. `check_staged_copies(tmp: pathlib.Path)` runs after `check_step_walk()` in
  the suite's dispatch (`tools/govkit/selftest.py:4685`), over `tmp / "dst"`. It makes three checks,
  tagged `[dSP-71]`. First, over `selftest.py`'s own text, `read_handpicked_copies` returns no line
  outside the helper and at least one inside it. Second, over that text with one hand-picked line
  appended at column 0, so `_ast` still parses it, it names exactly that line. The appended line is
  the base `[dSP-36]` write, `(rooted / "upgrade_steps.py").write_text(src)`, assembled at runtime
  (§4). Third, `build_staged_copy(tmp / "dst", "")` leaves the same
  set of relative file paths as `HERE` outside every `__pycache__` directory. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- The scratch-gov builders. `build_steps_gov` (`tools/govkit/selftest.py:2897-2912`), the
  `g / PFX / KIT_NAMES["govkit"]` copies such as `:13948-13950`, and the `_g21` break at `:18233` build
  a gov tree with its own registry and descriptors. They run `govkit.py` or `upgrade_steps.py list`,
  and neither reaches `load_fixture_target`. A whole-directory copy would bring gov's own
  `registry.toml`, `steps.toml` and `steps/` into a tree whose arms plant those files.
- `upgrade_steps.py`'s own fixture govs, `build_walk_gov`
  (`tools/govkit/upgrade_steps.py:3253-3274`) and `build_update_gov` (`:3808-3866`). Their copies of `upgrade_steps.py` are the scratch gov's installed engine, and the
  fixture child runs `HERE / "upgrade_steps.py"`, not the copy (`:3378`, `:3543`).
- Sibling kits beside the copy. Only the `[dSP-35]` arm needs one, `process-monitor`, and it already
  copies it. A helper keyword for one caller is scaffolding.
- A change to `upgrade_steps.py`'s loaders. `load_fixture_target` imports only when a fixture runs,
  so a scratch gov that holds the module and not the factory still imports (`:3177-3179`).

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-7's `[dSP-7] AC6` callers arm
and the isolation fixture; TOOL-dSafePassage-36's `[dSP-36]` walk copy; TOOL-dSafePassage-35's
`[dSP-35] AC4` judge copy; TOOL-dSafePassage-42's `[dSP-42] AC5` index-first copy, which first
copied `fixture_target.py` by hand; and TOOL-dSafePassage-5's and TOOL-dSafePassage-26's
`fixture_target.py` factory and `load_fixture_target`. The edge join counts CLOSED specs
(`tools/memory-tree/check-memory-hygiene.sh:2676-2720`), and a CLOSED spec cannot take the matching
`hands-off` line.

## 4. Design

### What the copy must carry, read from the code

`upgrade_steps.py` reaches files beside itself in more ways than `import`. Of these, only the
fixture loader is an `import` statement.

| Reach | Site | How |
|---|---|---|
| `govkit.py` | `tools/govkit/upgrade_steps.py:2406-2414` | `spec_from_file_location` on `HERE / "govkit.py"` |
| `fixture_target.py` | `:3176-3183` | `sys.path.insert(0, str(HERE))`, then `import fixture_target` |
| `steps/receipt_schema_4.py`, `steps.toml` | `:3239`, `:3247` | read as text |
| `tools/process-monitor/census.py` | `:2153-2154` | `resolve_kit_dir`, then `spec_from_file_location` |

A copy driven by the module's import list sees one row of four, because an `ast` walk of
`import` nodes finds `fixture_target` and nothing else. A copy of the directory carries every row
that lives in it, today's and the next one's. The directory holds 43 files outside `__pycache__`.
Its `shutil.copytree` measured 0.03 s on node d on 2026-10-28 (PINNED). The fourth row lives in a
sibling kit, which S2 leaves to its one caller.

`__pycache__` is excluded because a stale bytecode file can run in place of the staged break. The
`[dSP-35]` break swaps two lines, so the patched file has the original's size. A cached `.pyc`
copied with its source's mtime can then validate against a file written in the same second
(`memory/gotchas/staged-break-runs-stale-bytecode.md`).

### Observed at base, through a stand-in for the helper

A scratchpad probe ran each arm's fixture over two copies of the arm's own patched text: the
hand-picked copy at base, and `copytree` of `tools/govkit/` without `__pycache__`, named `HERE.name`.

| Arm | Hand-picked copy | Directory copy |
|---|---|---|
| `[dSP-36]`, both plants | exit 1, `ModuleNotFoundError`, no `isolation: FAILED` | exit 1, `isolation: FAILED` |
| `[dSP-42] AC5` | green | exit 1, `fsmonitor canary: present`, `isolation: FAILED` |
| `[dSP-7] AC6` | green | exit 1, names `upgrade_steps.py:<n>, in planted_spawn` |
| `[dSP-35] AC4` | green | `lock: taken`, `lock: FAILED` |

### The class predicate, run over the real tree first

The candidate is the regex
`(?<![\w.])(?<!/ )(?!HERE\b)[A-Za-z_]\w* / "upgrade_steps\.py"`, applied per line. It matches a
bare local directory joined to `upgrade_steps.py`, which is how an arm both writes and runs a staged
copy. It does not match `HERE / ...`, `GOVKIT.parent / ...`, or a gov-tree chain such as
`g / PFX / gkn / ...`. Over `tools/govkit/selftest.py` at base it names 8 lines, `:3635`, `:3639`,
`:3661`, `:3664`, `:3720`, `:3721`, `:3926` and `:3930`. That is a write and a run in each of the four
arms, and nothing else (PINNED, measured 2026-10-28). Over every other `.py` file under `tools/` it
names one line, `tools/govkit/upgrade_steps.py:3263`, which is `build_walk_gov`'s scratch gov and
out of scope (§3). After S2, the helper's own write is the only line it names.

The arm never spells the shape it hunts. Its plant is assembled at runtime from two string pieces
that split `upgrade_steps` from `.py`. The regex spells `\.py`, so it never matches itself. Without
those two rules, the arm's own source would be a hit outside the helper.

What the predicate does not check: a path built another way, such as `joinpath`, an f-string or a
variable holding the file name; a copy written in any file but `selftest.py`; whether a gov-tree copy
carries what its run imports; and the sibling kit a copy resolves through `resolve_kit_dir`.

### Inventory

Minted: the functions `build_staged_copy`, `read_handpicked_copies` and `check_staged_copies`, in
`tools/govkit/selftest.py`. `python tools/lexicon/lexicon.py --suggest <name> --as py.function`
answered OK for each on 2026-10-28, leading with the declared verbs `build`, `read` and `check`. The
arm tag `[dSP-71]` is minted, and so is the scratch name `tmp / "dst"`, which no other line of
`selftest.py` uses. No conf key, gate leg, constant, receipt field or `Refusal` site is minted.

### Migration

None.

### Rollout

Live at landing, at order 10 beside TOOL-dSafePassage-42, whose `[dSP-42] AC5` arm S2 rewrites.
Both write `tools/govkit/selftest.py`, so M6 sequences them, and this unit builds after 42.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **Copy driven by the module's import list.** It misses `govkit.py`, which is loaded by path, and
  every text read under `HERE`. It would be a second parser of the module's dependencies beside the
  module itself.
- **Add `fixture_target.py` to the `[dSP-36]` copy.** That is the fix TOOL-dSafePassage-42 made to
  its own arm, and it leaves the class open for the next import.
- **Make `load_fixture_target` tolerate a missing factory.** The isolation fixture needs the factory
  to build its target, so the copy would die one line later.
- **Gate on `shutil.copy(HERE / `.** At base it names 16 lines, 12 of them gov-tree builders that are
  out of scope, so it would need an exemption list.

## 5. Production-readiness checklist

- security: N/A — selftest code only. No spawn, argv, path or input is added beyond the copies the
  arms already make.
- perf / scale: four copies of 43 files at about 0.03 s each, plus one more in the class arm.
- error / empty / loading states: a helper that cannot be found by `_ast` gives the predicate no
  inside count, and the arm's first check reds rather than reading an empty population as clean.
- observability: each `[dSP-71]` check prints the lines it names, or the file-set difference, as its
  detail.
- risks: a file later added to `tools/govkit/` that changes a fixture's behaviour by being present.
  The base probe saw none across the four arms.
- testing: the four routed arms re-observe their staged breaks through the helper, and
  `check_staged_copies` observes the class, both under §7's `New arm:` lines.
- migration: none.
- user docs: N/A — no user-facing behaviour changes, and no page under `help/` names these arms.

## 6. Acceptance criteria

The probes below run from the repository root. Each imports `selftest.py` as a module, which runs
no arm because the suite sits behind `if __name__ == "__main__"` (`tools/govkit/selftest.py:18724`).

- **AC1** — When `build_staged_copy` stages the `[dSP-36]` arm's walk-copy text and the copy runs
  `fixture isolation --plant submodule-unpopulated-worktree`, then `--plant submodule-main-only`, the
  probe below prints `submodule-unpopulated-worktree 1 True False` and
  `submodule-main-only 1 True False`. That is exit 1, `isolation: FAILED` printed, and no
  `ModuleNotFoundError`.
  Red when: the helper copies only `govkit.py`, so each run prints `1 False True`, which a probe of
  the base shape showed on 2026-10-28.
  cost: about a minute, two scratch fixtures.

  ```python
  import pathlib, subprocess, sys, tempfile
  sys.path.insert(0, "tools/govkit")
  import selftest as s
  src = (s.HERE / "upgrade_steps.py").read_text(encoding="utf-8")
  walk = '                mods = d / "modules"'
  text = src.replace(walk, '                mods = (pathlib.Path(git(target, "rev-parse", '
                           '"--path-format=absolute", "--git-common-dir").strip()) '
                           'if not via else d) / "modules"')
  with tempfile.TemporaryDirectory() as td:
      py = s.build_staged_copy(pathlib.Path(td), text)
      for plant in ("submodule-unpopulated-worktree", "submodule-main-only"):
          p = subprocess.run([sys.executable, str(py), "fixture", "isolation", "--plant", plant],
                             capture_output=True, text=True, encoding="utf-8", errors="replace")
          out = p.stdout + p.stderr
          print(plant, p.returncode, "isolation: FAILED" in out, "ModuleNotFoundError" in out)
  ```

- **AC2** — When the other three arms' texts are staged by `build_staged_copy` in the same way, with
  each arm's own replace text as that arm writes it, each fixture shows its arm's break.
  `fixture isolation --plant submodule-fsmonitor` exits 1, printing `fsmonitor canary: present` and
  `isolation: FAILED`. `fixture isolation --plant callers` exits 1, naming
  `upgrade_steps.py:<n>, in planted_spawn`, where `<n>` is the planted text's line count.
  `fixture lock --plant lock-live-slow-census` prints `lock: taken` and `lock: FAILED`, with
  `tools/process-monitor/census.py` copied beside the staged directory.
  Red when: the helper's copy changes what one of these fixtures does, so an arm's break no longer
  shows.
  cost: about two minutes.
- **AC3** — When
  `python -c "import pathlib, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; t = pathlib.Path(tempfile.mkdtemp()); d = s.build_staged_copy(t, '').parent; rel = lambda r: sorted(p.relative_to(r).as_posix() for p in r.rglob('*') if p.is_file() and '__pycache__' not in p.parts); print(rel(d) == rel(s.HERE), (d / 'upgrade_steps.py').read_text(encoding='utf-8') == '')"`
  runs, it prints `True True`.
  Red when: the helper copies a hand list, or copies `__pycache__`, or leaves the original
  `upgrade_steps.py` in place of `text`.
- **AC4** — When
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import selftest as s; t = (s.HERE / 'selftest.py').read_text(encoding='utf-8'); o, n = s.read_handpicked_copies(t); print(o, n >= 1); u = t + '(rooted / ' + chr(34) + 'upgrade_steps' + '.py' + chr(34) + ').write_text(src)\n'; print(s.read_handpicked_copies(u)[0] == [len(u.splitlines())])"`
  runs, it prints `[] True` and then `True`.
  Red when: an arm still writes or runs a bare-directory `upgrade_steps.py` outside the helper, so
  the first list is not empty; or the regex stops matching the helper's own write, so the inside
  count is 0; or the appended line is not named.
- **AC5** — When `git grep -n -e "build_staged_copy(" -e "shutil.copy(HERE / " -- tools/govkit/selftest.py`
  runs, it prints the helper's `def` line, its four call sites in the arms of S2 and its call in
  `check_staged_copies`, and no `shutil.copy(HERE / ` line.
  Red when: an arm of S2 still builds its copy by hand.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the `[dSP-36]`, `[dSP-42] AC5`, `[dSP-7] AC6` and `[dSP-35] AC4` arms moved onto `build_staged_copy`; `[dSP-36]` is observed RED at base c9baa97c, where its copy holds only `govkit.py`, and GREEN after the build · none

New arm: tools/govkit/selftest.py · covers AC3 AC4 · `check_staged_copies`, tagged `dSP-71`; its plant stages the predicate's failing case in the arm, and the close stages the arm's own red by restoring the `[dSP-36]` arm's hand-picked copy in a working copy · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from TOOL-dSafePassage-42's builder finding, by
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-71-2-spec-writer.md`.

## 10. Reuse audit

The seam extended is `selftest.py`'s own idiom of copying the kit directory whole:
`shutil.copytree(HERE, ...)` in the scratch-gov builder at `tools/govkit/selftest.py:5593`, with
`shutil.ignore_patterns` as at `:5880`. No helper builds a staged-break copy today. Each of the four
arms inlines its own, at the sites S2's table names, and S1 extracts them at the fourth instance. `python tools/codebase-map/reuse_lookup.py "copy the govkit directory into a scratch dir and run a patched upgrade_steps.py from it"`
ranked `run`, `resolve_kit_dir`, `scratch`, `build_scratch_gov` and `read_steps`, all name-token
matches. `build_scratch_gov` (`tools/govkit/fixture_target.py`) builds a gov repository rather than a
kit directory, and none of the others copies files, so no existing seam fits beyond the idiom above.
The recall probe ranked TOOL-aWokenSentinel-24 first. That unit made one tick-suite staged break into
a single helper that two arms name, which is the pattern S1 follows. It sits in another kit's suite,
so it is a precedent and not a seam.

Recall terms used: `python tools/memory-recall/query.py "how does a selftest arm stage a broken copy of upgrade_steps.py beside the modules it imports" --terms "staged break walk copy upgrade_steps govkit selftest fixture_target sibling module copytree ModuleNotFoundError arm red"`
