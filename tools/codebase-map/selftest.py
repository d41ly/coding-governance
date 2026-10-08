"""codebase-map kit self-test — exercises the pure engine with fixtures (stdlib only).

    python <kit>/selftest.py        # exit 0 = the kit's contract holds

These are the red-path proofs: an unclaimed key, a stale claim, a stale/lazy baseline line,
and every malformed-dossier class must FAIL LOUD; multi-claim, case-sensitivity, and
backslash normalization must behave identically on every platform.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


def derive_install_prefix() -> str:
    """The install prefix WITH its trailing slash, derived from where this file sits and empty at a
    root install. Every fixture and host path the self-test builds is spelled through it, never
    through a literal prefix (TOOL-aRepatriatedFork-28)."""
    import pathlib
    here = pathlib.Path(os.path.abspath(__file__)).parent
    for anc in here.parents:
        if (anc / ".git").exists():
            rel = here.parent.relative_to(anc).as_posix()
            return "" if rel == "." else rel + "/"
    raise SystemExit(f"{pathlib.Path(__file__).name}: not inside a git repository, so there is no "
                     "install prefix to derive")


PFX = derive_install_prefix()
# TOOL-aRepatriatedFork-46: this kit's own directory is named by the NAME it has in this install.
KIT_NAME = Path(os.path.abspath(__file__)).parent.name


# `abspath`, NOT `resolve()`: this insert decides which path string `map_lib.__file__` carries,
# and map_lib.kit_dir()/the gate template both use abspath. Under a junctioned kit dir resolve()
# yields the LINK TARGET, so this entrypoint would stamp one prefix into the byte-compared
# artifacts while the gate re-renders another — a permanently STALE gate whose own printed
# remedy re-writes the wrong spelling and never converges (measured).
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent))

import map_lib as m  # noqa: E402
import reuse_lookup as rl  # noqa: E402
import map_diff as md  # noqa: E402
import check_gate_coverage as cg  # noqa: E402

IDS = ("flags", "routes")
INV = {"flags": ["a_flag", "b_flag"], "routes": ["api/x/route.ts"]}
EMPTY_BASE: dict[str, tuple[str, ...]] = {k: () for k in IDS}

DOSSIER = """# x
```toml
feature = "x"
title = "X"
status = "shipped"
streams = ["core"]
decisions = ["REC-someSlug-1"]

[claims]
flags = ["a_flag"]
routes = []

[paths]
globs = ["src/x/**"]
```
"""


def claims(**over):
    return {k: () for k in IDS} | over


class Skipped(Exception):
    """An arm whose GUARD is unmet. TOOL-dRetiredFork-5, from adopter ic's ABL-aFerriedToolkit-4.

    It is an exception and not a `return` because `check` cannot tell a return from a pass: the
    guarded arms printed an honest `NOT a pass.` and returned, and the next line stamped them `ok`.
    A skip that looks like a pass is indistinguishable from coverage, which is the class AGENTS.md
    section 7 names — and it was living inside this kit's own proof.
    """


#: How many guarded arms exist, and how many skipped this run. The refusal below is keyed on the
#: GUARDED pair and never on "every arm": 24 of the 26 are unconditional, so an all-skipped
#: predicate is unreachable and would be dead code the moment it landed — the could-not-fail shape
#: this unit exists to close.
SKIPPED: list = []
#: Every arm `check` ran, skipped ones included. DERIVED here rather than counted by hand in
#: main(), because a hand-kept total is one more thing that can disagree with the arms.
EXECUTED: list = []
#: The arms that CAN skip, recorded by the registration that runs them rather than by a list of
#: their names. The first cut of this hard-coded the two names, got one of them wrong, and the
#: refusal below never fired while reporting `1 of 2 guarded` — a predicate that did not match
#: its own population, which is the exact class this unit exists to close. Measured by unsetting
#: both guards: 2 skipped, refusal silent, exit 0.
GUARDED: list = []


def check_guarded(name, fn):
    """`check` for an arm with a guard: registers it so the vacuity refusal has a population."""
    GUARDED.append(name)
    return check(name, fn)


def check(name, fn):
    EXECUTED.append(name)
    try:
        fn()
        print(f"ok   {name}")
        return 0
    except Skipped as exc:
        SKIPPED.append(name)
        print(f"skipped {name}: {exc}")
        return 0
    except AssertionError as exc:
        print(f"FAIL {name}: {exc}")
        return 1


def expect_maperror(text_mutation, needle):
    try:
        m.parse_dossier(text_mutation, IDS, source="t")
    except m.MapError as exc:
        assert needle in str(exc), f"wrong error: {exc}"
        return
    raise AssertionError(f"parsed but should have failed ({needle!r})")


def test_install_prefix_resolution(tmp: Path):
    """S1/AC1: the root is resolved from the KIT DIR, so both install shapes work. resolve_root is
    a pure function of that dir precisely so this can drive every shape without relocating map_lib.

    The old rule was `the kit dir's parent`, which encodes the `<repo-root>/codebase-map/`
    convention. Under a prefix it lands one segment short and every derived path — MAP_ROOT, the
    dossiers, the reference scan — points at a tree with nothing in it."""
    import os

    def tree(name: str, prefix: str, *, conf: bool, git: str | None = "dir") -> Path:
        root = tmp / name
        kit = root / prefix / KIT_NAME if prefix else root / KIT_NAME
        kit.mkdir(parents=True)
        if git == "dir":
            (root / ".git").mkdir()
        elif git == "file":  # a worktree's .git is a FILE, not a directory
            (root / ".git").write_text("gitdir: ../../.git/worktrees/w\n", encoding="utf-8")
        if conf:
            (root / m.CONF_NAME).write_text("MAP_ROOT=memory/map\n", encoding="utf-8")
        return kit

    # --- the kit's own convention: <root>/codebase-map/ ---------------------------------------
    assert m.resolve_root(tree("a", "", conf=True)) == tmp / "a"
    # --- a PREFIXED install: <root>/<prefix>/codebase-map/ (the defect this closes) ---------------
    # A root install has no prefix of its own, and this arm needs one.
    fx_pfx = PFX or "scripts"
    kit_b = tree("b", fx_pfx, conf=True)
    assert m.resolve_root(kit_b) == tmp / "b"
    assert m.resolve_root(kit_b) != tmp / "b" / fx_pfx, "resolved to the OLD grandparent answer"
    # both roots hold the conf AND .git, so this also pins the ORDER: the conf is tested first,
    # else the boundary would break the walk at the root and hand back the kit dir's parent.
    # --- the walk is not capped at one segment ------------------------------------------------
    assert m.resolve_root(tree("c", "x/y", conf=True)) == tmp / "c"
    # --- no conf anywhere -> the grandparent convention, unchanged from the old rule -----------
    assert m.resolve_root(tree("d", PFX, conf=False)) == tmp / "d" / PFX
    assert m.resolve_root(tree("e", "", conf=False)) == tmp / "e"  # a root install is unaffected

    # --- the .git boundary: a conf in a PARENT tree is a DIFFERENT checkout --------------------
    # Worktrees are commonly kept inside the primary tree (this repo uses .claude/worktrees/<n>/),
    # so an unbounded walk would resolve a worktree's map into the primary tree's MAP_ROOT.
    primary = tmp / "primary"
    (primary / ".git").mkdir(parents=True)
    (primary / m.CONF_NAME).write_text("MAP_ROOT=memory/map\n", encoding="utf-8")
    wt_kit = tree("primary/.claude/worktrees/w", PFX, conf=False, git="file")
    wt = primary / ".claude" / "worktrees" / "w"
    assert m.resolve_root(wt_kit) == wt / PFX, "the walk escaped the worktree into the primary tree"
    (wt / m.CONF_NAME).write_text("MAP_ROOT=memory/map\n", encoding="utf-8")
    assert m.resolve_root(wt_kit) == wt  # the worktree's OWN conf resolves it

    # --- nearest conf wins (a repo vendored inside another adopting repo) ----------------------
    inner = tmp / "nest" / "inner"
    (inner / PFX / KIT_NAME).mkdir(parents=True)
    (tmp / "nest" / m.CONF_NAME).write_text("MAP_ROOT=outer\n", encoding="utf-8")
    (inner / m.CONF_NAME).write_text("MAP_ROOT=inner\n", encoding="utf-8")
    assert m.resolve_root(inner / PFX / KIT_NAME) == inner

    # --- repo_root: the override wins, otherwise resolve_root of the kit's OWN dir -------------
    os.environ["CODEBASE_MAP_ROOT"] = str(tmp / "a")
    try:
        assert m.repo_root() == tmp / "a"
    finally:
        del os.environ["CODEBASE_MAP_ROOT"]
    assert m.repo_root() == m.resolve_root(Path(os.path.abspath(m.__file__)).parent)


def test_require_adopted_root_refuses(tmp: Path):
    """AC2 (helper half): resolution answers WHERE the root is; this answers WHETHER anything was
    adopted there. The refusal must name the resolved root, the kit dir and where the root came
    from — 'wrong install prefix' and 'not adopted yet' are otherwise the same message."""
    import os

    bare = tmp / "bare"
    bare.mkdir()
    os.environ["CODEBASE_MAP_ROOT"] = str(bare)
    try:
        try:
            m.require_adopted_root()
            raise AssertionError("an unadopted root did not refuse")
        except m.MapError as exc:
            msg = str(exc)
            assert m.CONF_NAME in msg, msg
            assert "empty corpus" in msg, msg
            assert str(bare) in msg, msg              # the resolved root, by name
            assert "CODEBASE_MAP_ROOT" in msg, msg    # where that root came from
        (bare / m.CONF_NAME).write_text("MAP_ROOT=memory/map\n", encoding="utf-8")
        assert m.require_adopted_root() == bare       # adopted -> the root, no refusal
    finally:
        del os.environ["CODEBASE_MAP_ROOT"]


def test_clis_refuse_an_unadopted_root(tmp: Path):
    """AC2: BOTH CLIs refuse through their OWN main(). The helper being correct is not the same
    claim as the CLIs calling it — that gap is the whole defect, since neither imports the project
    layer that would otherwise fail closed for them. Each must exit 2 AND print no result: a
    `no seam fits` or an all-UNMAPPED digest on stdout is the confident-empty-answer this closes."""
    import contextlib
    import io
    import os
    import sys as _sys

    import map_diff as md

    bare = tmp / "bare"
    bare.mkdir()
    os.environ["CODEBASE_MAP_ROOT"] = str(bare)
    saved_argv = _sys.argv
    try:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = rl.main(["normalise a display name into a url slug"])
        assert rc == 2, f"reuse_lookup exited {rc}, not a refusal"
        assert "refused" in err.getvalue(), err.getvalue()
        assert out.getvalue() == "", f"a shortlist was printed anyway: {out.getvalue()!r}"

        _sys.argv = ["map_diff.py", "HEAD~1..HEAD"]
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = md.main()
        assert rc == 2, f"map_diff exited {rc}, not a refusal"
        assert "refused" in err.getvalue(), err.getvalue()
        assert out.getvalue() == "", f"a digest was printed anyway: {out.getvalue()!r}"

        # TOOL-aMendedFleet-37: an unadopted root would otherwise read every dossier fresh.
        _sys.argv = ["map_diff.py", "--stale-dossiers"]
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = md.main()
        assert rc == 2, f"map_diff --stale-dossiers exited {rc}, not a refusal"
        assert "refused" in err.getvalue(), err.getvalue()
        assert out.getvalue() == "", f"an answer was printed anyway: {out.getvalue()!r}"
    finally:
        _sys.argv = saved_argv
        del os.environ["CODEBASE_MAP_ROOT"]


def test_gate_template_finds_the_kit(tmp: Path):
    """S5/AC5: GATE_FILE points wherever the project's suite collects, which is independent of the
    kit's install prefix, so the gate's own walk must handle both. Driven in a SUBPROCESS: importing
    the template in-process would leave stub `map_lib`/`map_extractors` entries in sys.modules and
    shadow the real ones for every case after this one."""
    import os
    import subprocess
    import sys as _sys

    template = (Path(os.path.abspath(__file__)).parent / "test_codebase_map.template.py").read_text(
        encoding="utf-8"
    )
    driver_src = (
        "import importlib.util, sys\n"
        "spec = importlib.util.spec_from_file_location('gate_under_test', sys.argv[1])\n"
        "mod = importlib.util.module_from_spec(spec)\n"
        "spec.loader.exec_module(mod)\n"
        "print(mod._kit_dir())\n"
    )

    def probe(root: Path, kit: Path | None, gate_dir: Path) -> subprocess.CompletedProcess:
        root.mkdir(parents=True, exist_ok=True)
        (root / ".git").mkdir(exist_ok=True)
        if kit is not None:
            kit.mkdir(parents=True, exist_ok=True)
            # stubs: _kit_dir only tests for map_lib.py, but the template imports both at module
            # level once it has found the dir, so both must exist for exec_module to complete.
            (kit / "map_lib.py").write_text(
                "import re\nDEFAULT_DECISION_ID_RE = re.compile(r'.')\n", encoding="utf-8"
            )
            (kit / "map_extractors.py").write_text(
                "def inventory_ids():\n    return ()\n", encoding="utf-8"
            )
        gate_dir.mkdir(parents=True, exist_ok=True)
        (gate_dir / "test_codebase_map.py").write_text(template, encoding="utf-8")
        driver = root / "drive.py"
        driver.write_text(driver_src, encoding="utf-8")
        return subprocess.run(
            [_sys.executable, str(driver), str(gate_dir / "test_codebase_map.py")],
            capture_output=True, text=True, encoding="utf-8",
        )

    # The gate searches a ONE-segment prefix and no deeper, by its own docstring, so the prefixed
    # fixtures take one segment whatever this install's own depth is: the host's first segment, or
    # a stand-in at a root install (TOOL-aRepatriatedFork-28, gate repair at VERIFYING).
    seg = PFX.split("/")[0] or "kits"
    # (a) PREFIXED kit, gate collected somewhere else entirely — the shape the old walk missed
    r1 = tmp / "g1"
    got = probe(r1, r1 / seg / KIT_NAME, r1 / "tests")
    assert got.returncode == 0, got.stderr
    assert Path(got.stdout.strip()) == r1 / seg / KIT_NAME, got.stdout

    # (b) gate installed INSIDE the kit dir (a repo with no test collector wires it as a leg)
    r2 = tmp / "g2"
    got = probe(r2, r2 / seg / KIT_NAME, r2 / seg / KIT_NAME)
    assert got.returncode == 0, got.stderr
    assert Path(got.stdout.strip()) == r2 / seg / KIT_NAME, got.stdout

    # (c) root install — the original convention, unchanged
    r3 = tmp / "g3"
    got = probe(r3, r3 / KIT_NAME, r3 / "tests")
    assert got.returncode == 0, got.stderr
    assert Path(got.stdout.strip()) == r3 / KIT_NAME, got.stdout

    # (d) no kit at all: a NAMED failure listing what was probed, never a silent wrong dir
    r4 = tmp / "g4"
    got = probe(r4, None, r4 / "tests")
    assert got.returncode != 0, got.stdout
    assert "not found above" in got.stderr and "Probed:" in got.stderr, got.stderr


def test_kit_commits_to_abspath():
    """B2: the kit has committed IN PROSE, three times, to `abspath` and never `resolve()` — a
    junctioned kit dir must anchor to the ADOPTING repo, not the link target. Since the renderers
    embed kit_rel()/regen_cmd() into the BYTE-COMPARED artifacts, one entrypoint resolving the other
    way makes the freshness gate permanently STALE with a printed remedy that re-writes the other
    spelling: the loop never converges. Prose cannot hold that; enforce it mechanically."""
    import os

    kit = Path(os.path.abspath(__file__)).parent
    offenders = []
    for py in sorted(kit.glob("*.py")):
        for n, line in enumerate(py.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("#"):
                continue  # a comment EXPLAINING the ban is not a violation of it
            if "gov:literal-resolve" in line:
                continue  # this detector's own two lines, which must spell what they hunt
            if "__file__" in line and ".resolve()" in line:  # gov:literal-resolve — the detector
                offenders.append(f"{py.name}:{n}: {line.strip()}")
    assert not offenders, (
        "`Path(__file__).resolve()` in the kit — use os.path.abspath. resolve() follows a junction "  # gov:literal-resolve
        "to the link target, so this entrypoint would disagree with map_lib.kit_dir() and the gate "
        "about the install prefix they stamp into the byte-compared artifacts:\n  "
        + "\n  ".join(offenders)
    )


def test_gate_template_boundary(tmp: Path):
    """M1: the gate's kit search must not leave the PROJECT, and `.git` alone is not the project
    boundary — a `git archive` tarball, a docker build whose `.dockerignore` drops `.git`, a vendored
    source drop all have none. The `*/codebase-map` glob then reaches every immediate subdirectory
    of every ancestor up to the filesystem root. Measured with only the `.git` test: the gate found
    an unrelated kit copy OUTSIDE the tree and the module-level import loaded and executed it, so
    the gate would byte-compare this project's artifacts against a foreign engine at a foreign kit
    version — a green or a red that says nothing. `.codebase-map.conf` is committed, so it is the
    boundary that survives the export."""
    import os
    import subprocess
    import sys as _sys

    # the PLANT: a valid-looking kit one level ABOVE the project, reachable only past the boundary
    plant = tmp / "outside" / KIT_NAME
    plant.mkdir(parents=True)
    (plant / "map_lib.py").write_text(
        "import re\nDEFAULT_DECISION_ID_RE = re.compile(r'.')\nPLANT = True\n", encoding="utf-8"
    )
    (plant / "map_extractors.py").write_text("def inventory_ids():\n    return ()\n", encoding="utf-8")

    # the PROJECT: an export with NO .git anywhere, its committed conf at the root, and no kit
    export = tmp / "export"
    (export / "tests").mkdir(parents=True)
    (export / m.CONF_NAME).write_text("MAP_ROOT=memory/map\n", encoding="utf-8")
    template = (Path(os.path.abspath(__file__)).parent / "test_codebase_map.template.py").read_text(
        encoding="utf-8"
    )
    gate = export / "tests" / "test_codebase_map.py"
    gate.write_text(template, encoding="utf-8")
    driver = export / "drive.py"
    driver.write_text(
        "import importlib.util, sys\n"
        "spec = importlib.util.spec_from_file_location('gate_under_test', sys.argv[1])\n"
        "mod = importlib.util.module_from_spec(spec)\n"
        "spec.loader.exec_module(mod)\n"
        "print(mod._kit_dir())\n",
        encoding="utf-8",
    )
    got = subprocess.run(
        [_sys.executable, str(driver), str(gate)], capture_output=True, text=True,
        encoding="utf-8",
    )
    assert got.returncode != 0, (
        f"the gate resolved a kit from OUTSIDE the project: {got.stdout.strip()}"
    )
    assert str(plant) not in got.stdout, got.stdout
    assert "not found above" in got.stderr and "Probed:" in got.stderr, got.stderr


def test_remedy_paths_are_real(tmp: Path):
    """TOOL-aRootedPrefix-2: every path the kit PRINTS must exist from the repo root. A remedy
    naming the kit's `gen_map.py` WITHOUT its prefix at a `<prefix>/`-prefixed install is a dead end
    at exactly the moment someone is stuck.

    Two halves. The pure half pins `relative_kit` across install shapes and pins the legacy
    `REGEN_CMD` constant EQUAL to `regen_cmd()`, so an old gate that reads it prints the command
    for its own prefix (TOOL-aRepatriatedFork-25 S4). The end-to-end half is the real acceptance: build
    a prefixed install, stale an artifact, then RUN THE COMMAND THE GATE PRINTED, verbatim, and
    require that it fixes the staleness — no hardcoded expectation of what the remedy should say."""
    import os
    import re
    import shutil
    import subprocess
    import sys as _sys

    # --- pure: the kit dir as a human must spell it from the repo root -------------------------
    root = tmp / "r"
    assert m.relative_kit(root / KIT_NAME, root) == KIT_NAME
    assert m.relative_kit(root / PFX / KIT_NAME, root) == f"{PFX}{KIT_NAME}"
    assert m.relative_kit(root / "a" / "b" / KIT_NAME, root) == f"a/b/{KIT_NAME}"
    assert "\\" not in m.relative_kit(root / PFX / KIT_NAME, root)  # POSIX on Windows too
    # not under the root (a CODEBASE_MAP_ROOT pointed at a fixture): the bare NAME, so a render
    # never embeds an absolute temp path and fixture bytes stay deterministic.
    assert m.relative_kit(tmp / "elsewhere" / KIT_NAME, root) == KIT_NAME
    # the legacy constant IS the accessor's answer for this install — one fact, not two.
    assert m.REGEN_CMD == m.regen_cmd(), (m.REGEN_CMD, m.regen_cmd())

    # --- end-to-end: the printed remedy, executed --------------------------------------------
    repo = tmp / "e2e"
    kit = repo / PFX / KIT_NAME
    kit.parent.mkdir(parents=True)
    shutil.copytree(Path(os.path.abspath(__file__)).parent, kit)
    (repo / ".git").mkdir()
    # H2: the conf carries the EXAMPLE's stale MAP_DIFF_CMD, which is what the documented adoption
    # path leaves behind (`cp` the example, THEN run the adopter — so the adopter's create-branch
    # stamp never fires). A truthy-but-dead value must not beat the prefix-correct fallback.
    # The stale value is the ROOT-install spelling, built through a prefix variable set EMPTY.
    root_pfx = ""
    (repo / m.CONF_NAME).write_text(
        f'MAP_ROOT=memory/map\nMAP_DIFF_CMD="python {root_pfx}{KIT_NAME}/map_diff.py"\n', encoding="utf-8"
    )
    (repo / "src").mkdir()
    (repo / "src" / "mod.py").write_text("def hello():\n    return 1\n", encoding="utf-8")
    (kit / "map_extractors.py").write_text(
        "import map_lib as m\n"
        "def inventory_ids():\n    return ('mods',)\n"
        "def all_inventories():\n    return {'mods': m.module_inventory(m.repo_root() / 'src', 'mods')}\n",
        encoding="utf-8",
    )

    def run(*args: str) -> subprocess.CompletedProcess:
        # cwd = the repo root, and NO CODEBASE_MAP_ROOT: the resolver must do the work here.
        env = {k: v for k, v in os.environ.items() if k != "CODEBASE_MAP_ROOT"}
        return subprocess.run(
            [_sys.executable, *args], cwd=str(repo), env=env, capture_output=True, text=True,
            encoding="utf-8",
        )

    got = run(f"{PFX}{KIT_NAME}/gen_map.py", "--scaffold")
    assert got.returncode == 0, got.stdout + got.stderr

    # S4 of TOOL-aRepatriatedFork-25: the legacy constant a pre-1.1 GATE_FILE reads names THIS
    # install's generator, so an old gate at a prefix prints a command that exists.
    got = run("-c", f"import sys; sys.path.insert(0, {str(kit)!r}); import map_lib as m; print(m.REGEN_CMD)")
    want = f"python {kit.relative_to(repo).as_posix()}/gen_map.py --write"
    assert got.stdout.strip() == want, got.stdout + got.stderr

    # the scaffolded map README must name the real kit dir, not the convention
    readme = (repo / "memory" / "map" / "README.md").read_text(encoding="utf-8")
    assert f"{PFX}{KIT_NAME}/gen_map.py" in readme, readme[:400]
    assert "`codebase-map/`" not in readme, "the scaffolded README still names the bare convention"

    # H2: EVERY path the kit printed must resolve — not just the regen command. Sweep every
    # `<something>.py` token out of the scaffolded README and the two generated artifacts and
    # require each to be a real file under the root. The digest command is the one that regressed:
    # a stale conf value beat the prefix-correct fallback and shipped a dead path into the README.
    printed = []
    for rel in ("memory/map/README.md", "memory/map/generated/inventories.json",
                "memory/map/generated/MAP.md"):
        for tok in re.findall(r"[A-Za-z0-9_./-]+\.py", (repo / rel).read_text(encoding="utf-8")):
            if "/" in tok:  # a PATH claim; a bare `map_extractors.py` in prose names no location
                printed.append((rel, tok))
    assert printed, "no paths were printed at all — this arm would pass by finding nothing"
    dead = [f"{src} -> {tok}" for src, tok in printed if not (repo / tok).is_file()]
    assert not dead, "the kit printed paths that do not exist:\n  " + "\n  ".join(dead)
    assert any(tok.endswith("map_diff.py") for _, tok in printed), (
        "the digest command vanished from the README — this arm no longer covers H2"
    )

    # stale an artifact, then take the remedy from the gate's OWN output and run it
    art = repo / "memory" / "map" / "generated" / "MAP.md"
    art.write_text(art.read_text(encoding="utf-8") + "\nhand-edited\n", encoding="utf-8")
    got = run(f"{PFX}{KIT_NAME}/gen_map.py", "--check")
    assert got.returncode == 1, f"--check did not detect the stale artifact: {got.stdout}"
    printed = re.search(r"regen:\s*python\s+(\S+)\s+--write", got.stdout)
    assert printed, f"no regen remedy printed: {got.stdout}"
    remedy_path = printed.group(1)
    assert (repo / remedy_path).is_file(), f"the remedy names a path that does not exist: {remedy_path}"
    fixed = run(remedy_path, "--write")
    assert fixed.returncode == 0, fixed.stdout + fixed.stderr
    again = run(f"{PFX}{KIT_NAME}/gen_map.py", "--check")
    assert again.returncode == 0, f"the printed remedy did not fix the staleness: {again.stdout}"

    # the generated artifacts carry the same real prefix (they are the remedy's other home)
    inv = (repo / "memory" / "map" / "generated" / "inventories.json").read_text(encoding="utf-8")
    assert f"{PFX}{KIT_NAME}/gen_map.py" in inv, inv[:400]


def test_coverage_directions():
    cov = m.compute_coverage(INV, {"x": claims(flags=("a_flag",))}, EMPTY_BASE)
    assert cov.unclaimed == {"flags": ["b_flag"], "routes": ["api/x/route.ts"]}
    cov = m.compute_coverage(
        INV,
        {"x": claims(flags=("a_flag", "dead"))},
        EMPTY_BASE | {"flags": ("b_flag",), "routes": ("api/x/route.ts",)},
    )
    assert cov.stale_claims == {"flags": ["x: dead"]}
    cov = m.compute_coverage(
        INV,
        {"x": claims(flags=("a_flag", "b_flag"), routes=("api/x/route.ts",))},
        EMPTY_BASE | {"flags": ("gone", "b_flag")},
    )
    assert cov.stale_baseline == {"flags": ["gone"]}
    assert cov.lazy_baseline == {"flags": ["b_flag"]}
    cov = m.compute_coverage(
        INV,
        {"x": claims(flags=("a_flag", "b_flag"), routes=("api/x/route.ts",)), "y": claims(flags=("a_flag",))},
        EMPTY_BASE,
    )
    assert cov.clean  # multi-claim legal


def test_parse_contract():
    d = m.parse_dossier(DOSSIER, IDS, source="t")
    assert d.feature == "x" and d.claims["flags"] == ("a_flag",)
    expect_maperror(DOSSIER.replace("```toml", "```"), "no ```toml fence")
    expect_maperror(DOSSIER.replace("routes = []", ""), "missing")
    expect_maperror(DOSSIER.replace("routes = []", "routes = []\nrouts = []"), "unknown")
    expect_maperror(DOSSIER.replace('status = "shipped"', 'status = "done"'), "status")
    expect_maperror(DOSSIER.replace('title = "X"', "title = 3"), "title")
    expect_maperror(DOSSIER.replace("REC-someSlug-1", "rec_bad"), "grammar")
    expect_maperror(DOSSIER.replace("src/x/**", "src\\\\x"), "forward-slash")


def test_attribution():
    d = m.parse_dossier(DOSSIER, IDS, source="t")
    f = m.parse_dossier(
        DOSSIER.replace('feature = "x"', 'feature = "foundation"').replace("src/x/**", "lib/**"),
        IDS,
        source="f",
    )
    tree = m.MapTree(foundation=f, dossiers=(d,), baseline=EMPTY_BASE)
    out = m.attribute_paths(["src\\x\\a.ts", "lib/b.ts", "Other/c.ts", "SRC/x/a.ts"], tree)
    assert out["x"] == ["src/x/a.ts"]  # backslash normalized
    assert out["foundation"] == ["lib/b.ts"]
    assert sorted(out["UNMAPPED"]) == ["Other/c.ts", "SRC/x/a.ts"]  # case-sensitive everywhere
    import re

    keyed = ((re.compile(r"^db/migrations/([0-9a-f]+)_"), "flags"),)
    d2 = m.parse_dossier(DOSSIER.replace('flags = ["a_flag"]', 'flags = ["abc123"]'), IDS, source="t")
    tree2 = m.MapTree(foundation=f, dossiers=(d2,), baseline=EMPTY_BASE)
    out2 = m.attribute_paths(["db/migrations/abc123_add.sql"], tree2, keyed_attributors=keyed)
    assert out2["x"] == ["db/migrations/abc123_add.sql"]  # keyed attribution wins


def test_renders_round_trip_and_determinism():
    text = m.render_baseline({"flags": ["b", "a"]}, IDS)
    parsed = m.parse_baseline(text, IDS)
    assert parsed["flags"] == ("a", "b") and parsed["routes"] == ()
    owners = {"x": claims(flags=("a_flag",)), "y": claims(flags=("b_flag",))}
    one = m.render_map_md(INV, IDS, owners, EMPTY_BASE)
    # a PERMUTED view must render byte-identically — reversed key lists AND reversed owner
    # insertion order, so this assert actually pins the renderer's own sorting
    permuted_inv = {k: list(reversed(v)) for k, v in INV.items()}
    permuted_owners = dict(reversed(list(owners.items())))
    two = m.render_map_md(permuted_inv, IDS, permuted_owners, EMPTY_BASE)
    assert one == two and "UNCLAIMED" in one and one.endswith("\n")
    j = m.render_inventories_json(permuted_inv, IDS)
    assert j == m.render_inventories_json(INV, IDS)
    assert '"a_flag"' in j and "claimant" not in j  # keys-only artifact
    # the version marker rides both generated artifacts so the deployer can grep the installed version
    marker = "codebase-map@" + m.KIT_CODEBASE_MAP_VERSION
    assert marker in one and marker in j


def _test_feature_cards():
    """TOOL-aMendedFleet-43: CARDS.md renders from the fences alone, one card per dossier, each
    within FEATURE_CARD_CAP_BYTES, and an overflowing card counts exactly what it dropped."""
    f = m.parse_dossier(DOSSIER.replace('"x"', '"foundation"', 1), IDS, source="f")
    plain = m.parse_dossier(DOSSIER, IDS, source="t")
    big = m.Dossier(
        feature="big", title="é" * 300, status="building", streams=("core",),
        decisions=(), claims=claims(flags=("a_flag",)),
        globs=tuple(f"src/very/long/path/number/{i:03d}/**" for i in range(60)),
    )
    empty = m.render_cards_md(m.MapTree(foundation=f, dossiers=(), baseline=EMPTY_BASE), IDS, "docs/map")
    assert "# Feature cards" in empty and "\n## " not in empty, "an empty tree renders a heading only"
    tree = m.MapTree(foundation=f, dossiers=(plain, big), baseline=EMPTY_BASE)
    text = m.render_cards_md(tree, IDS, "docs/map")
    permuted = m.MapTree(foundation=f, dossiers=(big, plain), baseline=EMPTY_BASE)
    assert text == m.render_cards_md(permuted, IDS, "docs/map"), "cards must not depend on input order"
    cards = re.split(r"(?m)^(?=## )", text)[1:]
    assert [c.split("\n", 1)[0] for c in cards] == ["## big", "## x"], "one card per dossier, sorted, no foundation"
    for c in cards:
        assert len(c.encode("utf-8")) <= m.FEATURE_CARD_CAP_BYTES, f"card over the cap: {len(c.encode('utf-8'))}"
    x = cards[1]
    assert "dossier `docs/map/features/x.md`" in x and "- decisions 1: `REC-someSlug-1`" in x
    assert "- flags 1: `a_flag`" in x and "routes" not in x and "- cut" not in x
    lines = cards[0].rstrip("\n").split("\n")
    assert lines[2].endswith("...") and len(lines[2].encode("utf-8")) <= 160, lines[2]
    globs = next(ln for ln in lines if ln.startswith("- globs "))
    assert globs.startswith("- globs 60: "), globs
    shown = globs.count("`") // 2 + 1  # plus the one flags item
    cut = re.fullmatch(r"- cut (\d+) item\(s\) to fit 1024 bytes; the dossier's toml fence lists them all", lines[-1])
    assert cut and int(cut.group(1)) == 61 - shown, (lines[-1], shown)


def _test_typed_counts():
    """TOOL-aMendedFleet-44: measure_typed_counts raises a present-tense digit count of an
    inventory noun in prose, and nothing else — every S2 clause, positive and negative."""
    ids = ("gate-legs", "rendered-skills", "gotcha-classes")

    def read_hits(text):
        return [mt for _, mt in m.measure_typed_counts(text, ids)[0]]

    positives = {
        "Seven of the 86 legs name a network verb.": ["86 legs"],
        "The bar runs 124 gate legs.": ["124 gate legs"],
        "It holds 1 leg.": ["1 leg"],
        "There are 9 classes and 3 inventory keys.": ["9 classes", "3 inventory keys"],
        "Three of the 27 dossiers remain.": ["27 dossiers"],
        "It ships 4 rendered skills.": ["4 rendered skills"],
        "one\n\nThe bar runs 12\ngate legs; it ran 5 legs on 2026-01-01.": ["12 gate legs"],
    }
    for text, want in positives.items():
        assert read_hits(text) == want, (text, read_hits(text))
    negatives = (
        "see the §7 leg line",
        "Check 42 grades the wall, 43 the Skill's hold routing.",
        "a code span holding `86 legs` here.",
        "before\n\n```\n86 legs\n```\n\nafter",
        "~~~\n86 legs\n~~~",
        "issue #12 legs, path a/12 legs, v1.12 legs, x-12 legs, a12 legs",
        "86 of those legs",
        "two legs and 123456 legs",
        "The bar runs 124 legs, measured at base.",
        "It ran 124 legs at `abc1234`.",
        "node a counts 124 legs.",
        "124 legs, PINNED.",
        "124 legs at review.",
        "124 legs on the day.",
        "There were 124 legs.",
    )
    for text in negatives:
        assert read_hits(text) == [], (text, read_hits(text))
    found, frozen = m.measure_typed_counts("A 3 legs read. B 4 legs.", ids)
    assert [h[1] for h in found] == ["4 legs"] and frozen == 1, (found, frozen)
    assert m.measure_typed_counts("line\n\nnext\n9 legs", ids)[0] == [(4, "9 legs")]
    assert m.measure_typed_counts("", ids) == ([], 0)


def test_conf_grammar(tmp: Path):
    (tmp / ".codebase-map.conf").write_text(
        '# c\nMAP_ROOT=docs/map\nGATE_FILE="tests/test map.py"\n'
        "export MAP_DIFF_CMD=python\nBAD=docs/map # inline\n"
        'NOTED="a b"   # inline after a quoted value\n'
        "HASHED=#x\nBLANKED=   # blank on purpose\n",
        encoding="utf-8",
    )
    conf = m.load_conf(tmp)
    assert conf["MAP_ROOT"] == "docs/map"
    assert conf["GATE_FILE"] == "tests/test map.py"  # quoted value keeps its space
    assert conf["MAP_DIFF_CMD"] == "python"  # export prefix normalized
    assert conf["BAD"] == "docs/map"  # unquoted value ends at whitespace, comment can't leak
    assert conf["NOTED"] == "a b", conf["NOTED"]  # TOOL-aRepatriatedFork-38: ends at its quote
    # rev-3 (C4): bash reads `K=#x` as `#x`, and `K=   # note` as empty, never as the word `#`.
    assert conf["HASHED"] == "#x", conf["HASHED"]
    assert conf["BLANKED"] == "", conf["BLANKED"]


def test_glob_brackets_fail_loud_and_escape_works():
    bad = DOSSIER.replace("src/x/**", "src/app/[id]/**")
    try:
        m.parse_dossier(bad, IDS, source="t")
        raise AssertionError("unescaped [ in a glob must fail")
    except m.MapError as exc:
        assert "character class" in str(exc)
    d = m.parse_dossier(DOSSIER.replace("src/x/**", "src/app/[[]id[]]/*"), IDS, source="t")
    f = m.parse_dossier(DOSSIER.replace('feature = "x"', 'feature = "foundation"'), IDS, source="f")
    tree = m.MapTree(foundation=f, dossiers=(d,), baseline=EMPTY_BASE)
    out = m.attribute_paths(["src/app/[id]/page.tsx"], tree)
    assert out["x"] == ["src/app/[id]/page.tsx"]  # the escape matches the literal segment


def test_extractor_helpers_fail_closed(tmp: Path):
    (tmp / "flat").mkdir(parents=True)
    (tmp / "flat" / "a.py").write_text("x", encoding="utf-8")
    assert m.module_inventory(tmp / "flat", "t") == ["a"]
    (tmp / "flat" / "nested").mkdir()
    try:
        m.module_inventory(tmp / "flat", "t")
        raise AssertionError("subpackage escaped the flat walk")
    except m.MapError:
        pass
    try:
        m.json_artifact_inventory(tmp / "missing.json", "t", lambda d: d)
        raise AssertionError("missing artifact did not fail")
    except m.MapError:
        pass
    (tmp / "app" / "admin" / "x").mkdir(parents=True)
    (tmp / "app" / "admin" / "x" / "page.jsx").write_text("x", encoding="utf-8")
    (tmp / "app" / "api").mkdir(parents=True)
    (tmp / "app" / "api" / "route.tsx").write_text("x", encoding="utf-8")
    pages = frozenset({"page.tsx", "page.ts", "page.jsx", "page.js"})
    routes = frozenset({"route.ts", "route.tsx", "route.js", "route.jsx"})
    assert m.walk_dir_keys(tmp / "app" / "admin", pages, "t") == ["x"]  # extension variants seen
    assert m.walk_file_keys(tmp / "app", routes, "t") == ["api/route.tsx"]
    for key in m.walk_file_keys(tmp / "app", routes, "t"):
        assert "\\" not in key  # POSIX keys on every platform


def test_symbols_render_deterministic_and_fail_closed():
    syms = [
        {"id": "slugify", "kind": "function", "file": "src/text.ts"},
        {"id": "Button", "kind": "component", "file": "web/Button.tsx"},
        {"id": "Cache", "kind": "class", "file": "src/cache.py"},
    ]
    one = m.render_symbols_json(syms)
    two = m.render_symbols_json(list(reversed(syms)))  # input order must not matter
    assert one == two, "symbols render depends on input order (not deterministic)"
    assert one.endswith("\n") and "\\" not in one  # LF-terminated, POSIX paths only
    marker = "codebase-map@" + m.KIT_CODEBASE_MAP_VERSION
    assert marker in one  # version marker rides the artifact
    # ids sorted (ascii: uppercase before lowercase) — the cross-platform byte-match guarantee
    assert one.index('"Button"') < one.index('"Cache"') < one.index('"slugify"')
    # fail-closed shape guards: the freshness gate runs the SAME renderer twice, so it cannot
    # see a fail-open producer — the shape is validated HERE, and every bad row must RAISE.
    for bad, needle in [
        ([{"id": "x", "kind": "widget", "file": "a.ts"}], "unknown kind"),
        ([{"id": "x", "kind": "function"}], "exactly id/kind/file"),
        ([{"id": "", "kind": "function", "file": "a.ts"}], "non-empty"),
        ([{"id": "x", "kind": "function", "file": "a\\b.ts"}], "POSIX"),
    ]:
        try:
            m.render_symbols_json(bad)
            raise AssertionError(f"render accepted a bad row (expected {needle!r})")
        except m.MapError as exc:
            assert needle in str(exc), f"wrong error: {exc}"


def test_symbol_extractors_fail_closed(tmp: Path):
    # --- python_symbols: real parser captures def/class/async/decorated + __all__ ----------
    pkg = tmp / "pkg"
    (pkg / "sub").mkdir(parents=True)
    (pkg / "mod.py").write_text(
        "import functools\n"
        "__all__ = ['slugify', 'CONST']\n"
        "CONST = 1\n"
        "def slugify(s):\n    return s\n"
        "async def fetch():\n    pass\n"
        "def _private():\n    pass\n"
        "@functools.total_ordering\n"
        "class Cache:\n    def method(self):\n        pass\n",
        encoding="utf-8",
    )
    (pkg / "sub" / "deep.py").write_text("def helper():\n    return 1\n", encoding="utf-8")
    syms = m.python_symbols(pkg, "py", root=tmp)
    got = {(s["id"], s["kind"], s["file"]) for s in syms}
    assert ("slugify", "function", "pkg/mod.py") in got
    assert ("fetch", "function", "pkg/mod.py") in got          # async def captured
    assert ("Cache", "class", "pkg/mod.py") in got             # decorated class captured (regex-hard)
    assert ("CONST", "const-export", "pkg/mod.py") in got      # __all__ const, not a def/class
    assert ("helper", "function", "pkg/sub/deep.py") in got    # nested dir walked, POSIX key
    assert not any(s["id"] == "_private" for s in syms)        # underscore = private, skipped
    assert not any(s["id"] == "method" for s in syms)          # a class method is not top-level
    assert all("\\" not in s["file"] for s in syms)            # POSIX keys on every platform
    (pkg / "broken.py").write_text("def broken(\n", encoding="utf-8")  # SyntaxError
    try:
        m.python_symbols(pkg, "py", root=tmp)
        raise AssertionError("python_symbols swallowed a parse error (fail-open)")
    except m.MapError as exc:
        assert "parse error" in str(exc)

    # --- enumerate_exports: the fail-closed JS/TS floor ------------------------------------
    web = tmp / "web"
    web.mkdir()
    (web / "ok.ts").write_text(
        "export function slugify(s) {}\n"
        "export async function load() {}\n"
        "export default class Panel {}\n"
        "export const RATE = 3;\n"
        "export type Foo = string;\n"            # recognized, not indexed (no runtime kind)
        "export interface Bar {}\n"              # recognized, not indexed
        "export { a, b as c } from './x';\n"     # recognized, not indexed (indexed at def site)
        "export * from './y';\n"                 # recognized, not indexed
        "// export function commented() {}\n"    # line comment ignored
        "/* export class Blocked {} */\n",       # block comment ignored
        encoding="utf-8",
    )
    jget = {(s["id"], s["kind"]) for s in m.enumerate_exports(web, "web", extensions=frozenset({".ts"}), root=tmp)}
    assert jget == {
        ("slugify", "function"),
        ("load", "function"),
        ("Panel", "class"),
        ("RATE", "const-export"),
    }, jget
    (web / "bad.ts").write_text("export abstract class Widget {}\n", encoding="utf-8")
    try:
        m.enumerate_exports(web, "web", extensions=frozenset({".ts"}), root=tmp)
        raise AssertionError("enumerate_exports silently skipped an unmodelled export form")
    except m.MapError as exc:
        assert "unmodelled" in str(exc)
    # multi-declarator export must RAISE (capturing only the first name is the fail-open hole):
    md = tmp / "md"
    md.mkdir()
    (md / "x.ts").write_text("export const a = 1, b = 2;\n", encoding="utf-8")
    try:
        m.enumerate_exports(md, "md", extensions=frozenset({".ts"}), root=tmp)
        raise AssertionError("multi-declarator export was silently under-captured")
    except m.MapError as exc:
        assert "multi-declarator" in str(exc)
    # a single declarator with a bracketed comma is NOT a multi-declarator -> no raise:
    (md / "x.ts").write_text("export const xs = [1, 2, 3];\n", encoding="utf-8")
    assert {s["id"] for s in m.enumerate_exports(md, "md", extensions=frozenset({".ts"}), root=tmp)} == {"xs"}
    # a single declarator whose comma sits inside a TS generic is NOT multi-declarator -> no raise
    # (the <> depth fix — the common false positive that blocked a real TS adopter):
    (md / "x.ts").write_text("export const role: Record<string, string> = {};\n", encoding="utf-8")
    assert {s["id"] for s in m.enumerate_exports(md, "md", extensions=frozenset({".ts"}), root=tmp)} == {"role"}
    # anonymous default class extending a base emits NO bogus id "extends":
    (md / "x.ts").write_text("export default class extends Base {}\n", encoding="utf-8")
    assert m.enumerate_exports(md, "md", extensions=frozenset({".ts"}), root=tmp) == []

    # --- scan_js_definitions: the DEFINITION probe the export scan cannot substitute for -------
    # The export scan is complete over export FORMS and blind to a file with no `export` line.
    # Measured on gov's own <prefix>/**/*.js: 30 definitions, 3 indexed export rows, DISJOINT.
    js = tmp / "js"
    js.mkdir()
    (js / "hooks.js").write_text(
        "function boundedK(t) {}\n"                    # bare declaration — the whole point
        "async function loadIt() {}\n"
        "function* genIt() {}\n"                       # generator
        "class Cache {}\n"
        "const slug = (s) => s;\n"                     # arrow const
        "const one = x => x;\n"                        # single-param arrow, no parens
        "const legacy = function () {};\n"             # function expression
        "export function shared() {}\n"                # BOTH a definition and an export
        "const NOTAFN = 3;\n"                          # a value, not a definition
        "  const indented = () => 1;\n"                # statement-leading after whitespace
        "// function commented() {}\n"                 # line comment ignored
        "/* class Blocked {} */\n"                     # block comment ignored
        "const prose = `functionality, duplicate or reinvented functionality?`;\n",
        encoding="utf-8",
    )
    dget = {(s["id"], s["kind"]) for s in m.scan_js_definitions(js, "js", root=tmp)}
    assert dget == {
        ("boundedK", "function"), ("loadIt", "function"), ("genIt", "function"),
        ("Cache", "class"), ("slug", "function"), ("one", "function"),
        ("legacy", "function"), ("shared", "function"), ("indented", "function"),
    }, dget
    # `functionality, …` at the head of a prose line is NOT a function named `ality`. The permissive
    # `function\s*\*?\s*` form indexed exactly that, and it was the one row by which this probe
    # disagreed with the lexicon's independently-authored set over the real corpus.
    assert not any(s["id"] == "ality" for s in m.scan_js_definitions(js, "js", root=tmp))
    # LIVENESS FLOOR: a scanned file that yields nothing RAISES rather than contributing silence —
    # the failure mode that let a 30-definition layer sit at 3 indexed rows without a red anywhere.
    (js / "empty.js").write_text("const x = 1;\nmodule.exports = { x };\n", encoding="utf-8")
    try:
        m.scan_js_definitions(js, "js", root=tmp)
        raise AssertionError("scan_js_definitions indexed nothing from a file and said nothing")
    except m.MapError as exc:
        assert "yielded NO definition" in str(exc) and "empty.js" in str(exc), str(exc)


def test_affordance_graced_presence(tmp: Path):
    # --- parse_affordance: leading seam block, none decl, delimiter-agnostic, presence-only ----
    seams = m.parse_affordance(
        "## Reuse affordance\n"
        "\n"
        "seam: slugify — reuse for name→slug; extend via the transform registry\n"
        "seam: Button - reuse for buttons; extend via the variant prop\n"  # plain hyphen delimiter
        "\n"
        "## Gaps\n"
    )
    assert seams.heading_present and seams.has_block
    assert seams.seams == ("slugify", "Button") and not seams.is_none  # id = first token, delim free
    none_aff = m.parse_affordance("## Reuse affordance\nnone — feature-specific glue, nothing reusable\n")
    assert none_aff.heading_present and none_aff.is_none and none_aff.has_block and none_aff.seams == ()
    bare = m.parse_affordance("## Reuse affordance\n\n## Gaps\n")
    assert bare.heading_present and not bare.has_block  # a bare heading dodges the decision → fails
    absent = m.parse_affordance("## Constraints & why\nx\n## Gaps\ny\n")
    assert not absent.heading_present and not absent.has_block
    # "leading CONSECUTIVE": prose ends the run — a `seam:` after prose is NOT in the block
    broken = m.parse_affordance("## Reuse affordance\nseam: a — x\nSee the notes.\nseam: b — y\n")
    assert broken.seams == ("a",)

    # --- affordance_offenders: graced skip, block passes, missing/bare fails --------------------
    texts = {
        "new_feat": "## Shared seams\n(no affordance section)\n",       # offender: no heading
        "graced_feat": "## Shared seams\n(predates the section)\n",     # exempt → not an offender
        "has_seams": "## Reuse affordance\nseam: slugify — reuse\n",    # ok
        "none_feat": "## Reuse affordance\nnone — nothing reusable\n",  # ok
        "bare": "## Reuse affordance\n\n## Gaps\n",                     # offender: no block
    }
    assert m.affordance_offenders(texts, frozenset({"graced_feat"})) == ["bare", "new_feat"]
    assert m.affordance_offenders(texts, frozenset()) == ["bare", "graced_feat", "new_feat"]

    # --- render → load round-trip + fail-closed on a malformed exempt file ----------------------
    map_dir = tmp / "memory" / "map"
    map_dir.mkdir(parents=True)
    assert m.load_affordance_exempt(tmp) == frozenset()  # absent file = no grace (fresh-repo default)
    rendered = m.render_affordance_exempt(["b", "a", "a"])  # unsorted + dup
    (map_dir / "affordance-exempt.toml").write_text(rendered, encoding="utf-8")
    assert m.load_affordance_exempt(tmp) == frozenset({"a", "b"})
    assert rendered.endswith("\n") and rendered.index('"a"') < rendered.index('"b"')  # sorted, deduped
    for bad, needle in [
        ("exempt = \"x\"\n", "exempt"),        # not a list
        ("exempt = [1]\n", "exempt"),          # non-string element
        ("exempt = [\"\"]\n", "exempt"),       # empty string
        ("other = []\n", "exempt"),            # unknown key / no exempt
        ("exempt = [\n", "toml parse error"),  # malformed toml
    ]:
        (map_dir / "affordance-exempt.toml").write_text(bad, encoding="utf-8")
        try:
            m.load_affordance_exempt(tmp)
            raise AssertionError(f"load accepted a malformed exempt file (expected {needle!r})")
        except m.MapError as exc:
            assert needle in str(exc), f"wrong error: {exc}"


def test_affordance_exemption_drop():
    """AC1 (U4 half): a dossier's affordance grace is dropped MECHANICALLY when a map_diff range
    touches its files (attribution owner), and it then fails the graced check until it carries a
    `seam:`/`none` block. An untouched graced dossier keeps its grace — no retro-red."""
    dx = m.parse_dossier(
        DOSSIER.replace('feature = "x"', 'feature = "touched"').replace("src/x/**", "src/touched/**"),
        IDS, source="touched",
    )
    dy = m.parse_dossier(
        DOSSIER.replace('feature = "x"', 'feature = "untouched"').replace("src/x/**", "src/untouched/**"),
        IDS, source="untouched",
    )
    f = m.parse_dossier(
        DOSSIER.replace('feature = "x"', 'feature = "foundation"').replace("src/x/**", "lib/**"),
        IDS, source="f",
    )
    tree = m.MapTree(foundation=f, dossiers=(dx, dy), baseline=EMPTY_BASE)

    attributed = m.attribute_paths(["src/touched/a.py"], tree)
    assert set(attributed) == {"touched"}, attributed  # only 'touched' was in the range
    exempt = frozenset({"touched", "untouched"})
    kept = m.drop_touched_exemptions(exempt, attributed)
    assert kept == frozenset({"untouched"}), kept  # touched loses grace, untouched keeps it
    # a range that hits nothing graced (foundation/UNMAPPED are never in the exempt list) is a no-op
    assert m.drop_touched_exemptions(exempt, {"UNMAPPED": ["z"], "foundation": ["vendor/b.py"]}) == exempt

    # gate consequence: the un-graced 'touched' dossier (no affordance block yet) is now an offender
    texts = {
        "touched": "## Shared seams\n(no affordance yet)\n",
        "untouched": "## Shared seams\n(still graced)\n",
    }
    assert m.affordance_offenders(texts, exempt) == []          # both graced BEFORE the touch (no retro-red)
    assert m.affordance_offenders(texts, kept) == ["touched"]   # touch dropped grace -> must carry a block
    texts["touched"] = "## Reuse affordance\nseam: foo — reuse for bar; extend via baz\n"
    assert m.affordance_offenders(texts, kept) == []            # clears once it carries a seam:/none block


def test_seed_affordances(tmp: Path):
    """AC5: gen_map --seed-affordances --top N lists the N highest-fan-in seams no dossier yet
    declares, and NOTHING already declared. Pure core tested on a fixture repo (the CLI is thin
    glue over this + build_reference_index); ordering by fan-in desc and the --top cap verified."""
    import os

    (tmp / ".codebase-map.conf").write_text("MAP_ROOT=memory/map\nSEAM_FANIN_THRESHOLD=3\n", encoding="utf-8")
    gen = tmp / "memory" / "map" / "generated"
    gen.mkdir(parents=True)
    syms = [
        {"id": "slugify", "kind": "function", "file": "src/text.py"},
        {"id": "titlecase", "kind": "function", "file": "src/text.py"},
        {"id": "truncate", "kind": "function", "file": "src/text.py"},
        {"id": "Cache", "kind": "class", "file": "src/cache.py"},
    ]
    (gen / "symbols.json").write_text(m.render_symbols_json(syms), encoding="utf-8")
    feats = tmp / "memory" / "map" / "features"
    feats.mkdir(parents=True)
    (feats / "text.md").write_text(  # slugify is ALREADY declared -> off the worklist despite top fan-in
        "## Reuse affordance\nseam: slugify — reuse for name→slug; extend via the registry\n",
        encoding="utf-8",
    )
    src = tmp / "src"
    src.mkdir()
    (src / "text.py").write_text(
        "def slugify(s):\n    return s\n"
        "def titlecase(s):\n    return s\n"
        "def truncate(s, n):\n    return s[:n]\n",
        encoding="utf-8",
    )
    (src / "cache.py").write_text("class Cache:\n    pass\n", encoding="utf-8")
    # reference files planting a known fan-in: slugify 5, titlecase 4, truncate 3, Cache 1
    refs = {
        "a": "from text import slugify, titlecase, truncate\nfrom cache import Cache\nslugify(1); titlecase(2); truncate(3, 4); Cache()\n",
        "b": "from text import slugify, titlecase, truncate\nslugify(1); titlecase(2); truncate(3, 4)\n",
        "c": "from text import slugify, titlecase, truncate\nslugify(1); titlecase(2); truncate(3, 4)\n",
        "d": "from text import slugify, titlecase\nslugify(1); titlecase(2)\n",
        "e": "from text import slugify\nslugify(1)\n",
    }
    for name, body in refs.items():
        (src / f"{name}.py").write_text(body, encoding="utf-8")

    os.environ["CODEBASE_MAP_ROOT"] = str(tmp)
    try:
        corpus = rl.load_corpus()
        ref = m.build_reference_index(corpus.symbol_files)
        assert m.fan_in(ref, "slugify", {"src/text.py"}) == 5
        assert m.fan_in(ref, "titlecase", {"src/text.py"}) == 4
        assert m.fan_in(ref, "truncate", {"src/text.py"}) == 3
        assert m.fan_in(ref, "Cache", {"src/cache.py"}) == 1  # below the threshold -> not a seam

        worklist = rl.seed_affordances(corpus, ref, 10)
        # slugify EXCLUDED (already declares a seam) despite fan-in 5; Cache EXCLUDED (fan-in 1 < 3);
        # ranked by fan-in desc.
        assert [c.name for c, _, _ in worklist] == ["titlecase", "truncate"], worklist
        assert [fi for _, fi, _ in worklist] == [4, 3]
        assert all(c.name != "slugify" for c, _, _ in worklist)  # nothing already declared
        # --top cap: only the single highest-fan-in undeclared seam
        assert [c.name for c, _, _ in rl.seed_affordances(corpus, ref, 1)] == ["titlecase"]
        # TOOL-aMendedFleet-42 S3: installs lift a below-threshold symbol onto the worklist, by the
        # same fan-in + installs test the lookup applies.
        corpus.installs = {"Cache": {"x/one.sh", "x/two.sh"}}
        lifted = {c.name: (fi, n) for c, fi, n in rl.seed_affordances(corpus, ref, 10)}
        assert lifted.get("Cache") == (1, 2), lifted
    finally:
        del os.environ["CODEBASE_MAP_ROOT"]


def _test_install_sites(tmp: Path):
    """TOOL-aMendedFleet-42 S1/S2: two carriers of one canonical-copy marker are two installs, and
    the file the marker names as its canonical copy is the SOURCE and is left out. Staged red by
    counting the source: the count is then three. A candidate at fan-in 1 with two installs is a
    SEAM at threshold 3, and its line prints `installs 2`."""
    import subprocess
    marker = "# >>> helper -- canonical copy: helper.py in the src dir (byte-identical; gated)\n"
    (tmp / "src").mkdir()
    (tmp / "src" / "helper.py").write_text(marker + "def helper():\n    pass\n", encoding="utf-8")
    (tmp / "a.sh").write_text("cat <<'EOF'\n" + marker + "EOF\n", encoding="utf-8")
    (tmp / "b.js").write_text("  // >>> helper -- canonical copy: helper.py\n", encoding="utf-8")
    (tmp / "untracked.sh").write_text(marker, encoding="utf-8")
    subprocess.run(["git", "-c", "init.defaultBranch=main", "init", "-q", str(tmp)],
                   check=True, capture_output=True)
    subprocess.run(["git", "-C", str(tmp), "add", "src/helper.py", "a.sh", "b.js"],
                   check=True, capture_output=True)
    sites, why = m._scan_install_sites(tmp)
    assert why == "", why
    assert sites == {"helper": {"a.sh", "b.js"}}, sites  # source and untracked file left out

    corpus = rl.Corpus(candidates={}, shared_seams={}, symbol_files=[], threshold=3,
                       installs=sites)
    pool = {"helper": rl.Candidate("helper", ("symbol",), "function", ("src/helper.py",))}
    r = rl._rank(pool, corpus, {"helper": {"src/helper.py", "c.py"}}, "helper", True, "name stem")
    assert (r.fanin, r.installs, r.is_seam) == (1, 2, True), r
    assert "fan-in 1 | installs 2 | SEAM" in rl._line(r, corpus), rl._line(r, corpus)

    # an empty scan carries its reason, never a silent zero
    (tmp / "a.sh").write_text("nothing\n", encoding="utf-8")
    (tmp / "b.js").write_text("nothing\n", encoding="utf-8")
    sites, why = m._scan_install_sites(tmp)
    assert sites == {} and why, (sites, why)


def test_reuse_shared_primitives(tmp: Path):
    # --- tokenizer + crude stemmer: the one "shares a token stem" definition (S3 recall)
    assert m.subtokens("getUserID") == ["get", "user", "id"]
    assert m.subtokens("api/x/route.ts") == ["api", "x", "route", "ts"]
    assert m.subtokens("a_flag") == ["a", "flag"]
    assert m.subtokens("HTTPServer") == ["http", "server"]  # acronym run kept, not shredded
    assert m.stems("slugify") == frozenset({"slug"})        # `ify` stripped, NOT down to `y`
    assert m.stems("normalise a name to a slug") & m.stems("slugify") == {"slug"}
    assert not (m.stems("payment gateway") & m.stems("slugify"))  # unrelated -> no shared stem

    # --- fan-in: distinct referencing files minus every def file, comments/strings excluded ---
    src = tmp / "src"
    src.mkdir(parents=True)
    (src / "text.py").write_text("def slugify(s):\n    return s\n", encoding="utf-8")
    (src / "a.py").write_text("from text import slugify\n", encoding="utf-8")         # import ref
    (src / "b.py").write_text("x = slugify(1)  # slugify in a comment too\n", encoding="utf-8")
    (src / "c.py").write_text("s = 'slugify only inside a string'\n", encoding="utf-8")  # excluded
    (src / "d.py").write_text("# just slugify in a comment\ny = 1\n", encoding="utf-8")   # excluded
    idx = m.build_reference_index(["src/text.py"], root=tmp)
    refs = idx.get("slugify", set())
    assert "src/c.py" not in refs and "src/d.py" not in refs, refs  # string/comment-only dropped
    assert m.fan_in(idx, "slugify", {"src/text.py"}) == 2  # a.py + b.py, minus the one def file

    # --- seam threshold from conf: default, override, fail-closed on a non-int -----------------
    assert m.seam_fanin_threshold(tmp) == m.SEAM_FANIN_THRESHOLD_DEFAULT  # no conf -> default
    (tmp / ".codebase-map.conf").write_text("SEAM_FANIN_THRESHOLD=5\n", encoding="utf-8")
    assert m.seam_fanin_threshold(tmp) == 5
    (tmp / ".codebase-map.conf").write_text("SEAM_FANIN_THRESHOLD=nope\n", encoding="utf-8")
    try:
        m.seam_fanin_threshold(tmp)
        raise AssertionError("a non-int SEAM_FANIN_THRESHOLD must fail closed")
    except m.MapError:
        pass


def test_lookup_row_carries_sources(tmp: Path):
    """The log row records WHAT came back, not only that a probe ran, and the write stays non-fatal.

    Against a SCRATCH repo with `CODEBASE_MAP_ROOT` redirected: an arm that wrote into this tree's
    own log would manufacture the very evidence a reader of that log would count.
    """
    import os
    import json
    import subprocess

    (tmp / ".codebase-map.conf").write_text(
        "MAP_ROOT=memory/map\nSEAM_FANIN_THRESHOLD=3\n", encoding="utf-8")
    gen = tmp / "memory" / "map" / "generated"
    gen.mkdir(parents=True)
    # A DOSSIER, and it is the whole point of this fixture. The first version of this arm had none,
    # so `corpus: … 0 affordance seams | 0 dossiers` and the dossier branch of `derive_source_paths`
    # was never entered — the (a2) containment assertion below then passed byte-for-byte against the
    # very defect it was written to gate. Caught by the closing review, which staged the break and
    # watched the arm stay green. A regression gate whose fixture cannot reach the regression is the
    # `fixture-passes-by-finding-nothing` class wearing the costume of a fix.
    feats = tmp / "memory" / "map" / "features"
    feats.mkdir(parents=True)
    (feats / "text.md").write_text(
        "## Reuse affordance\n"
        "seam: slugify — reuse for name->slug; extend via the transform registry\n"
        "\n## Shared seams\nThe text module normalises display names into url slugs.\n",
        encoding="utf-8",
    )
    # BOTH symbols in ONE file, deliberately: `n_shown` counts ranked CANDIDATES and `n_sources`
    # counts distinct source PATHS, so a fixture giving each symbol its own file makes the two
    # numbers coincide and cannot test either. They must differ for the arm to mean anything.
    syms = [{"id": "slugify", "kind": "function", "file": "src/text.py"},
            {"id": "slug_case", "kind": "function", "file": "src/text.py"},
            {"id": "slug_helper", "kind": "function", "file": "src/text.py"}]
    (gen / "symbols.json").write_text(m.render_symbols_json(syms), encoding="utf-8")
    src = tmp / "src"
    src.mkdir()
    (src / "text.py").write_text(
        "def slugify(s):\n    return s\n"
        "def slug_case(s):\n    return s\n"
        "def slug_helper(s):\n    return s\n", encoding="utf-8")
    subprocess.run(["git", "-c", "init.defaultBranch=main", "init", "-q", str(tmp)],
                   check=True, capture_output=True)

    os.environ["CODEBASE_MAP_ROOT"] = str(tmp)
    try:
        corpus = rl.load_corpus()
        ref = m.build_reference_index(corpus.symbol_files)
        sl = rl.assemble_shortlist("normalise a display name into a url slug", corpus, ref)

        # (a) ONE derivation: the paths the writer records are the candidates' own files, deduped
        #     and in shortlist order. Nothing parses rendered output.
        paths = rl.derive_source_paths(sl)
        assert paths == list(dict.fromkeys(paths)), f"not deduped: {paths}"
        assert all("\\" not in p for p in paths), f"not forward-slashed: {paths}"
        assert "src/text.py" in paths, paths

        # (a2) CONTAINMENT IN BOTH DIRECTIONS. A one-way subset assertion is what let the first
        #      cut of this field ship dropping every dossier source: `shown_paths` was a strict
        #      subset of what the reader saw, and a subset assertion cannot see that. The reverse
        #      direction is the whole gate.
        shown = rl._sources(sl, corpus)
        labelled = set()
        for line in shown:
            if line.startswith("symbol def: "):
                labelled.add(line[len("symbol def: "):])
            elif line.startswith("dossier: "):
                labelled.add(line[len("dossier: "):])
        assert set(paths) <= labelled, f"logged a path the reader was never shown: {set(paths) - labelled}"
        assert labelled <= set(paths), f"showed a source the log dropped: {labelled - set(paths)}"
        # (b) the row carries both fields, and n_shown keeps its OLD meaning -- the ranked count,
        #     which is a different number from the path count.
        rl.write_lookup(m.repo_root(), "q", len(sl.ranked), paths, 0)
        log = rl._resolve_git_dir(m.repo_root()) / "codebase-map" / "lookups.jsonl"
        row = json.loads(log.read_text(encoding="utf-8").strip().splitlines()[-1])
        assert row["n_shown"] == len(sl.ranked), row
        assert row["n_sources"] == len(paths), row
        assert row["shown_paths"] == paths[: rl.SOURCE_PATHS_CAP], row

        # (c) THE CAP, exercised rather than assumed: n_sources records the pre-cap count, so a
        #     truncated list is visible AS truncated. Without this the cap is a constant nothing reads.
        many = [f"src/f{i}.py" for i in range(rl.SOURCE_PATHS_CAP + 7)]
        rl.write_lookup(m.repo_root(), "q2", 999, many, 0)
        row = json.loads(log.read_text(encoding="utf-8").strip().splitlines()[-1])
        assert len(row["shown_paths"]) == rl.SOURCE_PATHS_CAP, len(row["shown_paths"])
        assert row["n_sources"] == len(many), row["n_sources"]
        assert row["n_sources"] > len(row["shown_paths"]), "truncation is invisible"

        # (c2) THE REAL CALL SITE, end to end. Everything above drives `write_lookup` with values
        #      the test itself computed, which cannot catch `main()` passing the wrong ones -- and
        #      that is exactly what a defaulted `paths` argument would have hidden. Run the CLI.
        before = log.read_text(encoding="utf-8").strip().splitlines()
        assert rl.main(["normalise a display name into a url slug"]) == 0
        after = log.read_text(encoding="utf-8").strip().splitlines()
        assert len(after) == len(before) + 1, "main() wrote no row"
        real = json.loads(after[-1])
        assert real["n_sources"] == len(real["shown_paths"]), real
        assert real["n_sources"] > 0, "main() logged an EMPTY source set — the argument was dropped"
        assert real["n_shown"] != real["n_sources"], (
            "this fixture cannot tell the two fields apart, so it proves nothing about either")
        # (d) NEVER FATAL: a write that cannot happen must not change the exit code. The root is
        #     pointed at a tree with no git dir at all, which is the real resolution failure.
        nogit = tmp / "nogit"
        nogit.mkdir()
        rl.write_lookup(nogit, "q3", 1, ["src/text.py"], 0)  # must not raise
        assert not list(nogit.rglob("lookups.jsonl")), "wrote a row with no git dir to write into"
    finally:
        os.environ.pop("CODEBASE_MAP_ROOT", None)


def test_neighbour_cap_ranks_before_truncating(tmp: Path):
    """The neighbour cap slices the RANKED pool, not the alphabetical one.

    The fixture is built so the two orderings cannot agree: `zzz_hub` has the highest fan-in in the
    pool and sorts LAST by name, while a run of `aa_*` names with fan-in 0 sorts first. Under the
    shipped code the cap took `sorted(neighbours.items())[:CAP]`, so `_rank` never even saw
    `zzz_hub` and the printed shortlist was the twelve alphabetically-first names ordered by a
    fan-in that had already been thrown away.

    Observed RED against the shipped ordering before it was written: `zzz_hub` was absent from the
    shortlist and the zero-fan-in filler was present.
    """
    import os

    cap = rl.NEIGHBOUR_CAP
    (tmp / ".codebase-map.conf").write_text(
        "MAP_ROOT=memory/map\nSEAM_FANIN_THRESHOLD=3\n", encoding="utf-8")
    gen = tmp / "memory" / "map" / "generated"
    gen.mkdir(parents=True)

    # One seed (matched by name stem), then MORE THAN `cap` same-kind neighbours whose names sort
    # before `zzz_hub`. Filler count is derived from the cap so the arm cannot rot if the cap moves.
    filler = [f"aa_pad_{i:02d}" for i in range(cap + 3)]
    syms = [{"id": "slugify", "kind": "function", "file": "src/text.py"}]
    syms += [{"id": n, "kind": "function", "file": f"src/{n}.py"} for n in filler]
    syms += [{"id": "zzz_hub", "kind": "function", "file": "src/hub.py"}]
    (gen / "symbols.json").write_text(m.render_symbols_json(syms), encoding="utf-8")
    (tmp / "memory" / "map" / "features").mkdir(parents=True)

    src = tmp / "src"
    src.mkdir()
    (src / "text.py").write_text("def slugify(s):\n    return s\n", encoding="utf-8")
    (src / "hub.py").write_text("def zzz_hub(s):\n    return s\n", encoding="utf-8")
    for n in filler:
        (src / f"{n}.py").write_text(f"def {n}(s):\n    return s\n", encoding="utf-8")
    # zzz_hub is referenced from many files -> the highest fan-in in the pool. The filler is
    # referenced from none -> fan-in 0. Nothing references slugify, so the seed stays a seed.
    for i in range(6):
        (src / f"ref{i}.py").write_text("from hub import zzz_hub\nx = zzz_hub(1)\n", encoding="utf-8")

    os.environ["CODEBASE_MAP_ROOT"] = str(tmp)
    try:
        corpus = rl.load_corpus()
        ref = m.build_reference_index(corpus.symbol_files)
        sl = rl.assemble_shortlist("normalise a display name into a url slug", corpus, ref)
        neighbours = [r for r in sl.ranked if not r.is_seed]
        names = [r.candidate.name for r in neighbours]

        assert neighbours, "the fixture produced no neighbours at all — it proves nothing"
        assert len(neighbours) <= cap, f"the cap was not applied: {len(neighbours)} > {cap}"
        assert "zzz_hub" in names, (
            "the highest-fan-in neighbour was truncated before it could be ranked — the cap is "
            f"still slicing the alphabetical pool: {names}"
        )
        assert names[0] == "zzz_hub", f"the ranked cap must keep fan-in order: {names}"
        # and the ordering is descending fan-in, which is the key the shortlist sort also reads
        fanins = [r.fanin for r in neighbours]
        assert fanins == sorted(fanins, reverse=True), fanins
    finally:
        os.environ.pop("CODEBASE_MAP_ROOT", None)


def test_neighbour_predicate_is_directory_scoped(tmp: Path):
    """The same-kind arm admits a candidate in the seed's DIRECTORY and refuses one outside it.

    Both directions, because a narrowing tested only on what it keeps is a narrowing whose whole
    point is unobserved. Kind alone admitted 95% of the corpus here; the cap over that selected
    nothing, whatever it sorted by.

    Observed RED against the un-narrowed predicate before it was written: `far_helper` was admitted
    as a `same kind` neighbour from another directory.
    """
    import os

    (tmp / ".codebase-map.conf").write_text(
        "MAP_ROOT=memory/map\nSEAM_FANIN_THRESHOLD=3\n", encoding="utf-8")
    gen = tmp / "memory" / "map" / "generated"
    gen.mkdir(parents=True)
    syms = [
        {"id": "slugify", "kind": "function", "file": "src/near/text.py"},     # the seed
        {"id": "near_helper", "kind": "function", "file": "src/near/util.py"},  # same dir  -> ADMIT
        {"id": "far_helper", "kind": "function", "file": "src/far/util.py"},    # other dir -> REFUSE
    ]
    (gen / "symbols.json").write_text(m.render_symbols_json(syms), encoding="utf-8")
    (tmp / "memory" / "map" / "features").mkdir(parents=True)

    (tmp / "src" / "near").mkdir(parents=True)
    (tmp / "src" / "far").mkdir(parents=True)
    (tmp / "src" / "near" / "text.py").write_text("def slugify(s):\n    return s\n", encoding="utf-8")
    (tmp / "src" / "near" / "util.py").write_text("def near_helper(s):\n    return s\n", encoding="utf-8")
    (tmp / "src" / "far" / "util.py").write_text("def far_helper(s):\n    return s\n", encoding="utf-8")
    # far_helper is the HIGHER fan-in of the two, so if it is absent that is the predicate refusing
    # it rather than the ranking burying it — otherwise this arm would pass for the wrong reason.
    for i in range(4):
        (tmp / "src" / f"ref{i}.py").write_text(
            "from far.util import far_helper\nx = far_helper(1)\n", encoding="utf-8")

    os.environ["CODEBASE_MAP_ROOT"] = str(tmp)
    try:
        corpus = rl.load_corpus()
        ref = m.build_reference_index(corpus.symbol_files)
        sl = rl.assemble_shortlist("normalise a display name into a url slug", corpus, ref)
        same_kind = {r.candidate.name: r for r in sl.ranked
                     if not r.is_seed and "same kind" in r.reason}

        assert "near_helper" in same_kind, (
            f"the narrowed arm dropped a same-directory candidate: {sorted(same_kind)}")
        assert "far_helper" not in same_kind, (
            "the same-kind arm admitted a candidate from another directory — the predicate is "
            f"still kind-only: {sorted(same_kind)}")
        # S4: the printed reason names the narrowed predicate, so an empty pool reads as honest.
        assert "src/near" in same_kind["near_helper"].reason, same_kind["near_helper"].reason
    finally:
        os.environ.pop("CODEBASE_MAP_ROOT", None)


def test_reuse_lookup(tmp: Path):
    """AC3 on a portable FIXTURE repo (no host-repo paths): a planted `slugify` seam is ranked
    above unrelated symbols for a behaviour query; a no-home query returns 'no seam fits'; and a
    recall-dark layer prints the partial-recall notice so an empty result is never falsely sure."""
    import os

    (tmp / ".codebase-map.conf").write_text(
        'MAP_ROOT=memory/map\nRECALL_DARK_LAYERS=".ts"\nSEAM_FANIN_THRESHOLD=3\n', encoding="utf-8"
    )
    gen = tmp / "memory" / "map" / "generated"
    gen.mkdir(parents=True)
    syms = [
        {"id": "slugify", "kind": "function", "file": "src/text.py"},
        {"id": "titlecase", "kind": "function", "file": "src/text.py"},
        {"id": "truncate", "kind": "function", "file": "src/text.py"},
        {"id": "Cache", "kind": "class", "file": "src/cache.py"},
    ]
    (gen / "symbols.json").write_text(m.render_symbols_json(syms), encoding="utf-8")
    (gen / "inventories.json").write_text(
        m.render_inventories_json({"flags": ["beta_flag"]}, ("flags",)), encoding="utf-8"
    )
    feats = tmp / "memory" / "map" / "features"
    feats.mkdir(parents=True)
    (feats / "text.md").write_text(
        # Front matter carrying `decisions`, so the reuse audit has ids to surface. Read from
        # the dossier TEXT, which is why this fixture still needs no project-side extractor.
        "```toml\n"
        'feature = \"text\"\n'
        'decisions = [\"ARCH-aSeeded-1\", \"ARCH-aSeeded-2\"]\n'
        "```\n\n"
        "## Reuse affordance\n"
        "seam: slugify — reuse for name→slug; extend via the transform registry\n"
        "\n"
        "## Shared seams\n"
        "The text module normalises display names into url slugs.\n",
        encoding="utf-8",
    )
    (feats / "glue.md").write_text(  # prose-only feature: `none` affordance, no seam symbol
        # Front matter here too, because this feature surfaces as the SYNTHETIC
        # `<feature> (## Shared seams)` candidate rather than through a named seam. That is a
        # different construction site, and it is the one that shipped empty.
        "```toml\n"
        'feature = \"glue\"\n'
        'decisions = [\"ARCH-aGlued-9\"]\n'
        "```\n\n"
        "## Reuse affordance\nnone — feature-specific glue\n"
        "\n## Shared seams\nThe glue layer wires the webhook dispatcher.\n",
        encoding="utf-8",
    )
    src = tmp / "src"
    src.mkdir()
    (src / "text.py").write_text(
        "def slugify(s):\n    return s\n"
        "def titlecase(s):\n    return s\n"
        "def truncate(s, n):\n    return s[:n]\n",
        encoding="utf-8",
    )
    for f in ("a", "b", "c"):
        (src / f"{f}.py").write_text(f"from text import slugify\nx = slugify('{f}')\n", encoding="utf-8")
    (src / "cache.py").write_text("class Cache:\n    pass\n", encoding="utf-8")

    os.environ["CODEBASE_MAP_ROOT"] = str(tmp)
    try:
        corpus = rl.load_corpus()
        ref = m.build_reference_index(corpus.symbol_files)

        # (a) a slug query ranks the planted seam FIRST and above unrelated same-file symbols
        sl = rl.assemble_shortlist("normalise a display name into a url slug", corpus, ref)
        names = [r.candidate.name for r in sl.ranked]
        assert names and names[0] == "slugify", names
        assert names.index("slugify") < names.index("titlecase"), names  # seed above neighbour
        top = sl.ranked[0]
        assert top.is_seed and top.is_seam and top.fanin == 3, top      # fan-in on demand, seam
        assert "affordance-seam" in corpus.candidates["slugify"].sources  # merged symbol + seam
        assert "Cache" not in names, names  # different kind AND file -> not a neighbour
        out = rl.render(sl, corpus)
        assert "recall partial: layers .ts" in out                   # (c) recall-dark announced
        # THE DECISIONS CLAUSE: its own line, and EVERY id rather than the first few. This
        # fixture has no `map_extractors.py` at all, so passing here is also the assertion that
        # reading the field kept this module portable instead of quietly ending that property.
        assert "decisions: ARCH-aSeeded-1 ARCH-aSeeded-2" in out, out
        assert not (tmp / "map_extractors.py").exists()  # the portability premise, asserted

        # (b) a no-home query returns "no seam fits" — and STILL flags the recall-dark gap
        sl2 = rl.assemble_shortlist("configure the payment gateway retry budget", corpus, ref)
        assert sl2.empty, [r.candidate.name for r in sl2.ranked]
        out2 = rl.render(sl2, corpus)
        assert "no seam fits" in out2
        assert "recall partial: layers .ts" in out2  # never a falsely-confident "no seam"

        # `## Shared seams` prose recall: a seam-less feature surfaces via its prose (behavioural
        # recall beyond symbol names), and assembling is IDEMPOTENT (no synthetic leak into corpus).
        before = len(corpus.candidates)
        sl3 = rl.assemble_shortlist("dispatch a webhook", corpus, ref)
        names3 = [r.candidate.name for r in sl3.ranked]
        assert "glue (## Shared seams)" in names3, names3
        # THE SYNTHETIC CANDIDATE CARRIES ITS DOSSIER'S IDS. This is the path the seam-named
        # assertion above cannot reach: the candidate is constructed elsewhere, and it shipped
        # with an empty decisions field while the seam path worked — so reverting that fix left
        # the other arm green. A dossier surfaced as ITSELF must print its own reasoning.
        assert "decisions: ARCH-aGlued-9" in rl.render(sl3, corpus), rl.render(sl3, corpus)
        assert len(corpus.candidates) == before  # pool copy, not the caller's corpus
    finally:
        del os.environ["CODEBASE_MAP_ROOT"]


def test_dossier_staleness_from_git(tmp: Path):
    """TOOL-aMendedFleet-37 S1-S3: a dossier is stale when a commit touching a claimed path is not
    an ancestor of the dossier's own last commit, read whole and by range, over a REAL git fixture —
    ancestry exists only in an object store. A map-root-only commit never stales it, and a dossier
    no commit carries is named in the note and left out of `of`."""
    import json
    import os
    import subprocess

    import map_diff as md

    env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull,
               GIT_CONFIG_NOSYSTEM="1")

    def run_git(*a):
        r = subprocess.run(["git", "-C", str(tmp), *a], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env)
        assert r.returncode == 0, f"git {' '.join(a)} failed: {r.stderr.strip()[:200]}"
        return r.stdout.strip()

    def write_commit(rel, text, msg):
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp / rel).write_text(text, encoding="utf-8")
        run_git("add", "-A")
        run_git("commit", "-qm", msg)
        return run_git("rev-parse", "HEAD")

    run_git("init", "--template=", "-q")
    run_git("config", "user.email", "t@t")
    run_git("config", "user.name", "t")
    run_git("config", "commit.gpgsign", "false")
    write_commit("src/x/a.ts", "1\n", "seed code")
    refresh = write_commit("map/features/x.md", "x\n", "refresh the dossier")
    code = write_commit("src/x/a.ts", "2\n", "code moves after the refresh")
    write_commit("map/generated/s.json", "{}\n", "map-root only")

    # x claims the map root as the real codebase-map dossier does, so the exclusion is what holds.
    d = m.parse_dossier(DOSSIER.replace('"src/x/**"', '"src/x/**", "map/*"'), IDS, source="t")
    y = m.parse_dossier(DOSSIER.replace('feature = "x"', 'feature = "y"'), IDS, source="t")
    f = m.parse_dossier(DOSSIER.replace('feature = "x"', 'feature = "foundation"').replace("src/x/**", "lib/**"),
                        IDS, source="f")
    tree = m.MapTree(foundation=f, dossiers=(d, y), baseline=EMPTY_BASE)

    def measure(base, head="HEAD"):
        commits, scope = md.read_commit_paths(tmp, base, head)
        return {r["feature"]: r for r in m.measure_dossier_staleness(commits, tree, "map", scope=scope)}

    at_refresh = measure(None, refresh)["x"]
    assert at_refresh["refreshed"] == refresh and not at_refresh["stale"], at_refresh
    whole = measure(None)
    x = whole["x"]
    assert x["stale"] and x["behind"] == 1 and x["newest"] == code, f"a code commit after the refresh: {x}"
    assert whole["y"]["refreshed"] is None, "y has no commit of its own"
    doc = json.loads(md.render_stale_dossiers("HEAD", list(whole.values()), as_json=True))
    assert (doc["of"], doc["stale"], doc["live"]) == (1, 1, True), doc
    assert doc["note"].endswith("carries them yet: y") and [r["feature"] for r in doc["dossiers"]] == ["x"], doc

    in_range = measure(refresh)  # refresh..HEAD holds the code commit and no dossier commit
    assert in_range["x"]["stale"] and in_range["x"]["refreshed"] == refresh, in_range["x"]
    text = md.render_stale_dossiers(f"{refresh}..HEAD", list(in_range.values()), as_json=False)
    assert "- x · map/features/x.md · 1 behind" in text, text

    again = write_commit("map/features/x.md", "x again\n", "refresh after the code")
    fixed = measure(refresh)["x"]
    assert fixed["refreshed"] == again and not fixed["stale"] and fixed["touched"] == 1, fixed
    assert "- x ·" not in md.render_stale_dossiers("r", list(measure(refresh).values()), as_json=False)

    shallow = json.loads(md.render_stale_dossiers("HEAD", None, as_json=True))
    assert shallow["live"] is False and "shallow" in shallow["note"] and shallow["of"] == 0, shallow
    untouched = m.measure_dossier_staleness([("a", (), ("map/x.md",))], tree, "map")
    assert json.loads(md.render_stale_dossiers("HEAD", untouched, as_json=True))["live"] is False, \
        "a whole history touching no claimed path is not a clean all-fresh answer"


def test_record_roots_split_code_from_records(tmp: Path):
    """TOOL-aMendedFleet-86 S2-S4: RECORD_ROOTS partitions the digest's population, over a REAL git
    fixture because a root is live only when `git ls-files` names a path under it. One code file and
    one record file split one of each; blank is undeclared; an entry naming nothing tracked is DEAD.
    Staged red by dropping the root from the conf: the split then claims no records."""
    import os
    import subprocess

    import map_diff as md

    env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull,
               GIT_CONFIG_NOSYSTEM="1")
    for rel in ("src/a.py", "memory/r.md"):
        (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp / rel).write_text("x\n", encoding="utf-8")
    for a in (("init", "--template=", "-q"), ("add", "-A")):
        r = subprocess.run(["git", "-C", str(tmp), *a], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env)
        assert r.returncode == 0, f"git {' '.join(a)} failed: {r.stderr.strip()[:200]}"

    roots, dead = md.derive_record_roots(tmp, {"RECORD_ROOTS": "memory/"})
    assert (roots, dead) == (["memory"], None), (roots, dead)
    files = ["src/a.py", "memory/r.md"]
    records = [p for p in files if any(p == r or p.startswith(r + "/") for r in roots)]
    assert records == ["memory/r.md"] and len(files) - len(records) == 1, records
    assert md.derive_record_roots(tmp, {"RECORD_ROOTS": ""}) == ([], None)
    assert md.derive_record_roots(tmp, {}) == ([], None)
    assert md.derive_record_roots(tmp, {"RECORD_ROOTS": "memory,nosuchdir"}) == (["memory", "nosuchdir"],
                                                                                "nosuchdir")
    assert md.render_coverage_line("code", 1, 3) == "# code: mapped 1/3 (33%)"
    assert md.render_coverage_line("records", 0, 0) == "# records: n/a (0 files)"


def test_baseline_additions_from_git(tmp: Path):
    """TOOL-aMendedFleet-40 S5: the baseline is graded against its own copy at a base sha, over a
    REAL git fixture. An added key is named, an unchanged file gains nothing, and a base with no
    baseline is NO comparison — never an empty one that would read every key as added."""
    import os
    import subprocess

    env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull,
               GIT_CONFIG_NOSYSTEM="1")

    def run_git(*a):
        r = subprocess.run(["git", "-C", str(tmp), *a], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env)
        assert r.returncode == 0, f"git {' '.join(a)} failed: {r.stderr.strip()[:200]}"
        return r.stdout.strip()

    run_git("init", "--template=", "-q")
    run_git("config", "user.email", "t@t")
    run_git("config", "user.name", "t")
    run_git("config", "commit.gpgsign", "false")
    (tmp / "README").write_text("x\n", encoding="utf-8")
    run_git("add", "-A")
    run_git("commit", "-qm", "no map yet")
    bare = run_git("rev-parse", "HEAD")
    baseline = tmp / "memory" / "map" / "baseline.toml"
    baseline.parent.mkdir(parents=True)
    baseline.write_text(m.render_baseline({"flags": ["a"]}, IDS), encoding="utf-8")
    run_git("add", "-A")
    run_git("commit", "-qm", "seed the baseline")
    seeded = run_git("rev-parse", "HEAD")

    same, note = m.derive_baseline_additions(tmp, seeded)
    assert same == {} and "base carried 1 key(s), working carries 1" in note, (same, note)
    baseline.write_text(m.render_baseline({"flags": ["a", "b"], "routes": ["r"]}, IDS), encoding="utf-8")
    added, _ = m.derive_baseline_additions(tmp, seeded)
    assert added == {"flags": ["b"], "routes": ["r"]}, f"an added key must be named: {added}"
    none, why = m.derive_baseline_additions(tmp, bare)
    assert none is None and "no memory/map/baseline.toml" in why, (none, why)
    # TOOL-dLadderedRemote-2: the remote is the LADDER'S, not one called `origin`. The ambient
    # GOV_REMOTE and GOV_DEFAULT_BRANCH are cleared for these arms, so a node exporting either
    # cannot make one pass, and restored after.
    saved = {k: os.environ.pop(k) for k in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH") if k in os.environ}
    try:
        gone, reason = m.resolve_compare_base(tmp)
        assert gone is None and reason == "no remote to compare against", (gone, reason)
        run_git("remote", "add", "upstream", "../upstream.git")
        run_git("update-ref", "refs/remotes/upstream/main", bare)
        run_git("symbolic-ref", "refs/remotes/upstream/HEAD", "refs/remotes/upstream/main")
        got, why = m.resolve_compare_base(tmp)
        assert got == bare and why == "merge-base of HEAD and upstream/main", (got, why)
        # TOOL-dLadderedRemote-5: the OBSERVED branch, never GOV_DEFAULT_BRANCH, picks the base.
        os.environ["GOV_DEFAULT_BRANCH"] = "elsewhere"
        same, why = m.resolve_compare_base(tmp)
        assert same == bare and why == "merge-base of HEAD and upstream/main", (same, why)
        del os.environ["GOV_DEFAULT_BRANCH"]
        run_git("remote", "add", "origin", "../origin.git")
        run_git("update-ref", "refs/remotes/origin/main", seeded)
        refused, why = m.resolve_compare_base(tmp)
        assert refused is None and "export GOV_REMOTE=<remote>" in why, (refused, why)
        os.environ["GOV_REMOTE"] = "upstream"
        chosen, why = m.resolve_compare_base(tmp)
        assert chosen == bare and "upstream/main" in why, (chosen, why)
    finally:
        os.environ.pop("GOV_REMOTE", None)
        os.environ.update(saved)


def test_identifier_tokens_per_language():
    """TOOL-aLexedStripper-1 §4 + -6: one arm per over-strip class, each asserting an identifier the
    LANGUAGE-BLIND chain deleted. Every fixture below was observed RED against the three-regex
    chain before this arm was wired -- the class table in that spec's §4 records which identifier
    each one lost. The arms assert the CLASS, not the reported instance: a suffix gate on the block
    regex alone (the adopter's proposed fix) passes rows 1-2 and fails 3-5.

    Both directions are checked. `absent` is not decoration: a scanner that strips nothing passes
    every `present` assertion, so the negative arms are what stop this test being satisfied by
    doing no work at all."""
    cases = [
        # (label, suffix, source, must be present, must be absent)
        ("class1 /* in a Python docstring", ".py",
         'def alpha():\n    """docs for application/* glob"""\n    return BRAVO\n# on*/\ndef charlie(): pass\n',
         {"alpha", "BRAVO", "charlie"}, set()),
        ("class2 // is floor division in Python", ".py",
         "def alpha():\n    return DELTA // ECHO\n", {"alpha", "DELTA", "ECHO"}, set()),
        ("class2 // is a path in shell", ".sh",
         "p=//server/share\nalpha=1\n", {"p", "server", "share", "alpha"}, set()),
        ("class3 # inside a TypeScript string", ".ts",
         'const a = "#frag" + bravo\nconst charlie = 1\n', {"a", "bravo", "charlie"}, set()),
        ("class3 # is a private field in TypeScript", ".ts",
         "class Foo { #priv = 1; bravo() {} }\n", {"Foo", "bravo"}, set()),
        ("class4 // inside a URL literal", ".ts",
         'const u = "https://x.io/" + bravo\n', {"u", "bravo"}, set()),
        ("class4 # inside a Python string", ".py",
         'alpha = "a # b" + bravo\n', {"alpha", "bravo"}, set()),
        ("class5 backtick is command substitution in shell", ".sh",
         "alpha=`date`\nbravo=1\n", {"alpha", "date", "bravo"}, set()),
        # the word-start predicate: the field a five-field profile could not express
        ("shell $# is not a comment", ".sh",
         'if [ $# -gt 0 ]; then resolve_target "$1"; fi\n', {"resolve_target"}, set()),
        ("shell ${x#y} is not a comment", ".sh",
         "prefix=${path#/opt/}; emit_result $prefix\n",
         {"prefix", "path", "opt", "emit_result"}, set()),
        ("shell a REAL comment is still stripped", ".sh",
         "alpha=1  # this is GONE\nbravo=2\n", {"alpha", "bravo"}, {"GONE"}),
        # S5: an unterminated multi-line construct is abandoned, never allowed to eat the file
        ("unterminated backtick does not swallow the file", ".ts",
         "const a = `unterminated\nconst bravo = 1\nfunction charlie() {}\n", {"bravo", "charlie"}, set()),
        ("unterminated triple quote does not swallow the file", ".py",
         'x = """unterminated\ndef bravo(): pass\ndef charlie(): pass\n', {"bravo", "charlie"}, set()),
        # S4: an undeclared suffix strips NOTHING -- the fail-open direction, stated and checked
        ("an undeclared suffix strips nothing", ".zzz",
         "anything # goes /* here */ `and` here\n", {"anything", "goes", "here", "and"}, set()),
        # TOOL-aLexedStripper-6: an interpolation body is CODE
        ("python f-string replacement field is code", ".py",
         'msg = f"hi {name.upper()} and {other or fallback}"\n',
         {"name", "upper", "other", "or", "fallback"}, set()),
        ("rf-string still interpolates", ".py",
         'p = rf"^\\s*{re.escape(marker)}\\b"\n', {"re", "escape", "marker"}, set()),
        # `k` is deliberately expected ABSENT: it is a STRING token, not a NAME, and stdlib
        # `tokenize` agrees. An earlier revision of this arm demanded it and was wrong -- the
        # interpolation walk now blanks nested strings, which is what stops a brace inside one
        # inflating the depth and leaking the rest of the file into the index.
        ("a field may hold a nested quote", ".py",
         "v = f\"{d['k'] if flag else other}\"\n", {"d", "flag", "other"}, {"k"}),
        ("a string with NO f prefix holds no code", ".py",
         's = "{not_code}"\nalpha = 1\n', {"alpha"}, {"not_code"}),
        ("a b-string holds no code", ".py",
         'v = b"{not_code}"\nalpha = 1\n', {"alpha"}, {"not_code"}),
        ("a doubled brace is literal text", ".py",
         'v = f"{{literal}}"\nalpha = 1\n', {"alpha"}, {"literal"}),
        ("a JS template interpolation is code", ".ts",
         "const r = `x ${compute(y)} z`\n", {"compute", "y"}, set()),
    ]
    for label, suffix, src, present, absent in cases:
        got = m._identifier_tokens(src, suffix)
        missing = sorted(present - got)
        leaked = sorted(absent & got)
        assert not missing, f"{label}: lost {missing}"
        assert not leaked, f"{label}: admitted {leaked} from a non-code position"


