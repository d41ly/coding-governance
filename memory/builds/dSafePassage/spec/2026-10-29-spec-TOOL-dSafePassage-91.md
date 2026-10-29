# TOOL-dSafePassage-91 — the round-3 closing review's three remaining minors: the in-place row's one snapshot path, a grader for the walk's two roots, and an arm for the floor stub's bash fallback

**Status:** DEFERRED · rev-1 · 2026-10-29 · node a · Tier-2 · base cbaaeebe · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-prompt-TOOL-dSafePassage-90-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-90-spec-brief.md) | research | TOOL-dSafePassage-90 |
| [2026-10-29-prompt-TOOL-dSafePassage-91-build-brief.md](../prompts/2026-10-29-prompt-TOOL-dSafePassage-91-build-brief.md) | journal | — |

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
  expression sits inline now. `check_graders` (`:976`) gains a `plant-root` grader. With
  `derive_tool_root` patched to answer `moved`, it requires the `engine-edit` plant under
  `read_target_prefix()`, the `withdraw-one` gov_plant under `moved`, and the policy adopter under
  the target's prefix. §4 "S2". Observed by AC3 and AC4.
- **S3** — L2 (id 7), the floor stub's fallback to bare `bash` has an arm. `check_step_isolation` of
  `tools/govkit/selftest.py` gains a `[dSP-91 L2]` check after `[dSP-87 AC5]` (`:4447-4448`). It runs
  the floor row's witness on the same unusable-bash `PATH` with `GOV_BASH` unset. It requires only
  that the witness's tail carry neither `upgrade_steps.Refusal` nor `Set GOV_BASH`.
  `tools/govkit/steps/python_floor.py` is not edited. §4 "S3". Observed by AC5 and AC6.

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
- Asserting an rc in S3's check. What bare `bash` finds on the check's `PATH` is the node's: measured,
  the WSL launcher's `127` on node a (§4 "S3").

### Edges

- **consumes-from** `TOOL-dSafePassage-90` — its S1 edits the same `renamed` write arm and its
  `[dSP-90]` check is the one S1's check sits after; without it S1's check has no anchor in the block

## 4. Design

Every cited line holds at `cbaaeebeb`, the build head with TOOL-dSafePassage-86, -87, -89 and -88
landed. TOOL-dSafePassage-90 edits `govkit.py` and `selftest.py` before this unit builds, so the
builder re-reads each cited line by content before editing. Each measurement below was taken on
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

In `check_graders`, after `check_grade_shim_root` (`:1086-1097`):

```python
    def check_grade_plant_root() -> str:
        gk, pfx = load_engine()[2], read_target_prefix()
        t = build_repo("plant-root-target", {f"{pfx}/policy/adopt-policy.sh": ""})
        real = gk.derive_tool_root
        gk.derive_tool_root = lambda root: "moved"
        try:
            ee = next(r["path"] for r in read_plant_rows() if r["id"] == "engine-edit")
            wo = next(r["path"] for r in read_fixture_rows("gov_plant") if r["id"] == "withdraw-one")
            try:
                pol = derive_policy_adopter(t)
            except LookupError as e:
                pol = f"LookupError: {e}"
        finally:
            gk.derive_tool_root = real
        bad = [] if ee.startswith(pfx + "/") else [f"the engine-edit plant read {ee}, not under {pfx}/"]
        bad += [] if wo.startswith("moved/") else [f"the withdraw-one gov_plant read {wo}, not under moved/"]
        bad += [] if isinstance(pol, pathlib.Path) and t / pfx in pol.parents else [
            f"the policy adopter read {pol}, not under the target's {pfx}"]
        return "; ".join(bad)
```

Its row joins the grader tuple (`:1101-1104`) as `("plant-root", check_grade_plant_root)`.
`read_fixture_rows` reads `gk.derive_tool_root` off the module that `load_engine` returns
(`:138-140`), so the patch reaches it. The grader catches `LookupError` itself, because the grader
loop catches only `Stop`, `OSError`, `KeyError` and `ValueError` (`:1107`). `build_repo` (`:986-995`)
gives the scratch target a `.git` and no receipt, so `resolve_kit_dir` answers from its probe, which
is the target's prefix or nothing (`govkit.py:265-270`).

