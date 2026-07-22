"""Feature-level digest of a git range via the codebase map (codebase-map kit).

    python codebase-map/map_diff.py <base>..<head> [--verbose] [--drop-affordance-exempt]
    python codebase-map/map_diff.py <base>..<head> --converge
    python codebase-map/map_diff.py <base> <head>  [--verbose]

Attributes every changed file to its claiming feature(s) — keyed attributors first (from
map_extractors.KEYED_ATTRIBUTORS), then dossier path globs, then foundation globs — and rolls
up the rest as UNMAPPED (per-top-level-dir counts by default; full list behind --verbose).
The coverage line is the map's convergence-visibility metric.

--drop-affordance-exempt (S4a): after attribution, rewrite <MAP_ROOT>/affordance-exempt.toml,
dropping every feature the range TOUCHED (shrink-only). Touching a graced feature's files
mechanically removes its grace, so the next gate run demands its `## Reuse affordance` block —
no human remembering. Commit the rewritten file with the change.

--converge (S5): the closing loop. Reports the convergence signals over the range —
`collision_flags` (each NEW exported symbol that resembles an existing high-fan-in seam of the
same kind it did NOT wire through — shipped reinvention, over ALL new code) routed as a review
WARN to <MAP_ROOT>/reinvention-backlog.md (deduped), plus `new_clones` (the adopted
clone-ratchet's count, or null) — and the demoted hygiene hints affordance_coverage_% /
dead_exports (explicitly NOT the convergence signal). A REPORT + WARN, never a gate (F5): a
convergence metric that hard-fails false-fails on legitimate feature churn. Always exits 0.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:  # a non-UTF-8 stdout (stripped CI locale) must degrade a non-ASCII print, not crash it
    sys.stdout.reconfigure(errors="replace")
except (AttributeError, ValueError):
    pass

import map_lib as m  # noqa: E402

# map_extractors (the project layer) is imported LAZILY inside the attribution path only — the
# --converge mode needs no project extractors (it reads committed symbols.json + dossiers + conf),
# so the module stays importable in the kit repo, where selftest.py exercises it without a project
# map_extractors.py present.


def _changed_files(base: str, head: str) -> list[str]:
    """Changed files in base..head. Fails SOFT (a notice + []) when git cannot resolve the range —
    a first commit's parent, a typo'd ref, a shallow clone missing the base — so --converge and the
    digest degrade to 'nothing to diff' and honor their advisory intent, never a raw traceback."""
    out = subprocess.run(
        ["git", "-C", str(m.repo_root()), "diff", "--name-only", f"{base}..{head}"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if out.returncode != 0:
        print(f"# map-diff: cannot resolve range {base}..{head} (bad ref / shallow clone?) - nothing to diff")
        return []
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


# ======================================================================================
# --converge (S5): the closing loop over the range
# ======================================================================================


def _symbols_at_ref(root: Path, ref: str, rel: str) -> list[dict]:
    """symbols.json rows at a git ref (POSIX rel path), fail-open to [] — a range that predates
    the SYMBOL tier (or a fresh adoption) simply has no baseline, so nothing reads as reinvented
    (advisory, never a crash)."""
    out = subprocess.run(
        ["git", "-C", str(root), "show", f"{ref}:{rel}"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if out.returncode != 0 or not out.stdout.strip():
        return []
    try:
        data = json.loads(out.stdout)
    except json.JSONDecodeError:
        return []
    return data.get("symbols", []) if isinstance(data, dict) else []


def _read_symbols(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    return data.get("symbols", []) if isinstance(data, dict) else []


def _new_clones(root: Path, conf: dict[str, str]) -> int | None:
    """new_clones (§4): the adopted verbatim-clone-ratchet's count, read from the file named by
    CLONE_COUNT_FILE (relative to the repo root) — whatever clone kit is adopted writes its count
    there and this surfaces it. None when unset/unreadable: the clone signal is OPTIONAL (no clone
    kit adopted). Folding a duplicate drops the ratchet count -> the signal trends toward zero."""
    rel = conf.get("CLONE_COUNT_FILE", "").strip()
    if not rel:
        return None
    try:
        return int((root / rel).read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        return None


def _converge(base: str, head: str, files: list[str]) -> int:
    root = m.repo_root()
    conf = m.load_conf(root)
    map_dir = m.map_root(root)
    sym_rel = f"{conf['MAP_ROOT']}/generated/symbols.json"

    head_rows = _symbols_at_ref(root, head, sym_rel) or _read_symbols(map_dir / "generated" / "symbols.json")
    print(f"# map-diff --converge {base}..{head}")
    if not head_rows:
        print("no generated/symbols.json (SYMBOL recall tier not adopted) - nothing to converge.")
        return 0

    base_rows = _symbols_at_ref(root, base, sym_rel)
    base_key = {(r["id"], r["kind"], r["file"]) for r in base_rows}
    new_rows = [r for r in head_rows if (r["id"], r["kind"], r["file"]) not in base_key]

    symbol_files = sorted({r["file"] for r in head_rows})
    sym_exts = frozenset(Path(r["file"]).suffix for r in head_rows if Path(r["file"]).suffix)
    ref_index = m.build_reference_index(symbol_files, root=root) if symbol_files else {}
    range_index = m.reference_index_for(files, root=root, extensions=sym_exts or None)

    texts = m.load_dossier_texts(map_dir)
    affordance_seams = frozenset(
        seam for t in texts.values() for seam in m.parse_affordance(t).seams
    )
    flags = m.detect_collisions(
        new_rows, base_rows, ref_index, range_index,
        threshold=m.seam_fanin_threshold(root), affordance_seams=affordance_seams,
    )

    # F7: route each flag to the durable, deduped reinvention backlog.
    backlog_path = map_dir / "reinvention-backlog.md"
    added: list[m.CollisionFlag] = []
    if flags:
        current = backlog_path.read_text(encoding="utf-8") if backlog_path.is_file() else ""
        new_text, added = m.append_backlog(current, flags)
        if added:
            backlog_path.write_text(new_text, encoding="utf-8", newline="\n")

    print("# convergence signals (trend to zero = the repo converges); a WARN, never a gate.")
    print(f"\ncollision_flags: {len(flags)}")
    for f in flags:
        print(
            f"- WARN {f.new} [{f.kind}, {f.file}] resembles seam {f.resembles} (fan-in {f.fanin}) "
            f"- built new instead of wiring through it; confidence {f.confidence}"
        )
    if flags:
        rel = backlog_path.relative_to(root).as_posix() if backlog_path.is_relative_to(root) else backlog_path.name
        dup = len(flags) - len(added)
        skip = f" ({dup} already recorded, skipped)" if dup else ""
        print(
            f"  -> {len(added)} row(s) appended to {rel}{skip}; fold each into its seam "
            "(or delete the row if genuinely distinct)."
        )

    clones = _new_clones(root, conf)
    if clones is None:
        print("\nnew_clones: null (clone-ratchet kit not adopted; set CLONE_COUNT_FILE to surface it)")
    else:
        print(f"\nnew_clones: {clones} (verbatim-clone-ratchet count; fold duplicates to trend it down)")

    features = [k for k in texts if k != "foundation"]
    with_block = sum(1 for k in features if m.parse_affordance(texts[k]).has_block)
    cov = f"{100 * with_block // len(features)}% ({with_block}/{len(features)})" if features else "n/a"
    dead = sum(1 for r in head_rows if m.fan_in(ref_index, r["id"], r["file"]) == 0)
    print("\n# hygiene hints (NOT the convergence signal - see spec S5):")
    print(f"affordance_coverage: {cov} of feature dossiers carry a ## Reuse affordance block")
    print(f"dead_exports: {dead} symbol(s) with fan-in 0 (a hint - a used dup is not dead)")
    return 0  # report + WARN, never a gate (F5)


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
    parser.add_argument(
        "--converge",
        action="store_true",
        help="S5: report the closing-loop convergence signals over the range (collision_flags "
        "routed to the reinvention backlog + new_clones + demoted hygiene hints). Report + WARN, "
        "never a gate.",
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

    if args.converge:
        return _converge(base, head, files)

    if not files:
        print(f"map-diff {base}..{head}: no changes")
        return 0

    import map_extractors as ext  # project layer — only the attribution digest needs it

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