def test_identifier_tokens_corpus_recall():
    """TOOL-aLexedStripper-1 AC1/AC2 + -6 AC2/AC3: the CLASS gated over this repo's real Python
    corpus, against stdlib `tokenize` NAME tokens -- the exact set this function approximates.

    Floors, not fixed figures: a floor cannot go stale on the next commit the way a pinned count
    would, and it is the property that matters. Measured at the landing commit: recall 100.0%,
    precision 98.1%, against 88.6% and 37.6% for the three-regex chain this replaced.

    SKIPPED, loudly, outside a git checkout of this repo -- an adopter copy-installs the kit and has
    no such corpus. A skip that looks like a pass is indistinguishable from coverage."""
    import io
    import subprocess
    import tokenize as _tok

    root = m.repo_root()
    # THIS REPO, not merely "a git checkout". The floors below are calibrated against this corpus;
    # run them anywhere else and they are a claim about a population nobody measured. Measured: the
    # CPython tree scores 0.858 precision against the 0.95 floor, so a git-ness guard turns this arm
    # into a spurious RED in any adopter that vendors the kit inside its own repo.
    if not (root / "coding-governance-agents.template.md").is_file():
        raise Skipped("not the coding-governance repo, and these floors are calibrated to its "
                      "corpus")
    try:
        listing = subprocess.run(
            # `encoding=` EXPLICITLY (TOOL-dRetiredFork-5, from adopter ic's
            # KIT_CODEBASE_MAP_SELFTEST_DELTA). `text=True` alone decodes with the locale codec, so
            # a repo path carrying a non-ASCII byte raises UnicodeDecodeError on a Windows console
            # codepage and the arm dies for a reason that has nothing to do with what it measures.
            ["git", "-C", str(root), "ls-files", "*.py"],
            capture_output=True, text=True, check=True, encoding="utf-8",
        ).stdout.split("\n")
    except (OSError, subprocess.CalledProcessError):
        raise Skipped("not a git checkout, so there is no corpus to measure")

    truth_total = hit = kept = 0
    for rel in listing:
        if not rel:
            continue
        path = root / rel
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
            names = {t.string for t in _tok.generate_tokens(io.StringIO(text).readline)
                     if t.type == _tok.NAME}
        except (OSError, UnicodeDecodeError, _tok.TokenError, IndentationError, SyntaxError):
            continue
        if not names:
            continue
        got = m._identifier_tokens(text, ".py")
        truth_total += len(names)
        hit += len(got & names)
        kept += len(got)

    if truth_total < 1000:
        raise Skipped(f"only {truth_total} ground-truth identifiers found")
    recall = hit / truth_total
    precision = hit / kept if kept else 0.0
    assert recall >= 0.99, f"corpus recall {recall:.3f} below the 0.99 floor"
    assert precision >= 0.95, f"corpus precision {precision:.3f} below the 0.95 floor"