Measured with S2 staged in a scratch tree made by `git archive cbaaeebeb tools`, its
`check_graders` taking about 5 s:

| Staged | `plant-root` row |
|---|---|
| S2 as written | `upgrade-walk: grader · plant-root · ok`, and the list `[]` |
| `:140` in its `b634d60e5` form, one root for every kind | `RED · the engine-edit plant read moved/memory-tree/README.md, not under tools/` |
| `:140` resolving every kind against `read_target_prefix()` | `RED · the withdraw-one gov_plant read tools/hooks/kit.toml, not under moved/` |
| `derive_policy_adopter` resolving at `t / gk.derive_tool_root(t)` | `RED · the policy adopter read LookupError: no policy kit holding adopt-policy.sh` |

Every other grader row read `ok` in each.

### S3: the floor stub's fallback

After `[dSP-87 AC5]` (`selftest.py:4447-4448`), reusing that check's `fake87`, `keep87` and
`floor_row`:

```python
    # TOOL-dSafePassage-91: the same PATH with GOV_BASH unset, so no bash resolves and the stub falls
    # back to bare `bash` (python_floor.py:36) rather than dying on resolve_bash's Refusal. Only the
    # tail is graded: what bare `bash` finds on this PATH, and so the rc, is the node's.
    held = {k: os.environ.get(k) for k in ("PATH", "GOV_PYTHON", "GOV_BASH")}
    os.environ.update(PATH=os.pathsep.join([str(fake87)] + keep87), GOV_PYTHON=sys.executable)
    os.environ.pop("GOV_BASH", None)
    try:
        got = us.run_step_isolated(floor_row, "witness", GOV_ROOT, GOV_ROOT)
    finally:
        for k, v in held.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    check("[dSP-91 L2] the floor row's witness, no bash resolving and GOV_BASH unset, falls back to bare bash",
          "upgrade_steps.Refusal" not in got["tail"] and "Set GOV_BASH" not in got["tail"], str(got))
```

`resolve_bash` refuses with `Set GOV_BASH.` when no `PATH` candidate runs (`upgrade_steps.py:421-422`),
and `resolve_shell_argv` falls back to the bare argv on that `Refusal` (`:437-440`). The witness's
`tail` is its stderr (`upgrade_steps.py:1766`, `:1805`).

`l2_probe.py` runs the same witness outside the selftest. Its one argument is a gov root whose
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

Minted: the function `derive_policy_adopter` in `upgrade_walk.py`, its nested grader
`check_grade_plant_root` and the grader row `plant-root`, the check labels `[dSP-91 L1]` and
`[dSP-91 L2]`, the selftest name `_kit88`, the locals `_g91`, `_t91`, `_ap91`, `_up91`, `_ord91` and
`_rs91`, and the scratch directories `rn-inplace-held-gov`, `rn-inplace-held-t` and
`plant-root-target`. No `Refusal` site, flag, conf key, gate leg or receipt field.

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
- **L2: assert no traceback at all, or an rc.** The skeptic rejected both. Bare `bash` on a node
  with none on `PATH` raises a `FileNotFoundError` traceback in the stub, which is the fallback
  working.

## 5. Production-readiness checklist

- security: no write path, spawn or surface is added. S1 narrows what the rollback touches to the
  paths a row occupies. S2 and S3 are checks.
- perf / scale: one more `update` fixture in the selftest, about 6 s by its probe, and one more
  grader, which shares `check_graders`' scratch directory.
- error / empty / loading states: the grader returns a red string on a missing policy adopter, as the
  other graders return theirs, rather than raising past the loop.
- observability: the update-rollback order names an in-place row once.
- risks: S2's patch of `derive_tool_root` is restored in a `finally`, so a red grader cannot leak the
  patched root into the walk that follows in the same process.
- testing: §7's three New arms, and AC1 to AC6.
- migration: none.
- user docs: none. No page under `help/` describes the update-rollback order's lines, the walk's
  graders or the floor stub's fallback, so no page sentence changes.

