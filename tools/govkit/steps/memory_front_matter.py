#!/usr/bin/env python3
"""memory_front_matter.py — the upgrade step `memory-tree/readme-front-matter-graded` (TOOL-dTotalRecall-20 S4).

    python <prefix>/govkit/steps/memory_front_matter.py up|down|witness <target>

Its row is the memory-tree descriptor's `[[upgrade]]`. A build README's front matter is declared
(TOOL-dTotalRecall-4), and a key outside the declaration is refused. The UP grades the target's READMEs
before that refusal meets them: it runs gov's memory-tree `gen_build_index.py
--print-front-matter-findings` with the target as its working directory, never an import of
memory-tree, passes the mode's stderr through (its `front-matter: legacy population unarmed` line
among it), prints each `<path>: <key> unknown|derived` finding, and exits 1 on any, so the walk stops
before the adopter's next hygiene run refuses the key. It exits 1 on the mode's exit 2, or naming the
memory-tree kit where it does not resolve. It never rewrites a README, so its DOWN is a no-op that
exits 0, and its WITNESS is the same grade as its up.

Exit 0 no finding, 1 a finding or no grade (nothing written), 2 a usage error.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from memory_journal_alias import run_index_mode  # noqa: E402  the steps' one reach of the index generator

STEP_ID = "memory-tree/readme-front-matter-graded"
VERBS = ("up", "down", "witness")


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] not in VERBS:
        print(f"usage: memory_front_matter.py {'|'.join(VERBS)} <target>", file=sys.stderr)
        return 2
    verb, target = argv
    if verb == "down":
        print(f"{STEP_ID}: down · the up writes nothing, so nothing is restored")
        return 0
    try:
        p = run_index_mode(target, "--print-front-matter-findings")
    except LookupError as exc:
        print(f"{STEP_ID}: the memory-tree kit does not resolve, so no README is graded: {exc}", file=sys.stderr)
        return 1
    sys.stderr.write(p.stderr)
    if p.returncode != 0:
        print(f"{STEP_ID}: gen_build_index.py --print-front-matter-findings exited {p.returncode}", file=sys.stderr)
        return 1
    findings = [ln for ln in p.stdout.splitlines() if ln.strip()]
    for ln in findings:
        print(ln)
    print(f"{STEP_ID}: {verb} · {len(findings)} front-matter finding(s)"
          + (" · edit each key before `update` goes on" if findings else ""))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    raise SystemExit(main(sys.argv[1:]))
