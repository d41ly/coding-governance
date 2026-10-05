"""Feature-level digest of a git range via the codebase map (codebase-map kit).

    python <kit>/map_diff.py <base>..<head> [--verbose] [--drop-affordance-exempt]
    python <kit>/map_diff.py <base> <head>  [--verbose]
    python <kit>/map_diff.py [<base>..<head>] --stale-dossiers [--json]

Attributes every changed file to its claiming feature(s) — keyed attributors first (from
map_extractors.KEYED_ATTRIBUTORS), then dossier path globs, then foundation globs — and rolls
up the rest as UNMAPPED (per-top-level-dir counts by default; full list behind --verbose).
The coverage line is the map's convergence-visibility metric.

--drop-affordance-exempt (S4a): after attribution, rewrite <MAP_ROOT>/affordance-exempt.toml,
dropping every feature the range TOUCHED (shrink-only). Touching a graced feature's files
mechanically removes its grace, so the next gate run demands its `## Reuse affordance` block —
no human remembering. Commit the rewritten file with the change.

--stale-dossiers: the feature dossiers OLDER THAN THEIR PATHS — a commit touching a path a dossier
claims is not an ancestor of the dossier's own last commit. Derived from git, no stamp: one
`git log` over the history reachable from HEAD, or with `<base>..<head>` the commits in that range,
which lists the dossiers a range touched and did not refresh. Paths under the map root are never a
claim, and a merge commit carries no paths (a conflict-resolution-only change is not seen). A
shallow clone prints `live` false instead of a count over an amputated history. `--json` prints
one object: scope, of, stale, live, note, dossiers. Exit 1 when git cannot read the range.

Exit 2 is the one exception, and it is a REFUSAL rather than a result: the resolved repo root
carries no .codebase-map.conf. At a root that was never adopted the digest would report every
file UNMAPPED and --stale-dossiers every dossier fresh, both at exit 0.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

# `abspath`, NOT `resolve()`: this insert decides which path string `map_lib.__file__` carries,
# and map_lib.kit_dir()/the gate template both use abspath. Under a junctioned kit dir resolve()
# yields the LINK TARGET, so this entrypoint would stamp one prefix into the byte-compared
# artifacts while the gate re-renders another — a permanently STALE gate whose own printed
# remedy re-writes the wrong spelling and never converges (measured).
sys.path.insert(0, str(Path(os.path.abspath(__file__)).parent))

try:  # a non-UTF-8 stdout (stripped CI locale) must degrade a non-ASCII print, not crash it
    sys.stdout.reconfigure(errors="replace")
except (AttributeError, ValueError):
    pass

import map_lib as m  # noqa: E402

# map_extractors (the project layer) is imported LAZILY inside the paths that need it, so the
# module stays importable in the kit repo, where selftest.py exercises it without a project
# map_extractors.py present.


def _changed_files(base: str, head: str) -> list[str]:
    """Changed files in base..head. Fails SOFT (a notice + []) when git cannot resolve the range —
    a first commit's parent, a typo'd ref, a shallow clone missing the base — so the digest degrades
    to 'nothing to diff' and honors its advisory intent, never a raw traceback."""
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
# --stale-dossiers: dossier freshness, derived from git
# ======================================================================================


def read_commit_paths(root: Path, base: str | None, head: str = "HEAD"):
    """``(commits, scope)`` for ``measure_dossier_staleness``, or ``None`` on a SHALLOW clone.

    ONE ``git log --topo-order`` over the history reachable from the tips — ``head``, plus ``base``
    in range scope — printing each commit's sha, parents and touched paths. ``scope`` is ``None``
    for the whole history, else the commits reachable from head and not from base, which is
    git's own ``base..head``, derived in process from the printed parents so a dossier committed
    before the range still names its true last commit. ``--no-renames`` so a rename shows both
    the path it left and the path it took; a dossier claiming either was moved by it.

    The shallow probe resolves the tips in the same call. A shallow history is unmeasurable, not
    clean: its first commit has parents the clone never fetched, so every ancestry answer is cut.
    Raises ``MapError`` when git cannot resolve a tip or print the log."""
    tips = [head] + ([base] if base is not None else [])
    probe = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--is-shallow-repository", *tips],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    lines = probe.stdout.split()
    if probe.returncode != 0 or len(lines) != 1 + len(tips):
        raise m.MapError(f"git cannot resolve {' and '.join(tips)}: "
                         f"{(probe.stderr.strip().splitlines() or ['no output'])[-1]}")
    if lines[0] == "true":
        return None
    shas = lines[1:]
    # Every flag below that restates a default is there because a config key can change it, and
    # the parse reads stdout as data: `log.showSignature` prints gpg text into it.
    out = subprocess.run(
        ["git", "-C", str(root), "-c", "core.quotePath=false", "log", "--topo-order",
         "--no-renames", "--no-show-signature", "--no-color", "--format=%x00%H %P", "--name-only",
         *shas, "--"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if out.returncode != 0:
        raise m.MapError(f"git log failed: {(out.stderr.strip().splitlines() or ['no output'])[-1]}")
    commits = []
    for chunk in out.stdout.split("\0")[1:]:
        head_line, _, body = chunk.partition("\n")
        sha, *parents = head_line.split()
        commits.append((sha, tuple(parents), tuple(p for p in body.splitlines() if p.strip())))
    if base is None:
        return commits, None
    # Topological order: a commit is reachable from a tip exactly when the tip is it, or a commit
    # already known reachable names it as a parent — one forward pass per tip, no graph walk.
    from_head, from_base = {shas[0]}, {shas[1]}
    for sha, parents, _ in commits:
        if sha in from_head:
            from_head.update(parents)
        if sha in from_base:
            from_base.update(parents)
    return [c for c in commits if c[0] in from_head], frozenset(from_head - from_base)


def render_stale_dossiers(scope: str, rows: list[dict] | None, *, as_json: bool) -> str:
    """The ``--stale-dossiers`` answer as text or as one JSON object, from the measured rows.

    ``rows`` is ``None`` for a shallow clone. ``of`` is every dossier with a commit of its own in
    whole-history scope, and the dossiers whose claimed paths the range touched in range scope; a
    dossier no commit carries is named in ``note`` and left out of ``of``. ``live`` is false for a
    shallow clone, and in whole-history scope when no commit touched any claimed path — a count
    over nothing touched is not a measurement. An untouched RANGE is a true empty answer."""
    whole = scope == "HEAD"
    notes: list[str] = []
    if rows is None:
        live, measured = False, []
        notes.append("the clone is shallow, so its history is cut and no dossier's ancestry can "
                     "be measured; fetch the full history (git fetch --unshallow)")
    else:
        uncommitted = sorted(r["feature"] for r in rows if r["refreshed"] is None
                             and (whole or r["touched"]))
        measured = [r for r in rows if r["refreshed"] is not None and (whole or r["touched"])]
        live = not whole or any(r["touched"] for r in rows)
        if not live:
            notes.append("no commit in the history touched any path a dossier claims")
        if uncommitted:
            notes.append("left out of `of`, no commit carries them yet: " + ", ".join(uncommitted))
    measured.sort(key=lambda r: (-r["behind"], r["feature"]))
    doc = {
        "scope": scope, "of": len(measured), "stale": sum(1 for r in measured if r["stale"]),
        "live": live, "note": "; ".join(notes),
        "dossiers": [{k: r[k] for k in ("feature", "dossier", "refreshed", "stale", "behind", "newest")}
                     for r in measured],
    }
    if as_json:
        return json.dumps(doc, indent=1)
    if not live:
        return f"# map-diff --stale-dossiers {scope}: DEAD PROBE - {doc['note']}"
    lines = [f"# map-diff --stale-dossiers {scope}: {doc['stale']} of {doc['of']} dossiers older "
             "than their paths (report only)"]
    lines += [f"- {r['feature']} · {r['dossier']} · {r['behind']} behind · newest {r['newest'][:8]}"
              for r in doc["dossiers"] if r["stale"]]
    if doc["note"]:
        lines.append(f"note: {doc['note']}")
    return "\n".join(lines)


def main() -> int:
    # `<kit>` resolved, so every command --help prints is copy-pasteable from the repo root at
    # whatever prefix this kit is installed at, not only at the default one.
    parser = argparse.ArgumentParser(description=__doc__.replace("<kit>", m.kit_rel()))
    parser.add_argument("range", nargs="*",
                        help="<base>..<head> or <base> <head>; optional with --stale-dossiers only")
    parser.add_argument("--verbose", action="store_true", help="full unmapped file list")
    parser.add_argument(
        "--drop-affordance-exempt",
        action="store_true",
        help="S4a: after attribution, drop every touched feature from the affordance-exempt list "
        "(shrink-only) so the next gate run demands its '## Reuse affordance' block",
    )
    parser.add_argument(
        "--stale-dossiers",
        action="store_true",
        help="list the feature dossiers older than their paths: a commit touching a claimed path "
        "is not an ancestor of the dossier's last commit. With no range, the whole history at HEAD; "
        "with <base>..<head>, the dossiers that range touched and did not refresh. Report only.",
    )
    parser.add_argument("--json", action="store_true", help="--stale-dossiers: one JSON object")
    args = parser.parse_args()

    if len(args.range) == 1 and ".." in args.range[0]:
        base, head = args.range[0].split("..", 1)
    elif len(args.range) == 2:
        base, head = args.range
    elif not args.range and args.stale_dossiers:
        base, head = None, "HEAD"
    else:
        parser.error("pass <base>..<head> or two refs")
        return 2

    # Refuse BEFORE any git call or artifact read: at a root that was never adopted the digest
    # reports every file UNMAPPED and --stale-dossiers would report every dossier fresh, both at
    # exit 0.
    try:
        m.require_adopted_root()
    except m.MapError as exc:
        print(f"map-diff refused: {exc}", file=sys.stderr)
        return 2

    if args.stale_dossiers:
        scope = "HEAD" if base is None else f"{base}..{head}"
        if base is not None:
            base = base or "HEAD"  # git's own spelling: an empty side of `..` is HEAD
        root = m.repo_root()
        rows = None
        try:
            read = read_commit_paths(root, base, head or "HEAD")
            if read is not None:
                import map_extractors as ext  # project layer — the claims need the inventory ids

                tree = m.load_map_tree(ext.inventory_ids(), root=root, decision_id_re=getattr(
                    ext, "DECISION_ID_RE", m.DEFAULT_DECISION_ID_RE))
                rows = m.measure_dossier_staleness(
                    read[0], tree, m.load_conf(root)["MAP_ROOT"],
                    keyed_attributors=getattr(ext, "KEYED_ATTRIBUTORS", ()), scope=read[1])
        except m.MapError as exc:
            print(f"map-diff: {exc}", file=sys.stderr)
            return 1
        print(render_stale_dossiers(scope, rows, as_json=args.json))
        return 0

    files = _changed_files(base, head)

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
