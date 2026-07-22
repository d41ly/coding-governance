"""Feature-level digest of a git range via the codebase map (codebase-map kit).

    python codebase-map/map_diff.py <base>..<head> [--verbose] [--drop-affordance-exempt]
    python codebase-map/map_diff.py <base> <head>  [--verbose]

Attributes every changed file to its claiming feature(s) — keyed attributors first (from
map_extractors.KEYED_ATTRIBUTORS), then dossier path globs, then foundation globs — and rolls
up the rest as UNMAPPED (per-top-level-dir counts by default; full list behind --verbose).
The coverage line is the map's convergence-visibility metric.

--drop-affordance-exempt (S4a): after attribution, rewrite <MAP_ROOT>/affordance-exempt.toml,
dropping every feature the range TOUCHED (shrink-only). Touching a graced feature's files
mechanically removes its grace, so the next gate run demands its `## Reuse affordance` block —
no human remembering. Commit the rewritten file with the change.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import map_extractors as ext  # noqa: E402
import map_lib as m  # noqa: E402


def _changed_files(base: str, head: str) -> list[str]:
    out = subprocess.run(
        ["git", "-C", str(m.repo_root()), "diff", "--name-only", f"{base}..{head}"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    return [line.strip() for line in out.stdout.splitlines() if line.strip()]


def _drop_affordance_exempt(touched: dict[str, list[str]]) -> None:
    """S4a: rewrite affordance-exempt.toml, dropping every feature the range touched (shrink-only).
    Writes only when the set actually shrinks; the dropped dossiers must carry a `## Reuse
    affordance` block on the next gate run. LF write, matching gen_map's artifact writer."""
    exempt = m.load_affordance_exempt()
    kept = m.drop_touched_exemptions(exempt, touched)
    dropped = sorted(exempt - kept)
    if not dropped:
        print("\n# affordance-exempt: no touched feature was graced - unchanged")
        return
    path = m.map_root() / "affordance-exempt.toml"
    path.write_text(m.render_affordance_exempt(kept), encoding="utf-8", newline="\n")
    print(
        f"\n# affordance-exempt: dropped {dropped} (touched) - {len(kept)} still graced. "
        "They must now carry a '## Reuse affordance' block (commit the rewritten file)."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("range", nargs="+", help="<base>..<head> or <base> <head>")
    parser.add_argument("--verbose", action="store_true", help="full unmapped file list")
    parser.add_argument(
        "--drop-affordance-exempt",
        action="store_true",
        help="S4a: after attribution, drop every touched feature from the affordance-exempt list "
        "(shrink-only) so the next gate run demands its '## Reuse affordance' block",
    )
    args = parser.parse_args()

    if len(args.range) == 1 and ".." in args.range[0]:
        base, head = args.range[0].split("..", 1)
    elif len(args.range) == 2:
        base, head = args.range
    else:
        parser.error("pass <base>..<head> or two refs")
        return 2

    files = _changed_files(base, head)
    if not files:
        print(f"map-diff {base}..{head}: no changes")
        return 0

    ids = ext.inventory_ids()
    tree = m.load_map_tree(ids, decision_id_re=getattr(ext, "DECISION_ID_RE", m.DEFAULT_DECISION_ID_RE))
    attributed = m.attribute_paths(
        files, tree, keyed_attributors=getattr(ext, "KEYED_ATTRIBUTORS", ())
    )
    unmapped = attributed.pop("UNMAPPED", [])
    by_feature = {d.feature: d for d in tree.dossiers}

    mapped_count = len(files) - len(unmapped)
    print(
        f"# map-diff {base}..{head} — {len(files)} files, mapped {mapped_count}/{len(files)} "
        f"({100 * mapped_count // len(files)}%)"
    )
    for owner in sorted(attributed):
        paths = attributed[owner]
        d = by_feature.get(owner)
        meta = f" · {d.status} · {', '.join(d.decisions[:3])}" if d else ""
        print(f"\n## {owner} — {len(paths)} file(s){meta}")
        for p in sorted(paths):
            print(f"- {p}")
    if unmapped:
        print(f"\n## UNMAPPED — {len(unmapped)} file(s)")
        if args.verbose:
            for p in sorted(unmapped):
                print(f"- {p}")
        else:
            tops = Counter(p.split("/", 1)[0] if "/" in p else "(root)" for p in unmapped)
            for top, n in sorted(tops.items()):
                print(f"- {top}: {n} file(s)")
            print("(full list: --verbose)")
    if args.drop_affordance_exempt:
        _drop_affordance_exempt(attributed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
