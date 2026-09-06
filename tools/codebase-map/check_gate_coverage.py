#!/usr/bin/env python3
"""check_gate_coverage.py — does the INSTALLED gate compare every artifact the engine writes?

    python <kit>/check_gate_coverage.py            # assert; exit 1 on an uncompared artifact
    python <kit>/check_gate_coverage.py --list     # print both sets and exit 0 (authoring aid)

THE HOLE THIS COVERS. `adopt-codebase-map.sh` copies the gate template into an adopting repo only
when it is ABSENT, and leaves it alone forever after — correctly, because the project owns that
file and may customise it. `gen_map.py` is engine and DOES update on every kit upgrade. So a kit
that starts writing a new generated artifact starts writing it into upgraded adopters whose frozen
gate has no idea it exists, and nothing detects the divergence: the artifact is generated, committed
and never compared, which is a freshness gate that passes over a file it does not know about.

WHAT IT COMPARES, and it is deliberately NOT a byte diff. A project is entitled to edit its gate, so
a diff between two files reports customisation as though it were staleness. What this reports is the
ADOPTER-VISIBLE CONSEQUENCE: the set of generated artifacts the engine writes, minus the set the
installed gate names. One predicate, two inputs — the same regex reads both sides, so the two sets
cannot be derived by two rules that disagree.

**WHAT IT CANNOT DECIDE, stated because a check's silence reads as coverage.** It cannot tell a
DELIBERATE omission from a STALE one. A project that removed the symbol tier on purpose and a
project whose gate predates it look identical from here, and no amount of reading the file
separates them — the difference is in an intent nothing records. It reports the omission and names
it as undecidable rather than guessing, which is why it is a REPORT with an exit code and not a
judgement about the adopter's choices.

It also does not check that a named artifact is compared CORRECTLY. It reads which artifacts each
side NAMES; a gate that names `symbols.json` and compares it against the wrong renderer passes here.
That is a structural check reported as one.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent))

import map_lib as m  # noqa: E402

#: The one predicate, applied to both sides. It matches the way BOTH the engine and the gate spell a
#: generated artifact: a `gen_dir`-rooted path with a literal filename. Anything either side reaches
#: by a computed name is invisible to it, which is a real limit and is why `--list` exists.
ARTIFACT_RE = re.compile(r'gen_dir\s*/\s*"([^"]+)"')
#: Unit 2 made the gate's conditional tiers an explicit table; its rows name the artifact too.
TIER_RE = re.compile(r'^\s*\(\s*"[^"]*"\s*,\s*"[^"]*"\s*,\s*"([^"]+)"\s*,', re.M)


def scan_artifacts(text: str) -> set[str]:
    """Every generated artifact filename a source file NAMES."""
    return set(ARTIFACT_RE.findall(text)) | set(TIER_RE.findall(text))


def resolve_gate_path(root: Path) -> Path | None:
    """The installed gate, from `.codebase-map.conf` GATE_FILE. `None` when it is unset or absent."""
    value = (m.load_conf(root) or {}).get("GATE_FILE", "").strip()
    if not value:
        return None
    path = Path(value)
    path = path if path.is_absolute() else (root / value)
    return path if path.is_file() else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.replace("<kit>", m.kit_rel()))
    parser.add_argument("--list", action="store_true", help="print both sets and exit 0")
    args = parser.parse_args(argv)

    root = m.repo_root()
    kit = Path(os.path.abspath(__file__)).parent
    engine = scan_artifacts((kit / "gen_map.py").read_text(encoding="utf-8"))

    # LIVENESS. A predicate that matches nothing on the engine side reports every gate as complete,
    # which is the vacuous-selector shape this kit's own docstrings name as its dominant failure.
    if not engine:
        print("gate-coverage REFUSED — the artifact predicate matched nothing in the engine, so it "
              "would report every installed gate as complete. The predicate is stale, not the gate.",
              file=sys.stderr)
        return 2

    gate_path = resolve_gate_path(root)
    if gate_path is None:
        print(f"gate-coverage: skipped — GATE_FILE is unset in .codebase-map.conf or names no "
              f"existing file, so there is no installed gate to compare. The engine writes "
              f"{len(engine)} artifact(s): {', '.join(sorted(engine))}")
        return 0

    installed = scan_artifacts(gate_path.read_text(encoding="utf-8"))
    rel = gate_path.relative_to(root).as_posix() if gate_path.is_relative_to(root) else gate_path.as_posix()
    uncompared = sorted(engine - installed)

    if args.list:
        print(f"engine writes : {', '.join(sorted(engine))}")
        print(f"{rel} names : {', '.join(sorted(installed)) or '(none)'}")
        print(f"uncompared    : {', '.join(uncompared) or '(none)'}")
        return 0

    if not uncompared:
        print(f"gate-coverage: ok — {rel} names every one of the {len(engine)} artifact(s) the "
              f"engine writes. Byte differences from the template are NOT reported: a project is "
              f"entitled to customise its gate.")
        return 0

    print(f"gate-coverage: {rel} does not compare {len(uncompared)} artifact(s) the engine writes: "
          f"{', '.join(uncompared)}.", file=sys.stderr)
    print("Each is generated, committed, and graded by nothing — a freshness gate passing over a "
          "file it does not know about. Copy the missing tier from the kit's "
          "`test_codebase_map.template.py`, or delete the artifact if you do not want it.",
          file=sys.stderr)
    print("THIS CHECK CANNOT TELL A DELIBERATE OMISSION FROM A STALE ONE. If you removed the tier "
          "on purpose, that intent is recorded nowhere this can read.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
