# **Serves:** journal TOOL-aMendedFleet-73
#
# The HIDDEN suite of the vague-brief arm. Written from the FULL brief (the journal beside this file)
# before any implementation existed, and never shown to a builder. It reaches a tool only through
# what the VAGUE brief pins: the file name `declared.py`, `kits.toml` with `[[kit]]` rows carrying
# `name` and `path`, and the `tools/` directory. Each test is copied into a fresh tree whose root also
# holds the tool, and runs `python declared.py` with that root as the working directory, so a tool
# that defaults to its own directory and one that defaults to the cwd are graded alike.
#
# TAGS ARE THE NAME. `test_intent_*` is a behaviour the vague brief's stated purpose implies, and is
# the hidden MEASURE. `test_contract_*` is a spelling only the full brief pins, reported beside it.
# The harness reads the tag off the name; a test named neither way is refused by the harness.
#
# LIVENESS: every test asserts something an exit-0 stub cannot do. A clean-tree test is PAIRED with a
# drifted twin that must exit non-zero, so a tool that never fails cannot pass one. The harness's
# `stub` verb runs this file against such a stub and reds if any test passes it.
#
# WHAT THIS DOES NOT CHECK: anything the vague brief leaves to the builder's judgement beyond what
# the purpose implies. That is the decision probes' job, not this suite's.
#
#     TRIAL_TOOL=<abs path to declared.py> python -m pytest -q <this file>
import os
import pathlib
import shutil
import subprocess
import sys

import pytest

TOOL = os.environ.get("TRIAL_TOOL", "")


@pytest.fixture(name="tree")
def build_tree(tmp_path):
    if not TOOL or not os.path.isfile(TOOL):
        pytest.fail(f"TRIAL_TOOL names no file: {TOOL!r}")
    root = tmp_path / "repo"
    (root / "tools").mkdir(parents=True)
    shutil.copyfile(TOOL, root / "declared.py")
    return root


def build_kits(root, rows, extra=""):
    body = "".join(f'[[kit]]\nname = "{n}"\npath = "{p}"\n\n' for n, p in rows) + extra
    (root / "kits.toml").write_text(body, encoding="utf-8")


def build_dirs(root, *names):
    for n in names:
        (root / "tools" / n).mkdir(parents=True, exist_ok=True)


def run_tool(root, *args, cwd=None, tool=None):
    tool = tool or str(root / "declared.py")
    p = subprocess.run([sys.executable, tool, *args], cwd=str(cwd or root), capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=60)
    return p.returncode, p.stdout, p.stderr


def build_clean(root):
    build_dirs(root, "alpha", "beta")
    build_kits(root, [("alpha", "tools/alpha"), ("beta", "tools/beta")])


# ---------------------------------------------------------------------------------- intent

def test_intent_clean_tree_passes_and_drift_fails(tree):
    build_clean(tree)
    assert run_tool(tree)[0] == 0
    build_dirs(tree, "gamma")
    assert run_tool(tree)[0] != 0


def test_intent_undeclared_directory_fails_naming_it(tree):
    build_clean(tree)
    build_dirs(tree, "zeta")
    rc, out, err = run_tool(tree)
    assert rc != 0
    assert "zeta" in out + err


def test_intent_declared_but_absent_fails_naming_it(tree):
    build_dirs(tree, "alpha")
    build_kits(tree, [("alpha", "tools/alpha"), ("omega", "tools/omega")])
    rc, out, err = run_tool(tree)
    assert rc != 0
    assert "omega" in out + err


def test_intent_both_directions_reported_together(tree):
    build_dirs(tree, "alpha", "zeta")
    build_kits(tree, [("alpha", "tools/alpha"), ("omega", "tools/omega")])
    rc, out, err = run_tool(tree)
    assert rc != 0
    assert "zeta" in out + err and "omega" in out + err


def test_intent_plain_file_under_tools_is_not_a_kit(tree):
    build_clean(tree)
    (tree / "tools" / "readme.txt").write_text("not a kit\n", encoding="utf-8")
    assert run_tool(tree)[0] == 0
    build_dirs(tree, "gamma")
    assert run_tool(tree)[0] != 0


def test_intent_nested_directory_is_not_a_kit(tree):
    build_clean(tree)
    (tree / "tools" / "alpha" / "inner").mkdir()
    assert run_tool(tree)[0] == 0
    build_dirs(tree, "gamma")
    assert run_tool(tree)[0] != 0


def test_intent_row_matched_by_path_not_name(tree):
    build_dirs(tree, "a")
    build_kits(tree, [("alpha", "tools/a")])
    assert run_tool(tree)[0] == 0
    build_dirs(tree, "b")
    assert run_tool(tree)[0] != 0


def test_intent_unparseable_registry_does_not_pass(tree):
    build_dirs(tree, "alpha")
    (tree / "kits.toml").write_text("[[kit]\nname = alpha\n", encoding="utf-8")
    rc, out, err = run_tool(tree)
    assert rc != 0
    assert (out + err).strip()


