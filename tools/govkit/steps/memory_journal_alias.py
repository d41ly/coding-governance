#!/usr/bin/env python3
"""memory_journal_alias.py — the upgrade step `memory-tree/serves-journal-read-as-log` (TOOL-dTotalRecall-20 S1).

    python <prefix>/govkit/steps/memory_journal_alias.py up|down|witness <target>

Its row is the memory-tree descriptor's `[[upgrade]]`. The Serves kind `journal` became `log`, and a
`journal` record is read through the alias `tree_lib.KIND_ALIASES` declares: no record is rewritten.
The step declares that renamed surface and grades the target against it. The UP runs gov's
memory-tree `gen_build_index.py --print-bindings` with the target as its working directory, so gov's
`read_bindings` reads the target's records, and counts each `S` row whose kind is `journal`, a
record bound through the alias. An `A` row whose reason opens `first token journal` is one a reader
without the alias refuses: the up names each and exits 1. It exits 1 too where the run exits other
than 0, or naming the memory-tree kit where it does not resolve. It writes no file, so its DOWN is a
no-op that exits 0, and its WITNESS is the same read as its up.

`run_index_mode` is the one way the three memory-tree steps beside this file reach gov's index
generator: by subprocess, found through `govkit.resolve_kit_dir`, never by import (TOOL-dTotalRecall-20 §2).

Exit 0 done, 1 a refused record or no grade (nothing written), 2 a usage error.
"""

import os
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import govkit  # noqa: E402  the deployer beside this directory: the kit resolver, as shims.py imports it

STEP_ID = "memory-tree/serves-journal-read-as-log"
VERBS = ("up", "down", "witness")


def run_index_mode(target, *args: str) -> subprocess.CompletedProcess:
    """gov's memory-tree `gen_build_index.py <args>`, run to completion with `target` as its working
    directory and no inherited `GIT_*` variable, so it reads the target's tree. LookupError where the
    memory-tree kit does not resolve from govkit's own directory."""
    kit = govkit.resolve_kit_dir("memory-tree", "gen_build_index.py", govkit.GOVKIT_DIR)
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    return subprocess.run([sys.executable, str(kit / "gen_build_index.py"), *args], cwd=str(target),
                          capture_output=True, text=True, encoding="utf-8", errors="replace",
                          stdin=subprocess.DEVNULL, env=env)


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] not in VERBS:
        print(f"usage: memory_journal_alias.py {'|'.join(VERBS)} <target>", file=sys.stderr)
        return 2
    verb, target = argv
    if verb == "down":
        print(f"{STEP_ID}: down · the up writes nothing, so nothing is restored")
        return 0
    try:
        p = run_index_mode(target, "--print-bindings")
    except LookupError as exc:
        print(f"{STEP_ID}: the memory-tree kit does not resolve, so no record is graded: {exc}", file=sys.stderr)
        return 1
    if p.returncode != 0:
        said = (p.stdout + p.stderr).strip().splitlines()
        print(f"{STEP_ID}: gen_build_index.py --print-bindings exited {p.returncode}: {said[-1] if said else 'no output'}",
              file=sys.stderr)
        return 1
    rows = [ln.split("\t") for ln in p.stdout.splitlines()]
    read = sum(1 for r in rows if r[0] == "S" and len(r) > 2 and r[2] == "journal")
    refused = [r for r in rows if r[0] == "A" and len(r) > 2 and r[2].startswith("first token journal")]
    for r in refused:
        print(f"{STEP_ID}: {r[1]} · {r[2]}")
    print(f"{STEP_ID}: {verb} · journal {read} record(s) read as log through the alias · {len(refused)} refused")
    return 1 if refused else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    raise SystemExit(main(sys.argv[1:]))
