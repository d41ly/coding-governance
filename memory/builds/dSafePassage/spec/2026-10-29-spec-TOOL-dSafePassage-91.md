# TOOL-dSafePassage-91 — the round-3 closing review's three remaining minors: the in-place row's one snapshot path, a grader for the walk's two roots, and an arm for the floor stub's bash fallback

**Status:** DEFERRED · rev-2 · 2026-10-29 · node a · Tier-2 · base cbaaeebe · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-prompt-TOOL-dSafePassage-90-audit-fold-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-90-audit-fold-brief.md) | research | TOOL-dSafePassage-90 |
| [2026-10-29-prompt-TOOL-dSafePassage-90-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-90-spec-brief.md) | research | TOOL-dSafePassage-90 |
| [2026-10-29-prompt-TOOL-dSafePassage-91-build-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-91-build-brief.md) | journal | — |
| [2026-10-29-review-TOOL-dSafePassage-90-91-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dSafePassage-90-91-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-90 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 closing diff review confirmed four mediums and two lows. TOOL-dSafePassage-90 closes M1
(id 1), M2 (id 2) and M3 (id 5) with its one mechanism, so three remain. They are a rollback order
that names an in-place row twice, L1 (id 4); a split between two roots that no permanent check holds,
M4 (id 6); and a bash fallback that no check observes, L2 (id 7). This unit closes all three, each
at the fix the review's skeptic judged sound, which for M4 and L2 is the skeptic's corrected fix.
Each fix is held by an arm that is red against the break the review names. BUILD-METHOD M4 batches
the minors into one unit, and this one builds after TOOL-dSafePassage-90, which edits two of the
same files.

## 2. Scope (IN)

- **S1** — L1 (id 4), an in-place row is snapshotted at its one path. In `_cmd_update`'s pre-write
  snapshot (`tools/govkit/govkit.py:10745-10747`), a `renamed` row's destination joins `_paths` only
  when it differs from the row's own path. So the rollback restores an in-place row once, and its
  order prints one `restored` line for it. The `DEPL-dCarriedReceipt-11` block of
  `tools/govkit/selftest.py` gains a `[dSP-91 L1]` check after TOOL-dSafePassage-90's `[dSP-90]`
  check, on its own fixture: gov's root moves, and a sibling rename onto the adopter's own file holds
  the kit back. The in-place fixture's kit text, now an inline literal (`selftest.py:13087-13090`),
  is bound to one name that both fixtures read. §4 "S1". Observed by AC1 and AC2.
- **S2** — M4 (id 6), the walk's two roots are patched apart and graded. A new function in
  `tools/govkit/upgrade_walk.py`, `derive_policy_adopter`, answers the policy adopter's path in the
  walked target from the target's install prefix. `build_release_tree` calls it at `:248`, where the
  expression sits inline now. The kind-to-file table typed inside `read_fixture_rows` (`:136`)
  becomes the module constant `FIXTURE_FILES`, which that function reads. `check_graders` (`:976`)
  gains a `plant-root` grader, and its docstring (`:977-980`) names it. With `derive_tool_root`
  patched to answer `moved`, the grader reads every row of every kind in `FIXTURE_FILES`. Each
  `path`, `from` and `to`, nested ones included, that resolves under either root must resolve under
  its own kind's: `moved` for `gov_plant`, `read_target_prefix()` for every other kind. Both roots
  must be sampled, and the policy adopter must sit under the target's prefix. §4 "S2". Observed by
  AC3 and AC4.
- **S3** — L2 (id 7), the floor stub's fallback to bare `bash` has an arm. A new module function of
  `tools/govkit/selftest.py`, `check_floor_bash`, takes TOOL-dSafePassage-87's `[dSP-87 AC5]` block
  out of `check_step_isolation` (`:4422-4448`), which calls it there, and adds a `[dSP-91 L2]` check
  after it. The new check runs the floor row's witness on the same unusable-bash `PATH` with
  `GOV_BASH` unset. Its tail must name `bash` or the floor script, and must carry none of
  `python_floor.py:`, `upgrade_steps.Refusal` and `Set GOV_BASH`. A new context manager of
  `selftest.py`, `set_environ`, holds the environment for both checks and for the two other copies
  of that save-and-restore loop in `check_step_isolation` (`:3766`, `:4409`).
  `tools/govkit/steps/python_floor.py` is not edited. §4 "S3". Observed by AC5, AC6 and AC7.

## 3. Non-goals (OUT)

- M1 (id 1), M2 (id 2), H1 (id 3) and M3 (id 5). TOOL-dSafePassage-90 closes them, or shows them
  unreachable, with its one mechanism.
- Widening the census at `selftest.py:15426` to parse `tools/govkit/steps/`. L2's gate note names it
  as what "would catch the next file it misses"; the review's fix is the check alone, and S3 is that
  check.
- The bug-class checklist lines that M3's and M4's gate notes name. The review records that no
  checklist exists, and each item's persisted arm here is its gate.
- A green `upgrade-walk` row in the foreign-prefix parity leg. S2's grader observes the root split on
  the real tree, at gov's own root, by patching one root apart.
- Asserting an rc in S3's check. What bare `bash` resolves to is the node's. On Windows the loader
  finds the System32 WSL launcher before it searches `PATH`, whatever `PATH` holds
  (`upgrade_steps.py:372-376`), measured as rc `127` on node a (§4 "S3").
- The round-1 spec audit's left-shift gates. The main loop takes them; none is authored here.

### Edges

- **consumes-from** `TOOL-dSafePassage-90` — its S1 edits `_cmd_update`'s `renamed` write arm
  (`govkit.py:11062-11114`), which this unit does not touch; the two share only the
  `DEPL-dCarriedReceipt-11` block of `selftest.py`, where this unit's `[dSP-91 L1]` check anchors
  after 90's `[dSP-90]` check and binds `_kit88`; without 90 that check has no anchor in the block

## 4. Design

Every cited line holds at `cbaaeebeb`, the build head with TOOL-dSafePassage-86, -87, -89 and -88
landed. At rev-2 `git diff --stat cbaaeebeb a3ad798cf -- tools skills` printed nothing, and every
line rev-2 adds was read at `a3ad798cf`. TOOL-dSafePassage-90 edits `govkit.py` and `selftest.py`
before this unit builds, so the builder re-reads each cited line by content before editing. Each measurement below was taken on
2026-10-29 on node a, in scratch copies of the engine under the temp root.

### S1: one snapshot path for an in-place row

At `govkit.py:10746`:

```python
        if a["verdict"] == "renamed" and a["c"].get("renamed_to") and a["c"]["renamed_to"][1] != _paths[0]:
            _paths.append(a["c"]["renamed_to"][1])
```

A moved row keeps both spellings, as DEPL-dCarriedReceipt-14 requires. An in-place row, whose
`renamed_to[1]` is its own path (TOOL-dSafePassage-88's `in_place`), is recorded once. Its index
lookup (`:10799-10805`) and the `_left` test (`:8524`) read the one path as they read two equal ones.
This is the skeptic's sound fix. It does not touch a case-only rename, whose spellings differ as
strings, and which TOOL-dSafePassage-90 refuses before any write.

The arm sits after the `[dSP-90]` check and before the `mvfail` fixture (`selftest.py:13126`). The
demo kit text passed to `build_rename_gov` at `:13087-13090` is bound to `_kit88` there, and both
fixtures pass `_kit88`:

```python
        # TOOL-dSafePassage-91: an in-place row in a held-back kit. Gov's root moves, so keep.txt is in
        # place, and other.txt is renamed onto the adopter's own file, so the kit is rolled back. The
        # in-place row is snapshotted at its one path, so the order restores it once.
        _g91 = build_rename_gov("inplace-held", _kit88, "pinned", {"keep.txt": "one\ntwo\n", "other.txt": "other\n"})
        _t91 = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n', "rn-inplace-held-t")
        _ap91 = subprocess.run([sys.executable, str(_g91 / "pinned" / KIT_NAMES["govkit"] / "govkit.py"), "apply",
                                "--target", str(_t91), "--kits", "demo"],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        (_t91 / "pinned" / "demo" / "renamed.txt").write_text("the adopter's own file\n", encoding="utf-8", newline="\n")
        settle(_t91, "the install and the adopter's own file")
        git(_g91, "mv", "pinned", "moved")
        git(_g91, "mv", "moved/demo/other.txt", "moved/demo/renamed.txt")
        git(_g91, "commit", "-qm", "B")
        _up91 = subprocess.run([sys.executable, str(_g91 / "moved" / KIT_NAMES["govkit"] / "govkit.py"), "update",
                                "--target", str(_t91), "--write"],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
        _ord91 = _t91 / ".governance" / "outbox" / "update-rollback-demo.md"
        _rs91 = _ord91.read_text(encoding="utf-8").splitlines().count("restored  pinned/demo/keep.txt") \
            if _ord91.is_file() else None
        check("[dSP-91 L1] a held-back kit's in-place row is restored once, and its order names it once",
              _ap91.returncode == 0 and _up91.returncode == 1 and "ALREADY holds a file there" in _up91.stdout
              and _rs91 == 1 and read_bytes11(_t91 / "pinned" / "demo" / "keep.txt") == b"one\ntwo\n",
              f"apply {_ap91.returncode} update {_up91.returncode} restored {_rs91} " + _up91.stdout[-1500:])
```

It reuses `build_rename_gov` (`selftest.py:12209`), `build_target`, `settle` (`:587`), `git`
(`:583`) and `read_bytes11` (`:12165`). The order's name and its `restored  <path>` line are the ones
the rollback writes (`govkit.py:12293`, `:12314`).

### S1's probe

`l1_probe.py`, run from the repository root. Its one optional argument is the engine directory,
`tools/govkit` by default. It builds the arm's fixture with `fixture_target`'s factories and prints
one line.

```python
import pathlib, shutil, subprocess, sys, tempfile
eng = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "tools/govkit").resolve()
sys.path.insert(0, str(eng))
from fixture_target import build_scratch_gov, build_target
tmp = pathlib.Path(tempfile.mkdtemp(prefix="l1-"))
def git(cwd, *a):
    return subprocess.run(["git", "-C", str(cwd), "-c", "user.email=t@e", "-c", "user.name=t", *a],
                          capture_output=True, text=True, check=True).stdout
g = build_scratch_gov(tmp / "gov")
(g / "pinned" / "govkit").mkdir(parents=True)
for f in ("govkit.py", "adopters.toml", "upgrade_steps.py"):
    shutil.copy2(eng / f, g / "pinned" / "govkit" / f)
(g / "pinned" / "govkit" / "registry.toml").write_text(
    '[surface]\nglobs = ["{prefix}/*"]\n\n[selection]\ndefault = ["demo"]\n\n'
    '[[entry]]\nid = "demo"\ndescriptor = "{prefix}/demo/kit.toml"\n\n'
    '[[exempt]]\npath = "{prefix}/govkit"\nwhy = "the deployer itself"\n', encoding="utf-8", newline="\n")
(g / "pinned" / "demo").mkdir()
(g / "pinned" / "demo" / "kit.toml").write_text(
    'id = "demo"\nhome = "demo"\nversion_from = { none = "fixture" }\n\n[check]\nnone = "a fixture kit"\n\n'
    '[[files]]\ninclude = "**"\nrole = "engine"\n\n[adopt]\nargv = []\nmutates_index = false\n',
    encoding="utf-8", newline="\n")
(g / "pinned" / "demo" / "keep.txt").write_text("one\ntwo\n", encoding="utf-8", newline="\n")
(g / "pinned" / "demo" / "other.txt").write_text("other\n", encoding="utf-8", newline="\n")
git(g, "add", "-A"); git(g, "commit", "-qm", "A")
t = build_target(tmp, 'gov_source = "local"\nprefix = "pinned"\nkits = ["demo"]\n')
subprocess.run([sys.executable, str(g / "pinned" / "govkit" / "govkit.py"), "apply", "--target", str(t),
                "--kits", "demo"], capture_output=True, check=True)
git(t, "add", "-A"); git(t, "commit", "-qm", "install")
(t / "pinned/demo/renamed.txt").write_text("the adopter's own file\n", encoding="utf-8", newline="\n")
git(t, "add", "-A"); git(t, "commit", "-qm", "own file")
git(g, "mv", "pinned", "moved")
git(g, "mv", "moved/demo/other.txt", "moved/demo/renamed.txt")
git(g, "commit", "-qm", "B")
up = subprocess.run([sys.executable, str(g / "moved" / "govkit" / "govkit.py"), "update", "--target", str(t),
                     "--write"], capture_output=True, text=True, encoding="utf-8", errors="replace")
order = (t / ".governance/outbox/update-rollback-demo.md").read_text(encoding="utf-8")
print("in place, sibling refused: update exit", up.returncode,
      "| occupied refused:", "ALREADY holds a file there" in up.stdout,
      "| restored lines for keep.txt:", order.splitlines().count("restored  pinned/demo/keep.txt"),
      "| bytes:", (t / "pinned/demo/keep.txt").read_text(encoding="utf-8").split())
```

Measured, about 6 s each:

| Engine | Line |
|---|---|
| `cbaaeebeb` | `in place, sibling refused: update exit 1 \| occupied refused: True \| restored lines for keep.txt: 2 \| bytes: ['one', 'two']` |
| S1 staged on TOOL-dSafePassage-90's S1 | the same, with `restored lines for keep.txt: 1` |
| TOOL-dSafePassage-90's S1 alone | `restored lines for keep.txt: 2` |

### S2: the plant-root grader

Beside `FIXTURE` (`upgrade_walk.py:44`), the table `read_fixture_rows` types inline at `:136`:

```python
# TOOL-dSafePassage-91 S2: each fixture row kind and the file holding it, read by `read_fixture_rows`
# and walked whole by the plant-root grader.
FIXTURE_FILES = {"plant": "plants.toml", "gov_plant": "plants.toml", "condition": "plants.toml", "arm": "arms.toml"}
```

`:136` then reads `name = FIXTURE_FILES[kind]`. The grader walks the dispatch's own kinds, so a kind
added to the table is graded the day it lands, and no second list of kinds is typed.

Beside `derive_release_engine` (`upgrade_walk.py:199-203`):

```python
def derive_policy_adopter(t) -> pathlib.Path:
    """TOOL-dSafePassage-91 S2: the policy adopter in the walked target. It is a target path, so it
    resolves against the target's install prefix (TOOL-dSafePassage-87 S7), never gov's tool root."""
    _us, _shims, gk = load_engine()
    return gk.resolve_kit_dir("policy", "adopt-policy.sh", t / read_target_prefix()) / "adopt-policy.sh"
```

At `:247-248` the local `adopter` and the inline `resolve_kit_dir` call give way to one call,
`[gk.resolve_bash(), derive_policy_adopter(t).as_posix(), "--scaffold", "--target", t.as_posix()]`.
The function returns the script, not its directory, so the anchor is spelled once.

The `check_graders` docstring (`:977-980`) ends `TOOL-dSafePassage-87's check_shim_paths over gov's
own row at another tool root; returns the reds.` It gains, before `returns the reds`: `and
TOOL-dSafePassage-91's plant-root split: the target's plants and the policy adopter at the install
prefix, gov plants at a moved tool root`.

In `check_graders`, after `check_grade_shim_root` (`:1086-1097`):

```python
    def check_grade_plant_root() -> str:
        gk, pfx = load_engine()[2], read_target_prefix()
        t = build_repo("plant-root-target", {f"{pfx}/policy/adopt-policy.sh": ""})
        real = gk.derive_tool_root
        gk.derive_tool_root = lambda root: "moved"
        try:
            got = {kind: read_fixture_rows(kind) for kind in FIXTURE_FILES}
            try:
                pol = derive_policy_adopter(t)
            except LookupError as e:
                pol = f"LookupError: {e}"
        finally:
            gk.derive_tool_root = real

        def extract_paths(row):
            for k, v in row.items():
                if k in ("path", "from", "to") and isinstance(v, str):
                    yield v
                elif isinstance(v, dict):
                    yield from extract_paths(v)

        bad, seen = [], set()
        for kind, rows in got.items():
            want, wrong = ("moved", pfx) if kind == "gov_plant" else (pfx, "moved")
            for r in (r for r in rows if isinstance(r, dict)):
                for p in extract_paths(r):
                    if p.startswith(want + "/"):
                        seen.add(want)
                    elif p.startswith(wrong + "/"):
                        bad.append(f"the {kind} row {r.get('id') or r.get('name')} read {p}, not under {want}/")
        bad += [f"no fixture row resolved under {w}/, so that root went unsampled" for w in ("moved", pfx)
                if w not in seen]
        bad += [] if isinstance(pol, pathlib.Path) and t / pfx in pol.parents else [
            f"the policy adopter read {pol}, not under the target's {pfx}"]
        return "; ".join(bad)
```

Its row joins the grader tuple (`:1101-1104`) as `("plant-root", check_grade_plant_root)`.
`read_fixture_rows` reads `gk.derive_tool_root` off the module that `load_engine` returns
(`:137-140`), so the patch reaches it. The resolved `{prefix}` is the only root a path carries, so a
path under `moved/` or under the target's prefix is one that `:140` resolved, and the fixture's
literal paths, such as `.claude/settings.json` (`plants.toml:48`), are under neither and are not
graded. At `a3ad798cf` no literal `path`, `from` or `to` in `plants.toml` or `arms.toml` starts with
`tools/` or `moved/`. Every kind's rows are walked, nested ones included: the `held-shim` arm's `shim.from` and
`shim.to` (`arms.toml:50`) and the `missing-plant` arm's `plant.path` (`arms.toml:70`) are sampled
beside the plants and gov plants. That is the round-1 spec audit's M4 (id 12). The `condition` kind
holds no `{prefix}` token today (`plants.toml:131-134`), so it is walked and samples nothing, and
the grader cannot see a mis-split of it until one of its rows carries a token.

The grader looks no row up by id, so a fixture missing a row cannot raise `StopIteration` past the
loop, which catches only `Stop`, `OSError`, `KeyError` and `ValueError` (`:1107`). A fixture with
no row resolving under one root reads the named `unsampled` red instead. That is the round-1 spec
audit's L5 (id 14). The grader catches `LookupError` itself for the same reason. `build_repo`
(`:986-995`) gives the scratch target a `.git` and no receipt, so `resolve_kit_dir` answers from its
probe, which is the target's prefix or nothing (`govkit.py:265-270`).

Measured at rev-2 with S2 staged in a scratch tree made by `git archive a3ad798cf tools` and
committed, its `check_graders` taking about 2 s a run:

| Staged | `plant-root` row |
|---|---|
| S2 as written | `upgrade-walk: grader · plant-root · ok`, and the list `[]` |
| `:140` in its `b634d60e5` form, one root for every kind | `RED · the plant row engine-edit read moved/memory-tree/README.md, not under tools/`, then the other plant and arm rows, then `no fixture row resolved under tools/, so that root went unsampled` |
| `:140` resolving every kind against `read_target_prefix()` | `RED · the gov_plant row withdraw-one read tools/hooks/kit.toml, not under moved/`, then `withdraw-one-source`, then `no fixture row resolved under moved/, so that root went unsampled` |
| `:140` sending `kind in ("gov_plant", "arm")` to gov's tool root | `RED · the arm row held-shim read moved/check-kit-versions.sh, not under tools/`, then its `to` and the `missing-plant` arm's plant |
| `derive_policy_adopter` resolving at `t / gk.derive_tool_root(t)` | `RED · the policy adopter read LookupError: no policy kit holding adopt-policy.sh` |

Every other grader row read `ok` in each. Rev-1's grader sampled only `engine-edit`, `withdraw-one`
and the policy adopter, so it reads no arm row and passes the fourth row's break, as the audit's M4
reasons. That form was not staged at rev-2.

### S3: the floor stub's fallback

After `check` (`selftest.py:279-284`), shaped as `measure_legs.set_environ`
(`tools/run-gates/measure_legs.py:2046-2057`), which this copy-installed kit cannot import across
kits. It also unsets, because `[dSP-91 L2]` needs `GOV_BASH` absent:

```python
@contextlib.contextmanager
def set_environ(values: dict):
    """TOOL-dSafePassage-91 S3: `values` set in this process's environment for the block, a `None`
    unsetting its key, and the previous state restored after. Shaped as `measure_legs.set_environ`,
    which this copy-installed kit cannot import across kits."""
    held = {k: os.environ.get(k) for k in values}
    for k, v in values.items():
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v
    try:
        yield
    finally:
        for k, v in held.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
```

`contextlib` is imported at `selftest.py:19`. The three hand-typed copies of this loop in
`check_step_isolation` take it. At `:3766-3775` the hold is `with set_environ(parent):` around the
`build_step_env` call; `parent` stays, because `run_fixture` reads it at `:3783`. At `:4409-4418`
it is `with set_environ({"PATH": str(fakes) + os.pathsep + os.environ.get("PATH", ""),
"GOV_PYTHON": sys.executable}):`. The third copy, at `:4437-4446`, goes with `[dSP-87 AC5]` into
`check_floor_bash`. That is the round-1 spec audit's L3 (id 7).

The block at `:4422-4448`, which is the end of `check_step_isolation`, becomes one call,
`check_floor_bash(tmp)`, and the block moves into that new module function, placed before
`check_step_gate_fixture` (`:4451`):

```python
def check_floor_bash(tmp: pathlib.Path) -> None:
    """TOOL-dSafePassage-87 AC5 and TOOL-dSafePassage-91 S3, the floor row's witness on one PATH whose
    every bash is unusable: with GOV_BASH the parent's bash it holds, and with GOV_BASH unset the
    floor stub reaches its fallback to bare `bash`. Called from `check_step_isolation`."""
    us = govkit_module().upgrade_steps
    floor_row = next(r for r in us.read_steps(GOV_ROOT, None, None) if r.id == "lib/python-floor-3.15")
    # (:4422-4436 as they stand: the TOOL-dSafePassage-87 S4 comment, bash87, fake87,
    #  test_launcher87 and keep87)
    path87 = os.pathsep.join([str(fake87)] + keep87)
    with set_environ({"PATH": path87, "GOV_BASH": bash87, "GOV_PYTHON": sys.executable}):
        got = us.run_step_isolated(floor_row, "witness", GOV_ROOT, GOV_ROOT)
    check("[dSP-87 AC5] the floor row's witness, PATH's bash unusable and GOV_BASH the parent's bash, is ok",
          got["verdict"] == "ok" and got["rc"] == 0, str(got))

    # TOOL-dSafePassage-91: the same PATH with GOV_BASH unset, so no bash resolves and the stub falls
    # back to bare `bash` (python_floor.py:36) rather than dying on resolve_bash's Refusal. What bare
    # `bash` resolves to (on Windows the loader's System32 WSL launcher, elsewhere PATH or nothing), and
    # so the rc, is the node's, so only the tail is graded: it names bash or the floor script, and it
    # carries neither the stub's own early exit nor the Refusal.
    with set_environ({"PATH": path87, "GOV_BASH": None, "GOV_PYTHON": sys.executable}):
        got = us.run_step_isolated(floor_row, "witness", GOV_ROOT, GOV_ROOT)
    tail = got["tail"]
    check("[dSP-91 L2] the floor row's witness, no bash resolving and GOV_BASH unset, falls back to bare bash",
          ("bash" in tail or "python-floor.sh" in tail) and "python_floor.py:" not in tail
          and "upgrade_steps.Refusal" not in tail and "Set GOV_BASH" not in tail, str(got))
```

`floor_row` is read as `:4403` reads it, because `[dSP-75]` still reads that one in
`check_step_isolation`. The function is its own so that AC5 can call it the way
TOOL-dSafePassage-71's criteria call `selftest.build_staged_copy`, without running the suite. That is
the round-1 spec audit's M2 (id 2): rev-1's AC5 ran only the witness, which reads the same before
the build as after it.

`resolve_bash` refuses with `Set GOV_BASH.` when no `PATH` candidate runs (`upgrade_steps.py:421-422`),
and `resolve_shell_argv` falls back to the bare argv on that `Refusal` (`:437-440`). The witness's
`tail` is its stderr (`upgrade_steps.py:1766`, `:1805`).

The positive half is the round-1 spec audit's M3 (id 11). Rev-1's check asserted only absences, so
it read green on any failure that stops before `python_floor.py:36`. The stub's own early exit
writes `python_floor.py: <the LookupError>` and returns 2 (`python_floor.py:31-35`), and that tail
carries neither absence. The check now requires the tail to name `bash` or the floor script
`python-floor.sh` (`FLOOR_SCRIPT`, `python_floor.py:22`), and refuses `python_floor.py:`. The
literal is spelled in the check because the stub's constant sits in a step program the selftest
does not import.

Measured at rev-2 by AC5's command, in the scratch tree of §4 "S2" with S3 staged and committed,
about 3 s a run:

| Staged | Lines |
|---|---|
| S3 as written | `ok   [dSP-87 AC5] ...`, `ok   [dSP-91 L2] ...`, and the list `[]` |
| `python_floor.py:36` as `[steps.resolve_bash(), (kit / FLOOR_SCRIPT).as_posix(), *argv]` | `ok   [dSP-87 AC5] ...`, then `FAIL [dSP-91 L2] ...` with `upgrade_steps.Refusal: govkit: no usable bash on PATH that shares this filesystem` in its detail |
| `python_floor.py:32` resolving `"no-such-floor.sh"` in place of `FLOOR_SCRIPT` | `FAIL [dSP-87 AC5] ...` and `FAIL [dSP-91 L2] ...`, each tail `python_floor.py: no lib kit holding no-such-floor.sh in this install: ...`, rc 2 |

The third row's tail carries neither `upgrade_steps.Refusal` nor `Set GOV_BASH`, so rev-1's
absence-only check reads it `ok`. That follows from the measured tail; rev-1's check was not staged.

`l2_probe.py` runs the same witness outside the selftest. It is a measurement of the stub, not a
criterion: it reads the same before the build as after it. Its one argument is a gov root whose
`tools/govkit` is the engine under test:

```python
import os, pathlib, sys, tempfile
gov = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(gov / "tools" / "govkit"))
import upgrade_steps as us
floor_row = next(r for r in us.read_steps(gov, None, None) if r.id == "lib/python-floor-3.15")
fake = pathlib.Path(tempfile.mkdtemp(prefix="l2-"))
for nm in ("bash", "bash.exe"):
    (fake / nm).write_bytes(b"not a program\n"); (fake / nm).chmod(0o755)
def launcher(d): return any(s in d.replace("\\", "/").lower() for s in ("/system32", "/windowsapps"))
keep = [d for d in os.environ.get("PATH", "").split(os.pathsep) if d and (launcher(d) or not any(
    os.path.isfile(os.path.join(d, n)) for n in ("bash", "bash.exe")))]
os.environ.pop("GOV_BASH", None)
os.environ.update(PATH=os.pathsep.join([str(fake)] + keep), GOV_PYTHON=sys.executable)
got = us.run_step_isolated(floor_row, "witness", gov, gov)
t = got["tail"]
print("verdict", got["verdict"], "rc", got["rc"], "| Refusal in tail:", "upgrade_steps.Refusal" in t,
      "| Set GOV_BASH in tail:", "Set GOV_BASH" in t)
```

Measured over a scratch tree made by `git archive cbaaeebeb tools` and committed:
`verdict failed rc 127 | Refusal in tail: False | Set GOV_BASH in tail: False`, the tail being the
WSL launcher's `No such file or directory` for the floor script. With `python_floor.py:36` staged
back to `[steps.resolve_bash(), (kit / FLOOR_SCRIPT).as_posix(), *argv]`, it printed
`verdict failed rc 1 | Refusal in tail: True | Set GOV_BASH in tail: True`.

### Inventory

Minted: in `upgrade_walk.py`, the constant `FIXTURE_FILES`, the function `derive_policy_adopter`,
its nested grader `check_grade_plant_root` with its nested generator `extract_paths`, and the grader
row `plant-root`. In `selftest.py`, the context manager `set_environ`, the function
`check_floor_bash` with its locals `path87` and `tail`, the check labels `[dSP-91 L1]` and
`[dSP-91 L2]`, the name `_kit88`, and the locals `_g91`, `_t91`, `_ap91`, `_up91`, `_ord91` and
`_rs91`. The scratch directories `rn-inplace-held-gov`, `rn-inplace-held-t` and `plant-root-target`.
Each function's leading token is a verb of `.lexicon.conf`'s table: `derive`, `check`, `extract`
and `set`. No `Refusal` site, flag, conf key, gate leg or receipt field.

### Migration

None.

### Rollout

Live at landing, at order 16, after TOOL-dSafePassage-90.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/upgrade_walk.py`

### Alternatives rejected

- **L1: dedupe `restored` at the order's render.** The snapshot is where the doubled path is born,
  and the restore loop would still run the path twice.
- **M4: the finder's fix.** The skeptic rejected it, and the corrected fix is S2.
- **M4: patch the fixture's `deploy.toml` prefix apart instead of the tool root.** The grader would
  then edit a tracked fixture file, and `read_target_prefix` reads it from disk.
- **L2: assert no traceback at all, or an rc.** The skeptic rejected both. On a node where no bare
  `bash` resolves at all, the stub's bare-`bash` spawn raises a `FileNotFoundError` traceback, which
  is the fallback working. On Windows the loader resolves bare `bash` to the System32 WSL launcher
  before `PATH` (`upgrade_steps.py:372-376`), so node a read rc `127` and no traceback.
- **M4: sample one named row per kind.** A fixed sample misses the next row and the next kind;
  walking every row of every `FIXTURE_FILES` kind does not, and costs the same one read per kind.
- **M2: AC5 as the `[dSP-91 L2]` line in the `govkit selftest` output.** That is the skeptic's
  wording. A criterion is never a self-test suite, so AC5 calls `check_floor_bash` alone, and the
  suite's own red and green ride §7's New arm lines.
- **L3: keep the inline copy and say why in §10.** The audit's alternative. The helper is ten lines,
  in the one file that types the loop, and it leaves one copy where there were three.

## 5. Production-readiness checklist

- security: no write path, spawn or surface is added. S1 narrows what the rollback touches to the
  paths a row occupies. S2 and S3 are checks.
- perf / scale: one more `update` fixture in the selftest, about 6 s by its probe, and one more
  grader, which shares `check_graders`' scratch directory.
- error / empty / loading states: the grader returns a red string on a missing policy adopter and on
  a root no fixture row resolves under, as the other graders return theirs, rather than raising past
  the loop. It looks no row up with `next`, so a missing fixture row cannot raise `StopIteration`.
- observability: the update-rollback order names an in-place row once.
- risks: S2's patch of `derive_tool_root` is restored in a `finally`, so a red grader cannot leak the
  patched root into the walk that follows in the same process.
- testing: §7's four New arms, and AC1 to AC7.
- migration: none.
- user docs: none. No page under `help/` describes the update-rollback order's lines, the walk's
  graders or the floor stub's fallback, so no page sentence changes.

## 6. Acceptance criteria

- **AC1** — When §4 "S1's probe", saved under the temp root as `l1_probe.py`, runs with `python` from the repository root, it
  prints
  `in place, sibling refused: update exit 1 | occupied refused: True | restored lines for keep.txt: 1 | bytes: ['one', 'two']`.
  Red when: the snapshot appends a renamed row's destination unconditionally, so it prints
  `restored lines for keep.txt: 2`, as at `cbaaeebeb`.
  cost: about 6 s.
  fixture: a scratch gov and target under the temp root. The tree holds none today.
- **AC2** — When `git grep -n -F "[dSP-91 L1]" -- tools/govkit/selftest.py` runs, it prints one
  line, inside the `DEPL-dCarriedReceipt-11` block; and `git grep -n -F "_kit88" -- tools/govkit/selftest.py`
  prints at least three lines, its binding and its two fixtures.
  Red when: the arm is absent, so the first grep prints nothing, as at `cbaaeebeb`.
- **AC3** — When
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import upgrade_walk as u; print(u.check_graders())"`
  runs from the repository root, it prints `upgrade-walk: grader · plant-root · ok`, and its last
  line is `[]`.
  Red when: `read_fixture_rows` resolves every kind against one root, resolves every kind against
  the target's prefix, or sends the `arm` kind to gov's tool root, or `derive_policy_adopter`
  resolves at gov's tool root, so it prints `grader · plant-root · RED ·` and names the rows or the
  adopter (§4 "S2"). At `a3ad798cf` no `plant-root` row prints.
  cost: about 2 s, measured at rev-2.
- **AC4** — When `git grep -n -F "derive_policy_adopter(t)" -- tools/govkit/upgrade_walk.py` runs, it
  prints three lines: the `def` beside `derive_release_engine`, the call in `build_release_tree` and
  the call in `check_grade_plant_root`. `git grep -n -F 'resolve_kit_dir("policy", adopter' -- tools/govkit/upgrade_walk.py`
  prints nothing. `git grep -n -F "FIXTURE_FILES" -- tools/govkit/upgrade_walk.py` prints three
  lines: the binding, `read_fixture_rows` and the grader. And
  `git grep -n -F "plant-root split" -- tools/govkit/upgrade_walk.py` prints one line, in
  `check_graders`' docstring.
  Red when: the adopter's path stays inline in `build_release_tree`, where no grader reaches it, so
  the second grep prints the line at `:248`; or the docstring is not updated, so the fourth prints
  nothing, as at `a3ad798cf`.
  figure: each count is PINNED, measured at rev-2 over S2 staged in a scratch tree.
- **AC5** — When
  `python -c "import pathlib, sys, tempfile; sys.path.insert(0, 'tools/govkit'); import selftest as s; s.check_floor_bash(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`
  runs from the repository root, it prints `ok   [dSP-87 AC5]`, then `ok   [dSP-91 L2]`, and its last
  line is `[]`.
  Red when: `selftest` holds no `check_floor_bash`, so it raises `AttributeError`, as at
  `a3ad798cf`; or the check is built but its fallback is dead, as AC6 stages.
  cost: about 3 s, measured at rev-2.
  fixture: a node whose `PATH` holds a bash, so the check's filtered `PATH` holds none that runs, as
  `[dSP-87 AC5]` already needs.
- **AC6** — When `tools/govkit/steps/python_floor.py:36` is staged to
  `[steps.resolve_bash(), (kit / FLOOR_SCRIPT).as_posix(), *argv]` and committed, AC5's command
  prints `FAIL [dSP-91 L2]` with `upgrade_steps.Refusal` in its detail. When `:32` is staged to
  resolve `"no-such-floor.sh"` in place of `FLOOR_SCRIPT` and committed, it prints
  `FAIL [dSP-91 L2]` with `python_floor.py:` in its detail, and `FAIL [dSP-87 AC5]`.
  Red when: the check asserts only absences, so the `:32` stage, whose tail carries neither
  absence, reads `ok   [dSP-91 L2]`.
  fixture: each stage edits a tracked file, so the build runs it in a scratch tree made by
  `git archive HEAD tools` and committed, as rev-2 measured it, and records the two FAIL lines. The
  tree holds no such scratch tree today.
- **AC7** — When `git grep -n -F "[dSP-91 L2]" -- tools/govkit/selftest.py` runs, it prints one line,
  inside `check_floor_bash`; and `git grep -n -F "os.environ.get(k) for k in" -- tools/govkit/selftest.py`
  prints one line, inside `set_environ`.
  Red when: the arm is absent, so the first grep prints nothing; or the save-and-restore loop is
  typed again, so the second prints more than one line. At `a3ad798cf` they print nothing and three
  lines.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the `[dSP-91 L1]` check in the `DEPL-dCarriedReceipt-11` block, staged red by the snapshot appending a renamed row's destination unconditionally, which restores the in-place row twice · none
New arm: tools/govkit/upgrade_walk.py · covers AC3 · the `plant-root` grader of `check_graders`, staged red by `read_fixture_rows` in its `b634d60e5` one-root form, by every kind resolved at the target's prefix, by the `arm` kind sent to gov's tool root and, separately, by `derive_policy_adopter` resolving at gov's tool root · none
New arm: tools/govkit/selftest.py · covers AC5 AC6 · the `[dSP-91 L2]` check of `check_floor_bash`, staged red by `python_floor.py:36` calling `steps.resolve_bash()` directly, whose `Refusal` reaches the tail, and separately by `:32` resolving a script no lib kit holds, whose early exit reaches it · none
New arm: tools/govkit/selftest.py · covers AC5 · the `[dSP-87 AC5]` check, moved from `check_step_isolation` into `check_floor_bash`, staged red by `python_floor.py:32` resolving a script no lib kit holds, so the witness exits 2 · none

The `{prefix}/govkit/` legs and `policy fixtures` are the guard join's for the three files; their
other guards are broad. `upgrade-walk` runs `check_graders` first on every invocation
(`upgrade_walk.py:1140`), so S2's grader rides that leg. No refusal call site is added, so
`govkit refusal join`'s pin does not move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-90-1-spec-writer.md` and its
  brief `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-90-spec-brief.md`.
  It batches the round-3 closing diff review's remaining minors,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md`
  L1 (id 4), M4 (id 6) and L2 (id 7), at the skeptic's fixes. M1 (id 1), M2 (id 2) and M3 (id 5)
  moved to TOOL-dSafePassage-90, whose mechanism closes them. Each fix and each staged break was
  measured in a scratch copy of the engine.
- rev-2 · 2026-10-29 · §2 S2 S3 · §3 Edges · §4 S2, S3, Inventory, Alternatives rejected · §5 ·
  AC1 · AC3 · AC4 · AC5 · AC6 · AC7 · §7 · §10 · folded the round-1 spec audit,
  `memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-90-91-spec-audit-round1.md`,
  from its brief
  `memory/builds/dSafePassage/prompts/2026-10-29-prompt-TOOL-dSafePassage-90-audit-fold-brief.md`.
  M1 (ids 1, 4, 8, 10), at the skeptic's corrected fix: AC4's first grep prints three lines, the
  `def` included. M2 (id 2): AC5 calls the new `check_floor_bash` and is red before the build, and
  AC6 stages its reds; `l2_probe.py` stays a §4 measurement. M3 (id 11): the check gains a positive
  marker and refuses the stub's early exit, with that exit staged red. M4 (id 12): the grader walks
  every row of every kind in the new `FIXTURE_FILES`, and the arm-kind break is staged red. L1 (ids
  3, 5), this unit's half: the Edges note names the one block shared with TOOL-dSafePassage-90. L2
  (id 6): the check's comment and the L2 alternative name the Windows loader's order. L3 (id 7): one
  `set_environ` in `selftest.py` holds all four uses. L4 (id 9): the `check_graders` docstring names
  the grader. L5 (id 14): the grader looks no row up by `next`, and an unsampled root is a named red.
  S2 and S3 were staged in a scratch tree from `a3ad798cf` and measured, and every cited line was
  re-verified there. AC1 names its probe by its bare filename, so every backticked path in §6 is
  tracked.

## 10. Reuse audit

S1 changes the pre-write snapshot of `_cmd_update` (`tools/govkit/govkit.py:10745-10747`) in place,
and its arm extends the `DEPL-dCarriedReceipt-11` block of `tools/govkit/selftest.py` through that
block's factory, `build_rename_gov` (`selftest.py:12209`), with the kit text bound once rather than
copied. S2 extends `check_graders` (`tools/govkit/upgrade_walk.py:976`), whose `build_repo` it
reuses, and its new function reads the existing `read_target_prefix` and `resolve_kit_dir` beside
`derive_release_engine`. S3 moves `[dSP-87 AC5]` out of `check_step_isolation` into `check_floor_bash`, whose new check
reuses that check's fake `PATH`. Its `set_environ` takes the shape of
`measure_legs.set_environ` (`tools/run-gates/measure_legs.py:2046`), which a copy-installed kit
cannot import, and takes the three hand-typed copies of the loop in `selftest.py`. `python tools/codebase-map/reuse_lookup.py "a grader patches gov's tool root apart from the target prefix and checks each fixture row resolves against its own root"`
ranked `resolve_kit_dir`, `repo_root` and `resolve_prefix_token` as seams. S2 calls the first
through `derive_policy_adopter` and reaches the other two through `read_fixture_rows`, unchanged. The
recall probe ranked the round-3 review's M4 item and TOOL-dSafePassage-87's S7, the split S2 grades.

Recall terms used: `python tools/memory-recall/query.py "the walk's plants resolve against the target prefix and gov plants against gov's tool root, and a grader holds the split" --terms "read_target_prefix derive_tool_root gov_plant plant-root grader check_graders policy adopter in-place snapshot restored twice python_floor GOV_BASH resolve_shell_argv"`
