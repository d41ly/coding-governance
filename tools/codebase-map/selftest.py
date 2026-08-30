"""codebase-map kit self-test — exercises the pure engine with fixtures (stdlib only).

    python <kit>/selftest.py        # exit 0 = the kit's contract holds

These are the red-path proofs: an unclaimed key, a stale claim, a stale/lazy baseline line,
and every malformed-dossier class must FAIL LOUD; multi-claim, case-sensitivity, and
backslash normalization must behave identically on every platform.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# `abspath`, NOT `resolve()`: this insert decides which path string `map_lib.__file__` carries,
# and map_lib.kit_dir()/the gate template both use abspath. Under a junctioned kit dir resolve()
# yields the LINK TARGET, so this entrypoint would stamp one prefix into the byte-compared
# artifacts while the gate re-renders another — a permanently STALE gate whose own printed
# remedy re-writes the wrong spelling and never converges (measured).
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent))

import map_lib as m  # noqa: E402
import reuse_lookup as rl  # noqa: E402

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


def check(name, fn):
    try:
        fn()
        print(f"ok   {name}")
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
        kit = root / prefix / "codebase-map" if prefix else root / "codebase-map"
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
    # --- a PREFIXED install: <root>/tools/codebase-map/ (the defect this closes) ---------------
    kit_b = tree("b", "tools", conf=True)
    assert m.resolve_root(kit_b) == tmp / "b"
    assert m.resolve_root(kit_b) != tmp / "b" / "tools", "resolved to the OLD grandparent answer"
    # both roots hold the conf AND .git, so this also pins the ORDER: the conf is tested first,
    # else the boundary would break the walk at the root and hand back the kit dir's parent.
    # --- the walk is not capped at one segment ------------------------------------------------
    assert m.resolve_root(tree("c", "x/y", conf=True)) == tmp / "c"
    # --- no conf anywhere -> the grandparent convention, unchanged from the old rule -----------
    assert m.resolve_root(tree("d", "tools", conf=False)) == tmp / "d" / "tools"
    assert m.resolve_root(tree("e", "", conf=False)) == tmp / "e"  # a root install is unaffected

    # --- the .git boundary: a conf in a PARENT tree is a DIFFERENT checkout --------------------
    # Worktrees are commonly kept inside the primary tree (this repo uses .claude/worktrees/<n>/),
    # so an unbounded walk would resolve a worktree's map into the primary tree's MAP_ROOT.
    primary = tmp / "primary"
    (primary / ".git").mkdir(parents=True)
    (primary / m.CONF_NAME).write_text("MAP_ROOT=memory/map\n", encoding="utf-8")
    wt_kit = tree("primary/.claude/worktrees/w", "tools", conf=False, git="file")
    wt = primary / ".claude" / "worktrees" / "w"
    assert m.resolve_root(wt_kit) == wt / "tools", "the walk escaped the worktree into the primary tree"
    (wt / m.CONF_NAME).write_text("MAP_ROOT=memory/map\n", encoding="utf-8")
    assert m.resolve_root(wt_kit) == wt  # the worktree's OWN conf resolves it

    # --- nearest conf wins (a repo vendored inside another adopting repo) ----------------------
    inner = tmp / "nest" / "inner"
    (inner / "tools" / "codebase-map").mkdir(parents=True)
    (tmp / "nest" / m.CONF_NAME).write_text("MAP_ROOT=outer\n", encoding="utf-8")
    (inner / m.CONF_NAME).write_text("MAP_ROOT=inner\n", encoding="utf-8")
    assert m.resolve_root(inner / "tools" / "codebase-map") == inner

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
    `no seam fits` or a `collision_flags: 0` on stdout is the confident-empty-answer this closes."""
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

        _sys.argv = ["map_diff.py", "HEAD~1..HEAD", "--converge"]
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = md.main()
        assert rc == 2, f"map_diff exited {rc}, not a refusal"
        assert "refused" in err.getvalue(), err.getvalue()
        assert "collision_flags" not in out.getvalue(), out.getvalue()
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

    # (a) PREFIXED kit, gate collected somewhere else entirely — the shape the old walk missed
    r1 = tmp / "g1"
    got = probe(r1, r1 / "tools" / "codebase-map", r1 / "tests")
    assert got.returncode == 0, got.stderr
    assert Path(got.stdout.strip()) == r1 / "tools" / "codebase-map", got.stdout

    # (b) gate installed INSIDE the kit dir (a repo with no test collector wires it as a leg)
    r2 = tmp / "g2"
    got = probe(r2, r2 / "tools" / "codebase-map", r2 / "tools" / "codebase-map")
    assert got.returncode == 0, got.stderr
    assert Path(got.stdout.strip()) == r2 / "tools" / "codebase-map", got.stdout

    # (c) root install — the original convention, unchanged
    r3 = tmp / "g3"
    got = probe(r3, r3 / "codebase-map", r3 / "tests")
    assert got.returncode == 0, got.stderr
    assert Path(got.stdout.strip()) == r3 / "codebase-map", got.stdout

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
    plant = tmp / "outside" / "codebase-map"
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
    naming `codebase-map/gen_map.py` at a `tools/`-prefixed install is a dead end at exactly the
    moment someone is stuck.

    Two halves. The pure half pins `relative_kit` across install shapes and pins the legacy
    `REGEN_CMD` constant EQUAL to the accessor's root-install answer, so the last hardcoded
    spelling cannot drift from the computed one. The end-to-end half is the real acceptance: build
    a prefixed install, stale an artifact, then RUN THE COMMAND THE GATE PRINTED, verbatim, and
    require that it fixes the staleness — no hardcoded expectation of what the remedy should say."""
    import os
    import re
    import shutil
    import subprocess
    import sys as _sys

    # --- pure: the kit dir as a human must spell it from the repo root -------------------------
    root = tmp / "r"
    assert m.relative_kit(root / "codebase-map", root) == "codebase-map"
    assert m.relative_kit(root / "tools" / "codebase-map", root) == "tools/codebase-map"
    assert m.relative_kit(root / "a" / "b" / "codebase-map", root) == "a/b/codebase-map"
    assert "\\" not in m.relative_kit(root / "tools" / "codebase-map", root)  # POSIX on Windows too
    # not under the root (a CODEBASE_MAP_ROOT pointed at a fixture): the bare NAME, so a render
    # never embeds an absolute temp path and fixture bytes stay deterministic.
    assert m.relative_kit(tmp / "elsewhere" / "codebase-map", root) == "codebase-map"
    # the legacy constant IS the accessor's root-install answer — one fact, not two.
    assert m.REGEN_CMD == f"python {m.relative_kit(root / 'codebase-map', root)}/gen_map.py --write"

    # --- end-to-end: the printed remedy, executed --------------------------------------------
    repo = tmp / "e2e"
    kit = repo / "tools" / "codebase-map"
    kit.parent.mkdir(parents=True)
    shutil.copytree(Path(os.path.abspath(__file__)).parent, kit)
    (repo / ".git").mkdir()
    # H2: the conf carries the EXAMPLE's stale MAP_DIFF_CMD, which is what the documented adoption
    # path leaves behind (`cp` the example, THEN run the adopter — so the adopter's create-branch
    # stamp never fires). A truthy-but-dead value must not beat the prefix-correct fallback.
    (repo / m.CONF_NAME).write_text(
        'MAP_ROOT=memory/map\nMAP_DIFF_CMD="python codebase-map/map_diff.py"\n', encoding="utf-8"
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

    got = run("tools/codebase-map/gen_map.py", "--scaffold")
    assert got.returncode == 0, got.stdout + got.stderr

    # the scaffolded map README must name the real kit dir, not the convention
    readme = (repo / "memory" / "map" / "README.md").read_text(encoding="utf-8")
    assert "tools/codebase-map/gen_map.py" in readme, readme[:400]
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
    got = run("tools/codebase-map/gen_map.py", "--check")
    assert got.returncode == 1, f"--check did not detect the stale artifact: {got.stdout}"
    printed = re.search(r"regen:\s*python\s+(\S+)\s+--write", got.stdout)
    assert printed, f"no regen remedy printed: {got.stdout}"
    remedy_path = printed.group(1)
    assert (repo / remedy_path).is_file(), f"the remedy names a path that does not exist: {remedy_path}"
    fixed = run(remedy_path, "--write")
    assert fixed.returncode == 0, fixed.stdout + fixed.stderr
    again = run("tools/codebase-map/gen_map.py", "--check")
    assert again.returncode == 0, f"the printed remedy did not fix the staleness: {again.stdout}"

    # the generated artifacts carry the same real prefix (they are the remedy's other home)
    inv = (repo / "memory" / "map" / "generated" / "inventories.json").read_text(encoding="utf-8")
    assert "tools/codebase-map/gen_map.py" in inv, inv[:400]


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


def test_conf_grammar(tmp: Path):
    (tmp / ".codebase-map.conf").write_text(
        '# c\nMAP_ROOT=docs/map\nGATE_FILE="tests/test map.py"\n'
        "export MAP_DIFF_CMD=python\nBAD=docs/map # inline\n",
        encoding="utf-8",
    )
    conf = m.load_conf(tmp)
    assert conf["MAP_ROOT"] == "docs/map"
    assert conf["GATE_FILE"] == "tests/test map.py"  # quoted value keeps its space
    assert conf["MAP_DIFF_CMD"] == "python"  # export prefix normalized
    assert conf["BAD"] == "docs/map"  # unquoted value ends at whitespace, comment can't leak


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
    # Measured on gov's own tools/**/*.js: 30 definitions, 3 indexed export rows, DISJOINT.
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
    assert m.drop_touched_exemptions(exempt, {"UNMAPPED": ["z"], "foundation": ["lib/b.py"]}) == exempt

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
        assert m.fan_in(ref, "slugify", "src/text.py") == 5
        assert m.fan_in(ref, "titlecase", "src/text.py") == 4
        assert m.fan_in(ref, "truncate", "src/text.py") == 3
        assert m.fan_in(ref, "Cache", "src/cache.py") == 1  # below the threshold -> not a seam

        worklist = rl.seed_affordances(corpus, ref, 10)
        # slugify EXCLUDED (already declares a seam) despite fan-in 5; Cache EXCLUDED (fan-in 1 < 3);
        # ranked by fan-in desc.
        assert [c.name for c, _ in worklist] == ["titlecase", "truncate"], worklist
        assert [fi for _, fi in worklist] == [4, 3]
        assert all(c.name != "slugify" for c, _ in worklist)  # nothing already declared
        # --top cap: only the single highest-fan-in undeclared seam
        assert [c.name for c, _ in rl.seed_affordances(corpus, ref, 1)] == ["titlecase"]
    finally:
        del os.environ["CODEBASE_MAP_ROOT"]


def test_reuse_shared_primitives(tmp: Path):
    # --- tokenizer + crude stemmer: the one "shares a token stem" definition (S3 recall / S5 collision)
    assert m.subtokens("getUserID") == ["get", "user", "id"]
    assert m.subtokens("api/x/route.ts") == ["api", "x", "route", "ts"]
    assert m.subtokens("a_flag") == ["a", "flag"]
    assert m.subtokens("HTTPServer") == ["http", "server"]  # acronym run kept, not shredded
    assert m.stems("slugify") == frozenset({"slug"})        # `ify` stripped, NOT down to `y`
    assert m.stems("normalise a name to a slug") & m.stems("slugify") == {"slug"}
    assert not (m.stems("payment gateway") & m.stems("slugify"))  # unrelated -> no shared stem

    # --- fan-in: distinct referencing files minus the def file, comments/strings excluded ----
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
    assert m.fan_in(idx, "slugify", "src/text.py") == 2  # a.py + b.py, minus the def file

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


def test_reuse_lookup(tmp: Path):
    """AC3 on a portable FIXTURE repo (no host-repo paths): a planted `slugify` seam is ranked
    above unrelated symbols for a behaviour query; a no-home query returns 'no seam fits'; and a
    recall-dark layer prints the partial-recall notice so an empty result is never falsely sure."""
    import os

    (tmp / ".codebase-map.conf").write_text(
        'MAP_ROOT=memory/map\nRECALL_DARK_LAYERS="web-ts"\nSEAM_FANIN_THRESHOLD=3\n', encoding="utf-8"
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
        "## Reuse affordance\n"
        "seam: slugify — reuse for name→slug; extend via the transform registry\n"
        "\n"
        "## Shared seams\n"
        "The text module normalises display names into url slugs.\n",
        encoding="utf-8",
    )
    (feats / "glue.md").write_text(  # prose-only feature: `none` affordance, no seam symbol
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
        assert "recall partial: layers web-ts" in out                   # (c) recall-dark announced

        # (b) a no-home query returns "no seam fits" — and STILL flags the recall-dark gap
        sl2 = rl.assemble_shortlist("configure the payment gateway retry budget", corpus, ref)
        assert sl2.empty, [r.candidate.name for r in sl2.ranked]
        out2 = rl.render(sl2, corpus)
        assert "no seam fits" in out2
        assert "recall partial: layers web-ts" in out2  # never a falsely-confident "no seam"

        # `## Shared seams` prose recall: a seam-less feature surfaces via its prose (behavioural
        # recall beyond symbol names), and assembling is IDEMPOTENT (no synthetic leak into corpus).
        before = len(corpus.candidates)
        sl3 = rl.assemble_shortlist("dispatch a webhook", corpus, ref)
        names3 = [r.candidate.name for r in sl3.ranked]
        assert "glue (## Shared seams)" in names3, names3
        assert len(corpus.candidates) == before  # pool copy, not the caller's corpus
    finally:
        del os.environ["CODEBASE_MAP_ROOT"]


def test_detect_collisions_and_backlog(tmp: Path):
    """AC4: on a range that adds `slugify2` (stem-colliding with the high-fan-in `slugify` seam,
    no new edge to it) the closing loop emits ONE collision_flag; a symbol that WIRES THROUGH its
    seam, one whose seam is below threshold, one of a different kind, and one unrelated do NOT
    flag; the backlog dedupes by (new, resembles); and new_clones is a clone-ratchet count, NOT
    dead_exports/affordance_coverage_%. Pure core — the git-range extraction is thin glue tested
    by the scratchpad fixture in the build report."""
    # base seams (present at range base). Constructed reference index -> exact fan-in per seam
    # (the fan_in math itself is proven in test_reuse_shared_primitives; this pins collision logic).
    base = [
        {"id": "slugify", "kind": "function", "file": "src/text.py"},        # reinvented (fan-in 3)
        {"id": "fetchGateway", "kind": "function", "file": "src/gw.py"},     # wired-through (fan-in 3)
        {"id": "parseThing", "kind": "function", "file": "src/parse.py"},    # below threshold (fan-in 1)
        {"id": "Money", "kind": "class", "file": "src/money.py"},            # a class (kind mismatch)
    ]
    ref = {
        "slugify": {"src/a.py", "src/b.py", "src/c.py", "src/text.py"},      # fan-in 3
        "fetchGateway": {"src/d.py", "src/e.py", "src/f.py", "src/gw.py"},   # fan-in 3
        "parseThing": {"src/g.py", "src/parse.py"},                          # fan-in 1 < threshold
        "Money": {"src/money.py"},                                           # fan-in 0
    }
    new = [
        {"id": "slugify2", "kind": "function", "file": "src/new1.py"},       # collides slugify, NOT wired -> FLAG
        {"id": "retryGateway", "kind": "function", "file": "src/new2.py"},   # collides fetchGateway, WIRES through
        {"id": "parseWidget", "kind": "function", "file": "src/new3.py"},    # collides parseThing, but it's < threshold
        {"id": "moneyBag", "kind": "function", "file": "src/new4.py"},       # stem 'money' but Money is a CLASS
        {"id": "helper", "kind": "function", "file": "src/new5.py"},         # unrelated -> no shared stem
    ]
    # the range wires through fetchGateway (new2 references it) — an edge added -> not reinvention;
    # slugify has NO edge added in the range -> slugify2 is reinvention.
    range_index = {"fetchGateway": {"src/new2.py"}}
    flags = m.detect_collisions(new, base, ref, range_index, threshold=3)
    assert [f.new for f in flags] == ["slugify2"], flags               # exactly one collision
    only = flags[0]
    assert only.resembles == "slugify" and only.file == "src/new1.py" and only.fanin == 3
    assert only.kind == "function" and only.confidence == "medium"     # no affordance declared -> medium
    # F8c: when the seam DECLARES an affordance, confidence rises to high.
    hi = m.detect_collisions(new, base, ref, range_index, threshold=3, affordance_seams=frozenset({"slugify"}))
    assert hi[0].confidence == "high"
    # retryGateway stays clean ONLY because the range wired through fetchGateway — drop that edge and
    # it flags, proving the reference-edge check is load-bearing (not dead code). parseWidget/moneyBag
    # stay clean regardless (below-threshold seam / kind mismatch).
    flagged_names = {f.new for f in m.detect_collisions(new, base, ref, {}, threshold=3)}
    assert flagged_names == {"slugify2", "retryGateway"}, flagged_names
    # KEYSTONE regression: a SAME-NAME reinvention (new `slugify` in another file) whose only
    # occurrence of the id in the range is its OWN definition must FLAG — a same-id row's
    # self-mention is never a wire-through edge to the same-named seam (else the most blatant
    # duplicate passes clean).
    dup = m.detect_collisions(
        [{"id": "slugify", "kind": "function", "file": "src/dup.py"}],
        base, ref, {"slugify": {"src/dup.py"}}, threshold=3,
    )
    assert [f.new for f in dup] == ["slugify"], dup
    # control: a RENAMED symbol whose own file genuinely references the seam is a wire-through -> clean.
    wired = m.detect_collisions(
        [{"id": "slugify2", "kind": "function", "file": "src/new1.py"}],
        base, ref, {"slugify": {"src/new1.py"}}, threshold=3,
    )
    assert wired == [], wired
    # control: the SAME rename with an edge from an UNRELATED file (not new1.py) still FLAGS —
    # the wire-through is scoped to the new symbol's own file, not the whole range.
    masked = m.detect_collisions(
        [{"id": "slugify2", "kind": "function", "file": "src/new1.py"}],
        base, ref, {"slugify": {"src/z.py"}}, threshold=3,
    )
    assert [f.new for f in masked] == ["slugify2"], masked

    # --- backlog: seeded header, append, dedup by (new, resembles) --------------------------------
    text0, added0 = m.append_backlog("", flags)
    assert added0 and "| slugify2 | slugify |" in text0 and text0.startswith("# Reinvention backlog")
    assert m.backlog_keys(text0) == {("slugify2", "slugify")}
    text1, added1 = m.append_backlog(text0, flags)          # re-run same range -> nothing new
    assert added1 == [] and text1 == text0
    more = [m.CollisionFlag("slugify3", "slugify", "src/t3.py", 3, "function", "medium")]
    text2, added2 = m.append_backlog(text0, more)           # a different `new` -> a new row
    assert [a.new for a in added2] == ["slugify3"]
    assert m.backlog_keys(text2) == {("slugify2", "slugify"), ("slugify3", "slugify")}


def test_new_clones_reader(tmp: Path):
    """new_clones is the adopted clone-ratchet's count (int), null when no clone kit is wired, and
    folding a duplicate drops it — NEVER dead_exports/affordance_coverage_% (the demoted hints)."""
    import map_diff as md

    assert md._new_clones(tmp, {}) is None                                  # no CLONE_COUNT_FILE -> null
    conf = {"CLONE_COUNT_FILE": "clones.txt"}
    assert md._new_clones(tmp, conf) is None                                # configured but absent -> null
    (tmp / "clones.txt").write_text("7\n", encoding="utf-8")
    assert md._new_clones(tmp, conf) == 7
    (tmp / "clones.txt").write_text("4\n", encoding="utf-8")                # a fold drops the count
    assert md._new_clones(tmp, conf) == 4
    (tmp / "clones.txt").write_text("not-a-number\n", encoding="utf-8")     # garbage -> null, never a crash
    assert md._new_clones(tmp, conf) is None


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
        ("a field may hold a nested quote", ".py",
         "v = f\"{d['k'] if flag else other}\"\n", {"d", "k", "flag", "other"}, set()),
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
    try:
        listing = subprocess.run(
            ["git", "-C", str(root), "ls-files", "*.py"],
            capture_output=True, text=True, check=True,
        ).stdout.split("\n")
    except (OSError, subprocess.CalledProcessError):
        print("     SKIP corpus recall: not a git checkout, so there is no corpus to measure. NOT a pass.")
        return

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
        print(f"     SKIP corpus recall: only {truth_total} ground-truth identifiers found. NOT a pass.")
        return
    recall = hit / truth_total
    precision = hit / kept if kept else 0.0
    assert recall >= 0.99, f"corpus recall {recall:.3f} below the 0.99 floor"
    assert precision >= 0.95, f"corpus precision {precision:.3f} below the 0.95 floor"


def test_js_probe_against_the_lexicon():
    """CROSS-CHECK: over this repo's own `tools/**/*.js`, the map's definition set is a SUPERSET of
    the lexicon's independently-authored one.

    WHY THIS DIRECTION ONLY. If the lexicon learns a definition form the map has not, the map is
    UNDER-indexing and that is the defect — silently, since a recall index that misses a seam looks
    exactly like a corpus that has none. The other direction is not a defect: the map indexes
    `export const meta = {…}` and the lexicon does not, correctly, today.

    NOT A SECOND OPINION — DRIFT PROTECTION. The two probes were written independently for different
    questions, which is what makes the comparison worth anything; unifying them behind one pattern
    set would delete the signal along with the duplication.

    SKIPS LOUDLY when `tools/lexicon/` is absent. An adopter who took the map without the lexicon is
    TOLD the arm did not run, rather than shown a green it did not earn — a silent skip here would be
    this repo's own `fixture-passes-by-finding-nothing` class inside the kit that gates it.
    """
    kit = m.repo_root() / "tools" / "lexicon"
    if not (kit / "lexicon.py").is_file():
        print("     SKIP js-probe cross-check: tools/lexicon/ is not installed here, so the "
              "independent definition set this arm compares against does not exist. NOT a pass.")
        return
    sys.path.insert(0, str(kit))
    try:
        import lexicon as lx
        import lexicon_conf as lxc
    finally:
        sys.path.pop(0)
    # THE STOPWORD PARITY, and this file is the only legal home for it. `.lexicon.conf` forbids
    # `tools/lexicon/* -> tools/codebase-map/*`, so the lexicon may not import `map_lib` and must
    # restate the 21-word set inline. The ban is DIRECTIONAL and FILE-SCOPED: it says nothing about a
    # third file importing both, and this one already imports both. So the equality the lexicon's own
    # docstring can only assert is asserted HERE, where it can actually be read.
    # TOOL-dPromptedSeam-3, added by the closing review after the lexicon-side comment claimed no
    # such check could exist.
    # RAISES AssertionError, which is this module's ONLY failure idiom — `check()` at :52 catches
    # exactly that and nothing else. The first cut called `fail(...)`, which is not defined here: the
    # arm's only failure path raised NameError, `check()` did not catch it, and sixteen later arms
    # never ran. Worse, the commit adding it claimed the break had been "watched to red naming the
    # dropped word" — what was actually watched was a traceback whose text happened to contain the
    # word being grepped for. A gate whose failing case has never been seen is an assertion about
    # nothing, and this one was that in the commit that fixed an instance of it. Round-2 B2.
    if lx.DEAD_TOKENS != m._STOPWORDS:
        only_lex = sorted(lx.DEAD_TOKENS - m._STOPWORDS)
        only_map = sorted(m._STOPWORDS - lx.DEAD_TOKENS)
        raise AssertionError(
            "lexicon.DEAD_TOKENS has drifted from map_lib._STOPWORDS — the lexicon restates this set "
            "because the layer ban forbids importing it, so nothing but this arm can see them "
            f"disagree. only in lexicon: {only_lex or 'none'}; only in map_lib: {only_map or 'none'}")
    print(f"     ok stopword parity: lexicon.DEAD_TOKENS == map_lib._STOPWORDS "
          f"({len(m._STOPWORDS)} words)")

    root = m.repo_root()
    conf = lxc.load_conf(root / ".lexicon.conf")
    langs = {ext: (pset, mode) for ext, pset, mode in lxc.langs(conf) if mode != "dark"}
    if "js" not in langs:
        print("     SKIP js-probe cross-check: .lexicon.conf declares no live `js` language.")
        return
    pset, mode = langs["js"]
    theirs = set()
    for f in lx.tracked_files(root):
        if f.endswith(".js") and f.startswith("tools/"):
            fns, types, _imports = lx.extract(root / f, mode, pset)
            theirs |= {(f, name) for name, _line in list(fns) + list(types)}
    ours = {(r["file"], r["id"]) for r in m.scan_js_definitions(root / "tools", "kit-js")}
    missing = sorted(theirs - ours)
    assert not missing, (
        f"the map's JS definition probe misses {len(missing)} symbol(s) the lexicon's finds — the "
        f"map is under-indexing this layer: {missing[:8]}"
    )
    assert theirs, "the lexicon found NO js definitions under tools/, so this arm compared to empty"


def main() -> int:
    import tempfile

    failures = 0
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "root resolution: both install shapes + git boundary (S1/AC1)",
            lambda: test_install_prefix_resolution(Path(td)),
        )
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
    failures += check("js definition probe ⊇ the lexicon's own set (TOOL-dClosedLexicon-12)",
                      test_js_probe_against_the_lexicon)
    failures += check("coverage both directions + ratchet guards", test_coverage_directions)
    failures += check("dossier contract fails loud", test_parse_contract)
    failures += check("attribution: keyed > globs, posix, case-sensitive", test_attribution)
    failures += check("renders deterministic + keys-only + round-trip", test_renders_round_trip_and_determinism)
    failures += check("glob brackets fail loud; [[]-escape matches", test_glob_brackets_fail_loud_and_escape_works)
    failures += check(
        "symbols.json deterministic + fail-closed render", test_symbols_render_deterministic_and_fail_closed
    )
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
        failures += check(
            "reuse-lookup shared primitives (stems + fan-in + threshold)", lambda: test_reuse_shared_primitives(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check("reuse-lookup shortlist (AC3 fixture)", lambda: test_reuse_lookup(Path(td)))
    with tempfile.TemporaryDirectory() as td:
        failures += check(
            "closing loop: collisions + backlog dedup (S5 / AC4)", lambda: test_detect_collisions_and_backlog(Path(td))
        )
    with tempfile.TemporaryDirectory() as td:
        failures += check("new_clones reader (S5 / AC4)", lambda: test_new_clones_reader(Path(td)))
    failures += check("identifier tokens: one arm per over-strip class", test_identifier_tokens_per_language)
    failures += check("identifier tokens: corpus recall + precision floors", test_identifier_tokens_corpus_recall)
    print("PASS" if not failures else f"{failures} FAILURE(S)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
