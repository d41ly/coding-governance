#!/usr/bin/env python3
"""python_floor.py — the upgrade step `lib/python-floor-<X.Y>`'s program (TOOL-dSafePassage-82 S3).

    python <prefix>/govkit/steps/python_floor.py preflight | down <prior> <target> [<to>] | floor

Its row is the floor row of `steps.toml`. It finds gov's `<prefix>/lib/python-floor.sh` through the
step module's `resolve_kit_dir`, runs it under the bash that module's `resolve_shell_argv` resolves,
`GOV_BASH` first, with this program's own arguments, and exits as it exits: the script owns every
verb, every line it prints and every refusal. Where no bash resolves, that module's Refusal is
written as one `python_floor.py:` line and the exit is 2, never the bare name `bash`, which the
Windows loader answers with WSL's launcher (TOOL-dWitnessedBar-26 S7).
The step module is loaded by its path, because the runner's `-I` drops this file's own directory from
`sys.path`; nothing is imported from govkit, so a step running isolated runs this.

Exit: the script's own, or 2 when no floor script or no bash resolves.
"""

import importlib.util
import pathlib
import subprocess
import sys

GOV = pathlib.Path(__file__).resolve().parents[2]  # `{gov}`: the tool root this step ships in
FLOOR_HOME, FLOOR_SCRIPT = "lib", "python-floor.sh"


def main(argv: list[str]) -> int:
    path = pathlib.Path(__file__).resolve().parents[1] / "upgrade_steps.py"
    spec = importlib.util.spec_from_file_location("upgrade_steps", path)
    steps = importlib.util.module_from_spec(spec)
    sys.modules["upgrade_steps"] = steps
    spec.loader.exec_module(steps)
    try:
        kit = steps.resolve_kit_dir(FLOOR_HOME, FLOOR_SCRIPT, GOV)
    except LookupError as e:
        sys.stderr.write(f"python_floor.py: {e}\n")
        return 2
    try:
        run = steps.resolve_shell_argv(["bash", (kit / FLOOR_SCRIPT).as_posix(), *argv])
    except steps.Refusal as e:
        sys.stderr.write(f"python_floor.py: {e}\n")
        return 2
    return subprocess.run(run).returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