def test_intent_missing_registry_does_not_pass(tree):
    build_dirs(tree, "alpha")
    rc, out, err = run_tool(tree)
    assert rc != 0
    assert (out + err).strip()


def test_intent_row_missing_path_does_not_pass(tree):
    build_dirs(tree, "alpha")
    (tree / "kits.toml").write_text('[[kit]]\nname = "alpha"\n', encoding="utf-8")
    rc, out, err = run_tool(tree)
    assert rc != 0
    assert (out + err).strip()


# ---------------------------------------------------------------------------------- contract

def test_contract_finding_exit_is_one(tree):
    build_clean(tree)
    build_dirs(tree, "zeta")
    assert run_tool(tree)[0] == 1


def test_contract_undeclared_line(tree):
    build_clean(tree)
    build_dirs(tree, "zeta")
    rc, out, _ = run_tool(tree)
    assert "UNDECLARED tools/zeta" in out.splitlines()


def test_contract_missing_line(tree):
    build_dirs(tree, "alpha")
    build_kits(tree, [("alpha", "tools/alpha"), ("omega", "tools/omega")])
    rc, out, _ = run_tool(tree)
    assert rc == 1
    assert "MISSING omega tools/omega" in out.splitlines()


def test_contract_waiver_file_exempts(tree):
    build_clean(tree)
    build_dirs(tree, "zeta")
    assert run_tool(tree)[0] == 1
    (tree / "waivers.txt").write_text("tools/zeta\n", encoding="utf-8")
    assert run_tool(tree)[0] == 0


def test_contract_waiver_blank_and_comment_lines_ignored(tree):
    build_clean(tree)
    build_dirs(tree, "zeta")
    assert run_tool(tree)[0] == 1
    (tree / "waivers.txt").write_text("# kept out on purpose\n\ntools/zeta\n\n", encoding="utf-8")
    rc, out, _ = run_tool(tree)
    assert rc == 0
    assert "STALE-WAIVER" not in out


def test_contract_stale_waiver_nonexistent(tree):
    build_clean(tree)
    (tree / "waivers.txt").write_text("tools/ghost\n", encoding="utf-8")
    rc, out, _ = run_tool(tree)
    assert rc == 1
    assert "STALE-WAIVER tools/ghost" in out.splitlines()


def test_contract_stale_waiver_declared(tree):
    build_clean(tree)
    (tree / "waivers.txt").write_text("tools/alpha\n", encoding="utf-8")
    rc, out, _ = run_tool(tree)
    assert rc == 1
    assert "STALE-WAIVER tools/alpha" in out.splitlines()


def test_contract_misconfiguration_exit_is_two(tree):
    build_dirs(tree, "alpha")
    (tree / "kits.toml").write_text("[[kit]\n", encoding="utf-8")
    rc, _, err = run_tool(tree)
    assert rc == 2
    assert err.strip()


def test_contract_missing_registry_exit_is_two(tree):
    build_dirs(tree, "alpha")
    assert run_tool(tree)[0] == 2


def test_contract_row_missing_field_exit_is_two(tree):
    build_dirs(tree, "alpha")
    (tree / "kits.toml").write_text('[[kit]]\npath = "tools/alpha"\n', encoding="utf-8")
    rc, _, err = run_tool(tree)
    assert rc == 2
    assert err.strip()


def test_contract_preview_exits_zero_with_findings(tree):
    build_clean(tree)
    build_dirs(tree, "zeta")
    rc, out, _ = run_tool(tree, "--preview")
    assert rc == 0
    assert "UNDECLARED tools/zeta" in out.splitlines()


def test_contract_root_option(tree, tmp_path):
    build_clean(tree)
    build_dirs(tree, "zeta")
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    tool = elsewhere / "declared.py"
    shutil.copyfile(TOOL, tool)
    rc, out, _ = run_tool(tree, "--root", str(tree), cwd=elsewhere, tool=str(tool))
    assert rc == 1
    assert "UNDECLARED tools/zeta" in out.splitlines()


def test_contract_root_not_a_directory_exit_is_two(tree, tmp_path):
    build_clean(tree)
    assert run_tool(tree, "--root", str(tmp_path / "nowhere"))[0] == 2


def test_contract_deterministic_bytes(tree):
    build_dirs(tree, "alpha", "zeta", "eta", "theta")
    build_kits(tree, [("alpha", "tools/alpha"), ("omega", "tools/omega")])
    first = run_tool(tree)
    second = run_tool(tree)
    assert first[0] == 1
    assert first[1] == second[1]
    lines = [ln for ln in first[1].splitlines() if ln.startswith("UNDECLARED ")]
    assert len(lines) == 3


def test_contract_clean_prints_at_most_one_line(tree):
    build_clean(tree)
    rc, out, _ = run_tool(tree)
    assert rc == 0
    assert len(out.splitlines()) <= 1
    build_dirs(tree, "gamma")
    assert run_tool(tree)[0] == 1