def test_js_probe_against_the_lexicon():
    """CROSS-CHECK: over this repo's own `<prefix>/**/*.js`, the map's definition set is a SUPERSET of
    the lexicon's independently-authored one.

    WHY THIS DIRECTION ONLY. If the lexicon learns a definition form the map has not, the map is
    UNDER-indexing and that is the defect — silently, since a recall index that misses a seam looks
    exactly like a corpus that has none. The other direction is not a defect: the map indexes
    `export const meta = {…}` and the lexicon does not, correctly, today.

    NOT A SECOND OPINION — DRIFT PROTECTION. The two probes were written independently for different
    questions, which is what makes the comparison worth anything; unifying them behind one pattern
    set would delete the signal along with the duplication.

    SKIPS LOUDLY when `<prefix>/lexicon/` is absent. An adopter who took the map without the lexicon is
    TOLD the arm did not run, rather than shown a green it did not earn — a silent skip here would be
    this repo's own `fixture-passes-by-finding-nothing` class inside the kit that gates it.
    """
    # A SIBLING of this kit, found from where the kit sits and never from gov's prefix
    # (TOOL-aRepatriatedFork-24 S6): at an adopter whose kits live under `scripts/`, the spelled path
    # skipped this arm with a false "not installed" over a lexicon that was right beside it.
    kit = m.kit_dir().with_name("lexicon")
    if not (kit / "lexicon.py").is_file():
        raise Skipped(f"no lexicon kit beside this one at {kit.as_posix()}, so the independent "
                      f"definition set this arm compares against does not exist")
    sys.path.insert(0, str(kit))
    try:
        import lexicon as lx
        import lexicon_conf as lxc
    finally:
        sys.path.pop(0)
    root = m.repo_root()
    conf = lxc.load_conf(root / ".lexicon.conf")
    langs = {ext: (pset, mode) for ext, pset, mode in lxc.langs(conf) if mode != "dark"}
    if "js" not in langs:
        raise Skipped(".lexicon.conf declares no live `js` language")
    pset, mode = langs["js"]
    theirs = set()
    for f in lx.tracked_files(root):
        if f.endswith(".js") and f.startswith(f"{PFX}"):
            fns, types, _imports = lx.extract(root / f, mode, pset)
            theirs |= {(f, name) for name, _line in list(fns) + list(types)}
    ours = {(r["file"], r["id"]) for r in m.scan_js_definitions(root / PFX, "kit-js")}
    missing = sorted(theirs - ours)
    assert not missing, (
        f"the map's JS definition probe misses {len(missing)} symbol(s) the lexicon's finds — the "
        f"map is under-indexing this layer: {missing[:8]}"
    )
    assert theirs, f"the lexicon found NO js definitions under {PFX}, so this arm compared to empty"