## 6. Acceptance criteria

- **AC1** — When §4 "S1's probe", `python <scratch>/l1_probe.py`, runs from the repository root, it
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
  Red when: `read_fixture_rows` resolves every kind against one root, or `derive_policy_adopter`
  resolves at gov's tool root, so it prints `grader · plant-root · RED ·` and names the plant or the
  adopter (§4 "S2"). At `cbaaeebeb` no `plant-root` row prints.
  cost: about 5 s.
- **AC4** — When `git grep -n -F "derive_policy_adopter(t)" -- tools/govkit/upgrade_walk.py` runs, it
  prints two lines, one in `build_release_tree` and one in `check_grade_plant_root`; and
  `git grep -n -F 'resolve_kit_dir("policy", adopter' -- tools/govkit/upgrade_walk.py` prints nothing.
  Red when: the adopter's path stays inline in `build_release_tree`, where no grader reaches it, so
  the second grep prints the line at `:248`, as at `cbaaeebeb`.
- **AC5** — When §4 "S3"'s `python <scratch>/l2_probe.py <scratch>/gov` runs from the repository root,
  over a committed `git archive` of this tree's `tools`, it prints
  `Refusal in tail: False | Set GOV_BASH in tail: False`.
  Red when: `python_floor.py:36` calls `steps.resolve_bash()` directly, so it prints
  `rc 1 | Refusal in tail: True | Set GOV_BASH in tail: True`, as measured with that line staged.
  fixture: a scratch gov tree under the temp root, and a node whose `PATH` holds a bash, so the
  probe's filtered `PATH` holds none that runs. The tree holds none today.
- **AC6** — When `git grep -n -F "[dSP-91 L2]" -- tools/govkit/selftest.py` runs, it prints one line,
  inside `check_step_isolation`.
  Red when: the arm is absent, so it prints nothing, as at `cbaaeebeb`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the `[dSP-91 L1]` check in the `DEPL-dCarriedReceipt-11` block, staged red by the snapshot appending a renamed row's destination unconditionally, which restores the in-place row twice · none
New arm: tools/govkit/upgrade_walk.py · covers AC3 · the `plant-root` grader of `check_graders`, staged red by `read_fixture_rows` in its `b634d60e5` one-root form and, separately, by `derive_policy_adopter` resolving at gov's tool root · none
New arm: tools/govkit/selftest.py · covers AC5 · the `[dSP-91 L2]` check of `check_step_isolation`, staged red by `python_floor.py:36` calling `steps.resolve_bash()` directly, whose `Refusal` reaches the tail · none

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

## 10. Reuse audit

S1 changes the pre-write snapshot of `_cmd_update` (`tools/govkit/govkit.py:10745-10747`) in place,
and its arm extends the `DEPL-dCarriedReceipt-11` block of `tools/govkit/selftest.py` through that
block's factory, `build_rename_gov` (`selftest.py:12209`), with the kit text bound once rather than
copied. S2 extends `check_graders` (`tools/govkit/upgrade_walk.py:976`), whose `build_repo` it
reuses, and its new function reads the existing `read_target_prefix` and `resolve_kit_dir` beside
`derive_release_engine`. S3 extends `check_step_isolation` beside `[dSP-87 AC5]`, reusing its fake
`PATH`. `python tools/codebase-map/reuse_lookup.py "a grader patches gov's tool root apart from the target prefix and checks each fixture row resolves against its own root"`
ranked `resolve_kit_dir`, `repo_root` and `resolve_prefix_token` as seams. S2 calls the first
through `derive_policy_adopter` and reaches the other two through `read_fixture_rows`, unchanged. The
recall probe ranked the round-3 review's M4 item and TOOL-dSafePassage-87's S7, the split S2 grades.

Recall terms used: `python tools/memory-recall/query.py "the walk's plants resolve against the target prefix and gov plants against gov's tool root, and a grader holds the split" --terms "read_target_prefix derive_tool_root gov_plant plant-root grader check_graders policy adopter in-place snapshot restored twice python_floor GOV_BASH resolve_shell_argv"`
