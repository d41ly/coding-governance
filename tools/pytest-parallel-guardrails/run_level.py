#!/usr/bin/env python3
"""run_level.py — the pytest runner adapter: one product-test level, run with the crash probe armed.

    python <this kit>/run_level.py --detect     # each level a tracked pytest table declares as a marker
    python <this kit>/run_level.py <level>      # pytest -p crashprobe -m <level>, this kit importable

TOOL-dWitnessedBar-9 S3. This kit's descriptor declares the adapter as a `[[test_runner]]` row: its
`detect` argv, the `levels` it can run and the `argv` that runs one. The run-gates kit's leg factory
runs `detect` in a repository and renders one leg per level it names, as `tests.product` says.

`--detect` reads EVERY tracked `pyproject.toml` carrying `[tool.pytest.ini_options]`, the files this
kit's `[[hole]]` `pytest-ini-knobs` probe reads, and prints, one per line in the row's order, each
level of the `pytest` row whose name a `markers` entry declares (`unit: fast tests` declares `unit`).
EXIT 0 one level or more · 1 none: no tracked table, or no level among its markers · 2 refused: a
table that does not parse, no `pytest` row in this kit's descriptor, or git not answering.

`<level>` puts this kit's directory on PYTHONPATH and runs `python -m pytest -p crashprobe -m
<level>` in the current directory, so every adapter run carries the probe (the README's "Arm the
probe" step), and exits with pytest's own status. A level outside the row's `levels` is refused, 2.

WHAT IT DOES NOT CHECK. That a test marked with a level is of that level, or that the suite marks any
test at all: a declared marker no test carries runs nothing, and pytest exits 5 saying so.
"""
import os
import pathlib
import re
import subprocess
import sys
import tomllib

HERE = pathlib.Path(os.path.abspath(__file__)).parent
SAY = "run_level"
RUNNER = "pytest"
MARKER_RX = re.compile(r"\s*([A-Za-z_][A-Za-z0-9_]*)")


class Refusal(Exception):
    """Exit 2, nothing run."""


def read_runner_levels():
    """The `levels` of this kit's own `[[test_runner]]` row for pytest: the adapter's one statement of them."""
    try:
        desc = tomllib.loads((HERE / "kit.toml").read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as e:
        raise Refusal(f"this kit's kit.toml does not read: {e}") from None
    for row in desc.get("test_runner") or []:
        if isinstance(row, dict) and row.get("runner") == RUNNER:
            levels = row.get("levels")
            if isinstance(levels, list) and levels and all(isinstance(x, str) and x for x in levels):
                return levels
            raise Refusal(f"the {RUNNER} [[test_runner]] row's levels {levels!r} is no list of names")
    raise Refusal(f"this kit's kit.toml holds no [[test_runner]] row for {RUNNER}")


def read_declared_levels(root, levels):
    """Each of `levels` a tracked `pyproject.toml`'s `[tool.pytest.ini_options]` `markers` declares."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    r = subprocess.run(["git", "-c", "core.quotepath=off", "ls-files", "-z", "--", "*pyproject.toml"],
                       cwd=str(root), env=env, capture_output=True, encoding="utf-8", errors="replace",
                       stdin=subprocess.DEVNULL, timeout=120)
    if r.returncode != 0:
        raise Refusal(f"git ls-files did not list the tracked pyproject.toml files: {r.stderr.strip()}")
    declared = set()
    for rel in (p for p in r.stdout.split("\0") if p):
        try:
            data = tomllib.loads(pathlib.Path(root, rel).read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as e:
            raise Refusal(f"{rel} does not parse as TOML: {e}") from None
        ini = data.get("tool", {}).get("pytest", {}).get("ini_options")
        if not isinstance(ini, dict):
            continue
        markers = ini.get("markers") or []
        for m in markers.splitlines() if isinstance(markers, str) else markers:
            hit = MARKER_RX.match(m) if isinstance(m, str) else None
            if hit:
                declared.add(hit.group(1))
    return [lv for lv in levels if lv in declared]


def run_level_tests(level):
    """pytest at `level`, the crash probe armed from this kit's directory; pytest's exit status."""
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join([str(HERE)] + [p for p in [env.get("PYTHONPATH")] if p])
    return subprocess.run([sys.executable, "-m", "pytest", "-p", "crashprobe", "-m", level], env=env).returncode


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print("usage: run_level.py --detect | <level>", file=sys.stderr)
        return 2
    try:
        levels = read_runner_levels()
        if argv[0] == "--detect":
            found = read_declared_levels(pathlib.Path.cwd(), levels)
            for lv in found:
                print(lv)
            if not found:
                print(f"{SAY}: no tracked pyproject.toml declares a marker for any of {', '.join(levels)}",
                      file=sys.stderr)
            return 0 if found else 1
        if argv[0] not in levels:
            raise Refusal(f"{argv[0]!r} is no level of the {RUNNER} row: {', '.join(levels)}")
        return run_level_tests(argv[0])
    except Exception as e:  # noqa: BLE001 - any failure is a refusal, never the exit 1 that means "none"
        print(f"{SAY}: refused · {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