def main() -> int:
    import tempfile

    failures = 0
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "root resolution: both install shapes + git boundary (S1/AC1)",
            lambda: test_install_prefix_resolution(Path(td)),
        )
    # FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
    if os.environ.get("FOREIGN_PREFIX_PROBE") == "1":
        print("foreign-prefix-probe: stopped after 1 arm")
        print("FAIL (1 assertions)" if failures else "PASS (1 assertions)")
        return 1 if failures else 0
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "unadopted root refuses, naming root + kit dir (AC2)",
            lambda: test_require_adopted_root_refuses(Path(td)),
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "both CLIs refuse through main(), printing no result (AC2)",
            lambda: test_clis_refuse_an_unadopted_root(Path(td)),
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "gate template finds the kit at any prefix (S5/AC5)",
            lambda: test_gate_template_finds_the_kit(Path(td)),
        )
    failures += check("kit commits to abspath, never resolve() (review B2)", test_kit_commits_to_abspath)
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "gate kit-search stops at the project boundary (review M1)",
            lambda: test_gate_template_boundary(Path(td)),
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "printed remedies name real paths; the remedy runs (TOOL-aRootedPrefix-2)",
            lambda: test_remedy_paths_are_real(Path(td)),
        )
    failures += check_guarded("js definition probe ⊇ the lexicon's own set (TOOL-dClosedLexicon-12)",
                      test_js_probe_against_the_lexicon)
    failures += check("coverage both directions + ratchet guards", test_coverage_directions)
    failures += check("dossier contract fails loud", test_parse_contract)
    failures += check("attribution: keyed > globs, posix, case-sensitive", test_attribution)
    failures += check("renders deterministic + keys-only + round-trip", test_renders_round_trip_and_determinism)
    failures += check("glob brackets fail loud; [[]-escape matches", test_glob_brackets_fail_loud_and_escape_works)
    failures += check(
        "symbols.json deterministic + fail-closed render", test_symbols_render_deterministic_and_fail_closed
    )
    failures += check("feature cards: fence-only, capped, cut counted (TOOL-aMendedFleet-43)", _test_feature_cards)
    failures += check("typed counts: prose digits of inventory nouns, frozen pass (TOOL-aMendedFleet-44)", _test_typed_counts)
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "extractor helpers fail closed", lambda: test_extractor_helpers_fail_closed(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "symbol extractors fail closed (ast + enum floor)", lambda: test_symbol_extractors_fail_closed(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check("conf restricted grammar", lambda: test_conf_grammar(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "affordance graced presence + shrink-only exempt", lambda: test_affordance_graced_presence(Path(td))
        )
    failures += check("affordance exemption drop on touch (S4a / AC1)", test_affordance_exemption_drop)
    with tempfile.TemporaryDirectory() as td:
        failures += check("seed-affordances worklist (S4b / AC5)", lambda: test_seed_affordances(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check("install sites: copies counted, the canonical source left out",
                          lambda: _test_install_sites(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "reuse-lookup shared primitives (stems + fan-in + threshold)", lambda: test_reuse_shared_primitives(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check("reuse-lookup shortlist (AC3 fixture)", lambda: test_reuse_lookup(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "the neighbour cap slices the RANKED pool, not the alphabetical one",
            lambda: test_neighbour_cap_ranks_before_truncating(Path(td)),
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "the same-kind neighbour arm is directory-scoped, both directions",
            lambda: test_neighbour_predicate_is_directory_scoped(Path(td)),
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "the map log row records the sources it showed, capped and never fatal",
            lambda: test_lookup_row_carries_sources(Path(td)),
        )
    failures += check("fan-in subtracts every definer (S1)", test_fan_in_subtracts_every_definer)
    failures += check("rank_harness: control and measurement share a denominator (review F5)",
                      test_the_control_and_the_measurement_share_a_denominator)
    failures += check("replay-phrases: a miss predictor needs a separable AUC AND enough misses",
                      test_miss_predictor_verdict_needs_enough_misses)
    failures += check("gen_map: every advertised read-only mode runs (review F1)",
                      test_every_advertised_gen_map_mode_runs)
    with tempfile.TemporaryDirectory() as td:
        failures += check("dark layers: present layers see outside the symbol roots (review F2)",
                          lambda: test_present_layers_see_outside_the_symbol_roots(Path(td)))
    failures += check("dark layers: no scan is not an empty corpus (review F3)",
                      test_no_scan_is_not_an_empty_corpus)
    with tempfile.TemporaryDirectory() as td:
        failures += check("gate-coverage: a GATE_FILE naming nothing REFUSES (review F6)",
                          lambda: test_gate_coverage_refuses_a_gate_file_that_names_nothing(Path(td)))
    failures += check("dark layers: an undeclared layer refuses with both remedies (AC1)",
                      test_undeclared_layer_refuses_with_both_remedies)
    failures += check("dark layers: the banner is derived, not declared (AC2/AC4)",
                      test_declared_layer_is_named_dark_in_the_banner)
    failures += check("dark layers: a stale declaration is reported (AC3)",
                      test_stale_declaration_is_reported_not_honoured)
    failures += check("dark layers: the legacy spelling refuses (AC6)",
                      test_legacy_language_name_refuses_and_names_the_extension)
    failures += check_guarded("dark layers: every declared layer is present here (AC5)",
                              test_every_declared_layer_is_present_on_this_tree)
    with tempfile.TemporaryDirectory() as td:
        failures += check("shell layer: public definitions only, untokenizable refuses (aMendedFleet-35)",
                          lambda: test_shell_layer_indexes_public_definitions_only(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check("gate-coverage: an uncompared artifact fails (AC1)",
                          lambda: test_gate_coverage_fails_on_an_uncompared_artifact(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check("gate-coverage: a customised gate passes (AC2)",
                          lambda: test_gate_coverage_passes_a_customised_gate(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check("gate-coverage: an unset GATE_FILE is a named skip (AC3)",
                          lambda: test_gate_coverage_names_its_skip(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check("gate-coverage: a predicate matching nothing REFUSES",
                          lambda: test_gate_coverage_refuses_a_predicate_that_matches_nothing(Path(td)))
    failures += check("gate-coverage: green on this tree",
                      test_gate_coverage_is_green_on_this_tree)
    failures += check("freshness: an orphaned artifact is a refusal (AC2)",
                      test_conditional_tier_refuses_an_orphaned_artifact)
    failures += check("freshness: a NEW conditional tier reports itself (AC1/AC4)",
                      test_a_new_conditional_tier_reports_itself)
    failures += check("gate and template are byte-identical (AC5)",
                      test_the_gate_and_its_template_are_byte_identical)
    failures += check("reuse-lookup: the byte budget keeps the first candidate (aMendedFleet-36)",
                      test_budget_cut_shows_first_and_names_the_rest)
    failures += check("gov-only files withheld on both paths (AC13)",
                      test_gov_only_files_are_withheld_on_both_paths)
    failures += check("scan coverage line cannot go quiet (AC12)",
                      test_scan_coverage_line_cannot_go_quiet)
    failures += check_guarded("every co-defined symbol reaches every definer (AC2)",
                              test_every_co_defined_symbol_reaches_every_definer)
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "stale dossiers: ancestry, whole and by range, map-root excluded (aMendedFleet-37)",
            lambda: test_dossier_staleness_from_git(Path(td)),
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "record roots: code and records split, undeclared and dead named (aMendedFleet-86)",
            lambda: test_record_roots_split_code_from_records(Path(td)),
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "baseline additions: graded against the base, absent base is no comparison (aMendedFleet-40)",
            lambda: test_baseline_additions_from_git(Path(td)),
        )
    failures += check("identifier tokens: one arm per over-strip class", test_identifier_tokens_per_language)
    failures += check_guarded("identifier tokens: corpus recall + precision floors", test_identifier_tokens_corpus_recall)
    # S2 — EXECUTED and SKIPPED reported separately, always. A single number cannot say which of
    # the two it is, and the whole defect this unit closes was a report that could not tell them
    # apart.
    skipped_guarded = [n for n in GUARDED if n in SKIPPED]
    print(f"codebase-map selftest: {len(EXECUTED) - len(SKIPPED)} executed, {len(SKIPPED)} skipped "
          f"({len(skipped_guarded)} of {len(GUARDED)} guarded)")
    if GUARDED and len(skipped_guarded) == len(GUARDED):
        # BOTH guarded arms skipped: the suite measured none of the corpus-calibrated claims and a
        # green line here would be exactly the vacuity this unit removed one level down.
        print("codebase-map selftest: REFUSED — every GUARDED arm skipped, so nothing "
              "corpus-calibrated was measured and a pass would report coverage that does not exist")
        return 1
    print("PASS" if not failures else f"{failures} FAILURE(S)")
    return 1 if failures else 0



# --- S1: fan-in subtracts EVERY definer (TOOL-dTracedLattice-1) -----------------------------------
def test_fan_in_subtracts_every_definer():
    """The S1 core, in the smallest form that can fail.

    A symbol defined in two files had ONE arbitrary definer subtracted, so the other definition
    counted as a reference and the symbol scored fan-in for being defined twice.
    """
    ref = {"repo_root": {"a.py", "b.py", "c.py", "x/repo_root.py", "y/repo_root.py"}}
    both = m.fan_in(ref, "repo_root", {"x/repo_root.py", "y/repo_root.py"})
    one = len(ref["repo_root"] - {"x/repo_root.py"})
    assert both == 3, both
    # The arm is only worth anything if the two readings DIFFER on this fixture; assert that rather
    # than trusting it, or a later fixture edit could make the row pass by finding nothing.
    assert one == 4 and one != both, (one, both)
    # A bare str is REFUSED, not iterated as characters. Python would subtract single letters and
    # return the un-subtracted count — a wrong number with no error at the exact call sites this
    # change corrects.
    try:
        m.fan_in(ref, "repo_root", "x/repo_root.py")
    except TypeError as exc:
        assert "SET of definer paths" in str(exc), str(exc)
    else:
        raise AssertionError("fan_in accepted a bare str instead of refusing it")


def test_every_co_defined_symbol_reaches_every_definer():
    """AC2 — after the name-merge fix, no definition is unreachable.

    Guarded on the committed `symbols.json`: an opt-out repo has none, and this arm grades THIS
    corpus rather than a fixture, so it says so instead of passing on an absent artifact.
    """
    root = m.repo_root()
    gen = m.map_root(root) / "generated" / "symbols.json"
    if not gen.is_file():
        raise Skipped("no committed symbols.json, so there is no corpus to grade")
    rows = json.loads(gen.read_text(encoding="utf-8")).get("symbols", [])
    by_id: dict = {}
    for r in rows:
        by_id.setdefault(r["id"], set()).add(r["file"])
    multi = {k: v for k, v in by_id.items() if len(v) > 1}
    # LIVENESS. On a corpus with no co-defined symbol every assertion below is vacuous, and a green
    # row would report coverage that does not exist. Refuse instead.
    assert multi, ("no symbol in this corpus has more than one definer, so this arm proves nothing "
                   "about the defect it exists to pin")
    corpus = rl.load_corpus(root)
    for sid, files in sorted(multi.items()):
        cand = corpus.candidates.get(sid)
        assert cand is not None, f"{sid} is in symbols.json and absent from the corpus"
        assert set(cand.files) >= files, (sid, sorted(files), sorted(cand.files))


def test_scan_coverage_line_cannot_go_quiet():
    """AC12 — S6's coverage line, and it REDS on any of the three facts going missing.

    Rendered from a synthetic shortlist rather than from a live lookup, so the arm grades the LINE
    rather than this corpus's numbers. Three separate assertions, because a single "line exists"
    check passes while two thirds of it are gone.
    """
    corpus = rl.Corpus(candidates={}, shared_seams={}, symbol_files=[], threshold=3,
                       recall_dark=("sh", "ps1"), has_symbols=True, decisions_by_feature={})
    scan = {"files_scanned": 41, "parse_skips": 2, "extensions": [".py"], "roots": ["tools"]}
    sl = rl.Shortlist("q", [], corpus.recall_dark, corpus.threshold, {}, scan)
    text = rl.render(sl, corpus)
    assert "41 files scanned" in text, text
    assert "2 parse skips" in text, text
    assert "unscanned layers: sh, ps1" in text, text
    # A scan that never ran must SAY so rather than printing zeros, which read as "scanned
    # everything and found nothing".
    quiet = rl.render(rl.Shortlist("q", [], (), corpus.threshold, {}, {}), corpus)
    assert "scan coverage: not run" in quiet, quiet


def test_budget_cut_shows_first_and_names_the_rest():
    """TOOL-aMendedFleet-36 — the byte budget cuts the ranked tail, never the first candidate.

    A synthetic shortlist, so the arm grades the cut rule rather than this corpus's sizes. Staged
    red by deleting the first-candidate exception in `derive_budget_cut`: budget 1 then shows none.
    """
    corpus = rl.Corpus(candidates={}, shared_seams={}, symbol_files=[], threshold=3,
                       has_symbols=True, decisions_by_feature={})
    ranked = [rl.Ranked(rl.Candidate(f"cand{i}", ("symbol",), "function", (f"src/f{i}.py",)),
                        True, 0, "stem match") for i in range(6)]
    sl = rl.Shortlist("q", ranked, (), 3, {}, {})
    shown, n_cut = rl.derive_budget_cut(sl, corpus, 1)
    assert [r.candidate.name for r in shown] == ["cand0"] and n_cut == 5, (shown, n_cut)
    text = rl.render(sl, corpus, 1)
    assert sum(ln.startswith("- cand") for ln in text.splitlines()) == 1, text
    assert ("cut 5 of 6 candidate(s) past the 1-byte budget - rerun with --budget 0 to see them all"
            in text), text
    assert text.rstrip("\n").splitlines()[-1].startswith("Decision:"), text
    full = rl.render(sl, corpus, 0)
    assert sum(ln.startswith("- cand") for ln in full.splitlines()) == 6, full
    assert "\ncut " not in full, full
    # Every budget: the printed head stays within it once more than one candidate is shown, and
    # the shown count never falls as the budget grows. LIVENESS: some budget must cut mid-list.
    prev, partial = 0, False
    for budget in range(1, len(full.encode("utf-8")) + 64, 7):
        shown, n_cut = rl.derive_budget_cut(sl, corpus, budget)
        assert len(shown) >= prev and len(shown) + n_cut == 6, (budget, len(shown), prev)
        head = rl.render(sl, corpus, budget).split("\ncut ")[0] + "\n"
        if n_cut and len(shown) > 1:
            assert len(head.encode("utf-8")) <= budget, (budget, len(head.encode("utf-8")))
        partial |= 1 < len(shown) < 6
        prev = len(shown)
    assert partial, "no budget cut mid-list, so the bound above was never exercised"


def test_gov_only_files_are_withheld_on_both_paths():
    """AC13 — a corpus-specific fixture reaches no adopter, by EITHER install path.

    `kit.toml` declares `include = "**"`, so a new file under this directory ships by default; a
    `project-owned` claim is what withholds it from `govkit apply`. The copy-install path in
    `WIRE-INTO-PROJECT.md` is a plain `cp -r` that never reads `kit.toml`, so it needs its own
    removal row — two carriers, and an omission in either ships the file.

    The population is DERIVED from the descriptor's own `project-owned` claims rather than typed
    here, so a fourth gov-only file added later is covered the day it is claimed. The seed
    destination is excluded by name: `map_extractors.py` is `project-owned` because the adopter
    authors it, and removing it would delete their work.

    WHAT IT DOES NOT CHECK: that a gov-only file was claimed AT ALL. A new corpus-specific file
    claimed in neither carrier is invisible to this arm — that is the ratchet over `include = "**"`
    this review named as a left-shift and it is not built here.
    """
    kit = Path(os.path.abspath(__file__)).parent
    toml = (kit / "kit.toml").read_text(encoding="utf-8")
    claimed: set = set()
    for block in toml.split("[[files]]")[1:]:
        head = block.split("[[", 1)[0]
        if 'role = "project-owned"' not in head:
            continue
        for tok in re.findall(r'"([^"]+)"', head.split("include", 1)[1].split("role", 1)[0]):
            claimed.add(tok)
    claimed -= {"map_extractors.py"}  # the SEED destination: the adopter authors it
    assert claimed, "no project-owned claim in kit.toml, so this arm would prove nothing"
    for expect in ("rank_harness.py", "scen-adversarial.json"):
        assert expect in claimed, f"{expect} is not withheld from `govkit apply` by kit.toml"
    runbook = next((p for p in kit.parents if (p / ".git").exists()), kit.parent.parent) / "WIRE-INTO-PROJECT.md"
    if not runbook.is_file():
        raise Skipped("WIRE-INTO-PROJECT.md is not in this tree (an adopter's copy of the kit)")
    text = runbook.read_text(encoding="utf-8")
    rm_lines = [ln for ln in text.splitlines() if "rm -f" in ln and "codebase-map" in ln]
    assert rm_lines, "the runbook has no codebase-map removal row at all"
    joined = " ".join(rm_lines)
    for name in sorted(claimed):
        assert name in joined, (f"{name} is withheld from `govkit apply` but the copy-install "
                                f"runbook never removes it: {joined}")


def _load_gate_module():
    """The gate file, imported by path. It is not importable by name (a hyphenated kit dir), and
    gov's own `GATE_FILE` points inside this directory, so there is one copy to grade."""
    import importlib.util
    path = Path(os.path.abspath(__file__)).parent / "test_codebase_map.py"
    spec = importlib.util.spec_from_file_location("_gate_under_test", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _run_gate(gate, *, empty_symbols=False):
    """Run the freshness gate against the REAL map tree, optionally with an empty symbol
    population. Returns `(assertion_text_or_None, stdout)`.

    No temp map root: the unconditional tiers need a real dossier tree, and faking one would grade
    a fixture rather than the gate. What is faked is exactly the one input under test.
    """
    import contextlib, io as _io
    # The ONE attribute under test is swapped on the real extractor module and restored in
    # `finally`. A proxy class was tried first and its `__getattr__` is graded by the naming leg,
    # which has no row for a dunder — so the smaller change is also the one that does not argue
    # with a gate about a method Python named.
    had = hasattr(gate.ext, "all_symbols")
    real_all = getattr(gate.ext, "all_symbols", None)
    if empty_symbols:
        gate.ext.all_symbols = list
    out, err = _io.StringIO(), None
    try:
        with contextlib.redirect_stdout(out):
            gate.test_generated_artifacts_are_fresh()
    except AssertionError as exc:
        err = str(exc)
    finally:
        if empty_symbols:
            if had:
                gate.ext.all_symbols = real_all
            else:
                del gate.ext.all_symbols
    return err, out.getvalue()


def test_conditional_tier_refuses_an_orphaned_artifact():
    """AC2 — an empty population WITH a committed artifact is a REFUSAL, not a silent pass.

    That pairing means the extractor went dark under a file it can no longer justify, and before
    this unit the gate passed over it: `if symbols:` with no `else` compares nothing and returns.
    """
    gate = _load_gate_module()
    err, out = _run_gate(gate, empty_symbols=True)
    assert err and "DARK symbol tier" in err, (err, out)
    assert "symbols.json" in err and "regen" in err, err


def test_a_new_conditional_tier_reports_itself():
    """AC1 and AC4 in one arm, because they are one mechanism.

    AC4 first: `symbols.json` was the ONLY conditional tier when this was written (7ad94fbb2,
    2026-09-06), so a criterion that enumerated the tiers would grade a population of one and could
    not fail. This introduces a SECOND tier in
    a fixture and asserts it is reported with no reporting line written for it — the list IS the
    mechanism. AC1 rides on it: that tier's artifact does not exist, so its empty population is a
    NAMED skip and not a refusal, which is the legal state an adopter declaring no such extractor
    is in.
    """
    gate = _load_gate_module()
    real = list(gate.CONDITIONAL_TIERS)
    gate.CONDITIONAL_TIERS.append(("widget", "all_widgets", "widgets.json", "render_symbols_json"))
    try:
        err, out = _run_gate(gate)
        assert "skipped widget tier" in out, (out, err)
        assert "widgets.json" in out and "NOTHING WAS COMPARED" in out, out
        assert err is None, f"a tier with no committed artifact must not refuse: {err}"
    finally:
        gate.CONDITIONAL_TIERS[:] = real


def test_the_gate_and_its_template_are_byte_identical():
    """AC5 — editing one and not the other ships a divergence no adopter ever sees corrected."""
    kit = Path(os.path.abspath(__file__)).parent
    a = (kit / "test_codebase_map.py").read_bytes()
    b = (kit / "test_codebase_map.template.py").read_bytes()
    assert a == b, ("the installed gate and its template have diverged; "
                    f"{len(a)} vs {len(b)} bytes")


# --- the adopter's frozen gate is compared against the engine (TOOL-dTracedLattice-4) -------------
def _run_gate_coverage(gate_text, tmp: Path, *, name="test_codebase_map.py"):
    """Run the real check against a FIXTURE installed gate. Returns `(exit, stdout, stderr)`."""
    import contextlib, io as _io
    path = None
    if gate_text is not None:
        path = tmp / name
        path.write_text(gate_text, encoding="utf-8")
    real = cg.resolve_gate_path
    cg.resolve_gate_path = lambda root: path
    out, err = _io.StringIO(), _io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = cg.main([])
    finally:
        cg.resolve_gate_path = real
    return code, out.getvalue(), err.getvalue()


def test_gate_coverage_fails_on_an_uncompared_artifact(tmp: Path):
    """AC1 — an installed gate missing a tier the engine writes FAILS, naming the artifact."""
    frozen = 'fresh = {gen_dir / "inventories.json": x, gen_dir / "MAP.md": y}\n'
    code, out, err = _run_gate_coverage(frozen, tmp)
    assert code == 1, (code, out, err)
    assert "symbols.json" in err, err
    assert "does not compare" in err, err
    # It must say what it CANNOT decide, or the report reads as a verdict about the adopter.
    assert "CANNOT TELL A DELIBERATE OMISSION" in err, err


def test_gate_coverage_passes_a_customised_gate(tmp: Path):
    """AC2 — a gate that covers every artifact passes even when it differs byte-for-byte.

    A project is entitled to edit its gate. Reporting a diff would report customisation as
    staleness, which is the reason this check compares SETS and not bytes.
    """
    customised = ('# a project comment the template does not have\n'
                  'fresh = {gen_dir / "inventories.json": x, gen_dir / "MAP.md": y}\n'
                  'CONDITIONAL_TIERS = [\n'
                  '    ("symbol", "all_symbols", "symbols.json", "render_symbols_json"),\n'
                  ']\n'
                  'def extra_project_arm(): pass\n')
    code, out, err = _run_gate_coverage(customised, tmp)
    assert code == 0, (code, out, err)
    assert "names every one" in out, out
    assert "customise" in out, out


def test_gate_coverage_names_its_skip(tmp: Path):
    """AC3 — an unset or absent GATE_FILE is a NAMED skip, never a silent pass."""
    code, out, err = _run_gate_coverage(None, tmp)
    assert code == 0, (code, out, err)
    assert "skipped" in out and "GATE_FILE" in out, out
    # It still names what the engine writes, so the skip is informative rather than a shrug.
    assert "symbols.json" in out, out


def test_gate_coverage_refuses_a_predicate_that_matches_nothing(tmp: Path):
    """The liveness refusal: a stale predicate would report every gate as complete.

    That is the vacuous-selector shape, and a check that cannot distinguish "covered" from "matched
    nothing" is worse than no check because it is cited as coverage.
    """
    import re as _re
    real_art, real_tier = cg.ARTIFACT_RE, cg.TIER_RE
    cg.ARTIFACT_RE = _re.compile(r"(?!x)x")
    cg.TIER_RE = _re.compile(r"(?!x)x")
    try:
        code, out, err = _run_gate_coverage('fresh = {}\n', tmp)
    finally:
        cg.ARTIFACT_RE, cg.TIER_RE = real_art, real_tier
    assert code == 2, (code, out, err)
    assert "REFUSED" in err and "predicate" in err, err


def test_gate_coverage_is_green_on_this_tree():
    """gov is its own adopter here: GATE_FILE points inside the kit dir, so the shipped pair is
    graded on every run rather than only in a fixture."""
    code = cg.main([])
    assert code == 0, "this repo's own installed gate does not compare every engine artifact"


# --- dark layers are DERIVED, not asserted (TOOL-dTracedLattice-5) --------------------------------
SCAN_FIXTURE = {"extensions": [".py"], "present_extensions": [".py", ".sh"],
                "present_counts": {".py": 47, ".sh": 85}, "files_scanned": 47, "parse_skips": 0}


def test_undeclared_layer_refuses_with_both_remedies():
    """AC1 / S3 — the refusal names the layer, its file count, and BOTH ways to clear it.

    Rev-4 graded two of the three. A refusal that names a problem and no repair is what §5's risks
    row forbids: an adopter meets it and has nowhere to go.
    """
    v = rl.derive_layer_verdict(SCAN_FIXTURE, ())
    text = rl.render_layer_refusal(v)
    assert ".sh" in text, text
    assert "85 file(s)" in text, text
    assert "register an extractor" in text, text
    assert "RECALL_DARK_LAYERS" in text, text
    # And it must NOT fire once the layer is declared, or the remedy it prints does not work.
    assert rl.render_layer_refusal(rl.derive_layer_verdict(SCAN_FIXTURE, (".sh",))) == ""


def test_declared_layer_is_named_dark_in_the_banner():
    """AC2 / AC4 / S4 — the banner's dark set is DERIVED from the corpus walk, not from the conf.

    This unit owns that wording outright: `TOOL-dTracedLattice-1` grades no banner content, and an
    ungraded handover between two sequenced units is what M6 clause 3 exists to catch.
    """
    corpus = rl.Corpus(candidates={}, shared_seams={}, symbol_files=[], threshold=3,
                       recall_dark=(".sh",), has_symbols=True, decisions_by_feature={})
    sl = rl.Shortlist("q", [], corpus.recall_dark, corpus.threshold, {}, SCAN_FIXTURE)
    text = rl.render(sl, corpus)
    assert "unscanned layers: .sh" in text, text
    # DERIVED means the conf cannot make it lie: declare something absurd and the banner is unmoved.
    lying = rl.Corpus(candidates={}, shared_seams={}, symbol_files=[], threshold=3,
                      recall_dark=(".nonexistent",), has_symbols=True, decisions_by_feature={})
    text2 = rl.render(rl.Shortlist("q", [], lying.recall_dark, 3, {}, SCAN_FIXTURE), lying)
    assert "unscanned layers: .sh" in text2, text2
    assert ".nonexistent" not in text2, text2


def test_stale_declaration_is_reported_not_honoured():
    """AC3 — a declared layer absent from the corpus is a STALE declaration, not a dark layer."""
    v = rl.derive_layer_verdict(SCAN_FIXTURE, (".sh", ".rb"))
    assert v["stale"] == [".rb"], v
    assert v["undeclared"] == [], v
    # Stale is a REPORT, never a refusal: it costs an adopter nothing and blocks nothing.
    assert rl.render_layer_refusal(v) == "", v


def test_legacy_language_name_refuses_and_names_the_extension():
    """AC6 / S6 — the migration. An old value is REFUSED, never reinterpreted.

    Reading `bash` as `.sh` is right on this tree and wrong for `c` or `go`, and an adopter whose
    conf still carries the old spelling has to be told rather than guessed at.
    """
    v = rl.derive_layer_verdict(SCAN_FIXTURE, ("bash",))
    text = rl.render_layer_refusal(v)
    assert "OLD language-name spelling" in text and "bash" in text, text
    assert ".sh" in text, "the refusal must name the uncovered layers it could be"
    # The legacy check leads: a conf carrying both an old and a new value is still a migration.
    both = rl.render_layer_refusal(rl.derive_layer_verdict(SCAN_FIXTURE, ("bash", ".sh")))
    assert "OLD language-name spelling" in both, both


def test_every_declared_layer_is_present_on_this_tree():
    """AC5 — over THIS repo's own conf, not a fixture. It reddened against the shipped `bash`
    value before the migration landed, which is the observation the criterion asks for."""
    root = m.repo_root()
    declared = tuple(t for t in (m.load_conf(root).get("RECALL_DARK_LAYERS", "")).replace(",", " ").split() if t)
    corpus = rl.load_corpus(root)
    scan: dict = {}
    m.build_reference_index(corpus.symbol_files, root=root, stats=scan)
    present = set(scan.get("present_extensions", ()))
    assert present, "the walk found no definition-carrying layer at all, so this arm proves nothing"
    for token in declared:
        assert token.startswith("."), f"{token} is the OLD language-name spelling"
        assert token in present, f"{token} is declared dark and is not present in the corpus"


def test_shell_layer_indexes_public_definitions_only(tmp: Path):
    """TOOL-aMendedFleet-35 S1/S2 — the project-owned `kit-sh` layer, over a fixture root.

    A public definition is indexed; a `_`-private one and a function inside a heredoc body are not;
    an untokenizable file raises MapError naming it rather than yielding a smaller index.
    """
    import map_extractors as mx
    good, bad = tmp / "good", tmp / "bad"
    good.mkdir()
    bad.mkdir()
    (good / "lib.sh").write_text(
        "build_thing() {\n  echo hi\n}\n_private_helper() {\n  :\n}\n"
        "cat <<'EOF'\nfunction embedded() { return 1; }\nEOF\n", encoding="utf-8")
    (bad / "broken.sh").write_text('f() {\n  echo "oops\n}\n', encoding="utf-8")
    rows = mx.scan_shell_layer("kit-sh", (good,), root=tmp)
    assert rows == [{"id": "build_thing", "kind": "function", "file": "good/lib.sh"}], rows
    try:
        mx.scan_shell_layer("kit-sh", (bad,), root=tmp)
    except m.MapError as exc:
        assert "bad/broken.sh" in str(exc), exc
    else:
        raise AssertionError("an untokenizable shell file was indexed as nothing, not refused")


# --- left-shifts from the closing diff review (dTracedLattice round 1) ----------------------------
def test_every_advertised_gen_map_mode_runs():
    """F1's class, not F1's line. `--seed-affordances` shipped BROKEN through a data-model rename
    because the only arm covering it drove the library function and never the printer, and its own
    docstring conceded "the CLI is thin glue over this". A suite green over a dead entrypoint is the
    green-by-absence shape.

    READ-ONLY modes only, in a subprocess against the real tree. `--write` and the three seeding
    modes mutate, and running them here would make the suite a writer; they are exercised by the
    build's own regen and by `codebase-map adopter e2e`. Stated rather than implied: this arm covers
    `--check` and `--seed-affordances`, and those are the two whose output is a PRINTER over the
    candidate data model, which is the surface the rename broke.
    """
    import subprocess
    kit = Path(os.path.abspath(__file__)).parent
    # `prints` says whether the mode has a PRINTER at all: `--check` is a gate and is silent
    # when it passes, so asserting output there would grade the wrong thing and red on a clean
    # tree.
    for argv, prints in ((["--check"], False), (["--seed-affordances", "--top", "3"], True)):
        proc = subprocess.run([sys.executable, str(kit / "gen_map.py"), *argv],
                              capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(m.repo_root()))
        assert proc.returncode == 0, f"gen_map.py {' '.join(argv)} exited {proc.returncode}\n{proc.stderr}"
        assert "Traceback" not in proc.stderr, proc.stderr
        if prints:
            assert proc.stdout.strip(), f"gen_map.py {' '.join(argv)} printed nothing"
            # A CANDIDATE ROW, not the header. `_seed_affordances` prints its
            # `# seed-affordances: top N ...` line unconditionally and BEFORE the loop that
            # crashed, so a needle satisfied by the header greens over a printer that never ran —
            # verified with `--top 0`: exit 0, header, zero rows, arm passes.
            rows = [ln for ln in proc.stdout.splitlines()
                    if ln.startswith("- ") and "fan-in" in ln]
            assert rows, (
                "the header printed and no candidate row followed it, so the printer this arm "
                f"exists to exercise never ran:\n{proc.stdout}")


def test_present_layers_see_outside_the_symbol_roots(tmp: Path):
    """F2's class. The tally used to sit inside a walk over the SYMBOL corpus's top-level dirs, so a
    layer in any other directory was never counted present — and everything downstream reads "not
    counted" as "not there", which turns a dark-layer check into an affirmative claim that every
    present layer is covered.

    The fixture is shaped like the repro: symbols under `src/`, an unextracted layer under `web/`.
    """
    (tmp / "src").mkdir()
    (tmp / "web").mkdir()
    (tmp / "src" / "text.py").write_text("def build_slug():\n    return 1\n", encoding="utf-8")
    (tmp / "web" / "text.ts").write_text("export function buildSlug() { return 1 }\n", encoding="utf-8")
    present = m.derive_present_layers(tmp)
    assert present.get(".ts") == 1, (
        "a layer outside the symbol corpus's roots is invisible to the present-layer tally, so the "
        f"dark-layer check would report it covered: {present}")
    assert present.get(".py") == 1, present
    # AND THE CALL SITE, which is where the defect lived: the helper can be correct while
    # `build_reference_index` still fills `stats` from its own roots-scoped loop. Symbols under
    # `src/` only, so `roots == ['src']` and the `.ts` under `web/` is reachable ONLY through the
    # widened population.
    stats: dict = {}
    m.build_reference_index(["src/text.py"], root=tmp, stats=stats)
    assert ".ts" in stats.get("present_extensions", ()), (
        "build_reference_index still reports the roots-scoped population, so every reader of "
        f"`stats` sees the old answer however correct the helper is: {stats}")
    # And the verdict built from it must REFUSE rather than report the correct declaration stale.
    scan = {"extensions": [".py"], "present_extensions": sorted(present),
            "present_counts": present, "files_scanned": 1, "parse_skips": 0}
    v = rl.derive_layer_verdict(scan, ())
    assert v["undeclared"] == [".ts"], v
    assert rl.render_layer_refusal(v), "an undeclared present layer must refuse"


def test_no_scan_is_not_an_empty_corpus():
    """F3's class. An empty-seed query and a corpus with no symbol file list both skip the walk, and
    reading that as "no layer is present" marked every correct declaration STALE and told the
    operator to delete the one thing protecting them."""
    v = rl.derive_layer_verdict({}, (".sh",))
    assert v["stale"] == [], v
    assert v["undeclared"] == [], v
    assert rl.render_layer_refusal(v) == "", v
    # The MIGRATION check still fires: it reads the declaration only, and a legacy value is owed a
    # refusal whether or not a walk ran.
    assert rl.derive_layer_verdict({}, ("bash",))["legacy"] == ("bash",)


def test_gate_coverage_refuses_a_gate_file_that_names_nothing(tmp: Path):
    """F6's class. "GATE_FILE unset" and "GATE_FILE names a path that is not there" were one return
    value and one exit 0 — a benign state and a broken configuration reported identically."""
    # FIRST, the function F6 actually changed. Monkeypatching it away and asserting on `main`
    # alone left the whole suite green with the resolver half reverted, which is the arm grading a
    # stand-in for the thing under test.
    (tmp / "tests").mkdir()
    (tmp / ".codebase-map.conf").write_text(
        "MAP_ROOT=map\nGATE_FILE=tests/moved_gate.py\n", encoding="utf-8")
    resolved = cg.resolve_gate_path(tmp)
    assert resolved is not None, (
        "a GATE_FILE that is SET must not resolve to None; that collapses a broken configuration "
        "into the benign unset state")
    assert not resolved.is_file() and resolved.name == "moved_gate.py", resolved

    missing = tmp / "tests" / "moved_gate.py"
    real = cg.resolve_gate_path
    cg.resolve_gate_path = lambda root: missing
    import contextlib, io as _io
    out, err = _io.StringIO(), _io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = cg.main([])
    finally:
        cg.resolve_gate_path = real
    assert code == 2, (code, out.getvalue(), err.getvalue())
    assert "does not exist" in err.getvalue(), err.getvalue()
    assert "not the benign unset state" in err.getvalue(), err.getvalue()


def test_the_control_and_the_measurement_share_a_denominator():
    """F5's class. `measure_recall` divides by the LIVE scenarios; the constant control divided by
    ALL rows, so a dead probe shrank one rate and not the other and the comparison flattered the
    ranking. A control that is not comparable is not a control.
    """
    import importlib.util
    kit = Path(os.path.abspath(__file__)).parent
    spec = importlib.util.spec_from_file_location("_rank_harness", kit / "rank_harness.py")
    rh = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rh)
    # DERIVED, not spelled: a kit file naming its own install path by literal is what the
    # carried-prefix ban exists to stop, and an arm is a shipped file like any other.
    # Row A's target is one of the repo's most-CHANGED files, so the churn control HITS it and the
    # two denominators give different numbers; row B's target is absent, so it is a DEAD probe and
    # is the difference between them. Both properties are asserted below rather than assumed.
    rows = [{"id": "A", "query": "q", "expected_file": "memory/backlog/TOOL.md"},
            {"id": "B", "query": "q", "expected_file": "no/such/file/anywhere.py"}]
    scored, dead = rh.measure_ranks(rows, m.repo_root())
    assert dead == ["B"], f"the fixture must carry a DEAD probe or this arm proves nothing: {dead}"
    assert len(scored) == 1, scored
    # THE RENDERED REPORT, which is the CALL SITE. The first cut of this arm rebuilt the filter
    # inside the test and asserted the rebuild agreed with itself — a tautology that stayed
    # green with the shipped fix reverted. What has to hold is that the line a reader sees uses
    # the same denominator the measured rate does.
    import types
    live_rows = rh.derive_live_rows(rows, scored)
    assert len(live_rows) == len(scored) == 1 and live_rows[0]["id"] == "A", (live_rows, scored)
    args = types.SimpleNamespace(scenarios="<fixture>", control="constant", trials=1, k=20)
    text = rh.render_report(rows, scored, dead, args, m.repo_root())
    # The control is scored over ONE live row here. Over both rows the same hit count divides by
    # two, so the two spellings cannot print the same number unless the fix is in place.
    want = rh.run_constant_control(live_rows, m.repo_root(), 20)
    other = rh.run_constant_control(rows, m.repo_root(), 20)
    assert want != other, (
        "the fixture does not discriminate between the two denominators, so this arm would "
        f"pass on either implementation: {want} vs {other}")
    assert f"{want:.3f}" in text, (
        "the constant control was scored over a different population than `measure_recall` "
        f"divides by:\n{text}")


def test_miss_predictor_verdict_needs_enough_misses():
    """TOOL-aMendedFleet-46 S7. Canned rows, no corpus: a separable predictor and an inseparable
    one through `derive_auc`, then `derive_predictor_verdict` over a population that clears the
    floor and one ONE miss short of it. The second is the arm's point: an AUC read off too few
    misses must never name a predictor, however far it sits from chance.
    """
    import importlib.util
    kit = Path(os.path.abspath(__file__)).parent
    spec = importlib.util.spec_from_file_location("_replay_phrases", kit / "replay-phrases.py")
    rp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rp)
    floor = rp.PREDICTOR_MIN_LABELS
    vals = {p: 0 for p in rp.PREDICTORS}
    # n_seeds separates the labels perfectly; q_len is one value on both sides
    rows = ([dict(vals, hit=True, n_seeds=5, q_len=3) for _ in range(floor + 10)]
            + [dict(vals, hit=False, n_seeds=1, q_len=3) for _ in range(floor + 10)])
    assert rp.derive_auc([3, 4, 5], [0, 1, 2]) == 1.0
    assert rp.derive_auc([1, 1, 1], [1, 1, 1]) == 0.5
    assert rp.derive_auc([1], []) is None, "an empty side has no AUC, never a chance reading"
    pop = rp.measure_population("all", rows)
    assert pop["aucs"]["n_seeds"] == 1.0 and pop["aucs"]["q_len"] == 0.5, pop["aucs"]
    assert pop["band"] and pop["band"][1] < 1.0, f"the shuffled band must sit below 1.0: {pop}"
    verdict = rp.derive_predictor_verdict([pop])
    assert verdict.startswith("n_seeds ("), verdict
    short = dict(pop, misses=floor - 1)
    verdict = rp.derive_predictor_verdict([short])
    assert verdict.startswith("none qualifies") and "too few misses" in verdict, verdict


if __name__ == "__main__":
    sys.exit(main())
