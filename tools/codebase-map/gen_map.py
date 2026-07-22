"""Generate / check / seed / scaffold the codebase-map artifacts (codebase-map kit).

Run from the ADOPTING repo's root:

    python codebase-map/gen_map.py --scaffold        # one-time: map tree + seeded baseline
    python codebase-map/gen_map.py --write           # (re)render generated/ to disk
    python codebase-map/gen_map.py --check           # byte-compare (LF-normalized); exit 1
    python codebase-map/gen_map.py --seed-baseline   # rewrite baseline.toml from unclaimed

Requires a filled codebase-map/map_extractors.py (the template refuses an empty EXTRACTORS).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import map_extractors as ext  # noqa: E402
import map_lib as m  # noqa: E402

IDS = ext.inventory_ids()
ID_RE = getattr(ext, "DECISION_ID_RE", m.DEFAULT_DECISION_ID_RE)

_FOUNDATION_SKELETON = """# foundation — the shared substrate (not a feature)

```toml
feature = "foundation"
title = "Foundation — shared substrate claimed outside any single feature"
status = "shipped"
streams = ["architecture"]
decisions = []

[claims]
{claims}
[paths]
globs = [
]
```

## Claim policy

Claim here only what is genuinely shared substrate (sanitization boundaries, shared transport
seams, ops tooling, the registries themselves). Feature-shaped items belong in
`features/<feature>.md` dossiers. Everything else waits in `baseline.toml` (shrink-only).
"""

_README = """# {map_root} — the self-verifying codebase map

Feature dossiers whose machine claims are CI-verified against live code inventories, a
generated system map, and a git-range digest. Kit: `codebase-map/` (coding-governance);
inventories: `codebase-map/map_extractors.py`; gate: see `.codebase-map.conf` GATE_FILE.

## Layout
- `FOUNDATION.md` — shared-substrate claims (same contract as a dossier).
- `baseline.toml` — shrink-only ratchet baseline (backfill inventory; never add new keys).
- `features/<feature>.md` — one dossier per feature: first ```toml fence = machine claims,
  then `## Constraints & why` · `## Shared seams` · `## Gaps` prose.
- `generated/` — `inventories.json` (keys-only) + `MAP.md` (claimant-annotated); regenerate
  with `python codebase-map/gen_map.py --write`, never hand-edit.

## How to claim (quickstart)
1. You add an inventoried moving part -> the gate fails naming the key.
2. Claim it in the owning dossier's toml fence (create the dossier from any existing one).
3. Shared substrate -> claim in `FOUNDATION.md` instead.
4. Claim edits stale `generated/MAP.md` -> run `python codebase-map/gen_map.py --write`
   in the same commit (`--check` to verify).
5. Digest any range: `{diff_cmd} <base>..<head>` (`--verbose` for files).

## Rules
- Claims are exact keys, gate-enforced BOTH directions (a claim naming a dead key fails too).
- Path globs are digest-only, never gated; overlap is legal (multi-claim >= 1 owner).
- Shared mega-modules are documented in dossiers' "Shared seams" prose, never glob-claimed.
- Substantial work touching an undossiered feature creates its dossier at design time.
"""


def _artifacts() -> dict[Path, str]:
    inventories = ext.all_inventories()
    tree = m.load_map_tree(IDS, decision_id_re=ID_RE)
    owners = m.owners_of(tree)
    gen_dir = m.map_root() / "generated"
    arts = {
        gen_dir / "inventories.json": m.render_inventories_json(inventories, IDS),
        gen_dir / "MAP.md": m.render_map_md(inventories, IDS, owners, tree.baseline),
    }
    # SYMBOL recall tier (optional): render symbols.json only when the project declares symbol
    # extractors and they yield symbols — an opted-out repo gets no artifact and no gate demand.
    symbols = getattr(ext, "all_symbols", list)()
    if symbols:
        arts[gen_dir / "symbols.json"] = m.render_symbols_json(symbols)
    return arts


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {path}")


def _seed_baseline() -> None:
    inventories = ext.all_inventories()
    tree = m.load_map_tree(IDS, decision_id_re=ID_RE)
    cov = m.compute_coverage(inventories, m.owners_of(tree), {k: () for k in IDS})
    _write(m.map_root() / "baseline.toml", m.render_baseline(cov.unclaimed, IDS))
    print(f"baseline: {sum(len(v) for v in cov.unclaimed.values())} unclaimed keys")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    for flag in ("--scaffold", "--write", "--check", "--seed-baseline"):
        mode.add_argument(flag, action="store_true")
    args = parser.parse_args()

    if args.scaffold:
        map_dir = m.map_root()
        if (map_dir / "FOUNDATION.md").is_file():
            print(
                f"{map_dir} already scaffolded — refusing to overwrite FOUNDATION.md.\n"
                "Resume a partial scaffold with: gen_map.py --seed-baseline && gen_map.py "
                "--write, then copy the gate template to GATE_FILE (or delete the map tree "
                "and re-run --scaffold)."
            )
            return 1
        # Run every extractor BEFORE the first write: the most likely first-run error is an
        # extractor raising on a wrong path, and it must leave ZERO state behind (a half
        # tree wedges the re-run on the refusal above).
        ext.all_inventories()
        claims = "\n".join(f"{inv_id} = []" for inv_id in IDS)
        conf = m.load_conf()
        _write(map_dir / "FOUNDATION.md", _FOUNDATION_SKELETON.format(claims=claims))
        _write(
            map_dir / "README.md",
            _README.format(
                map_root=conf["MAP_ROOT"],
                diff_cmd=conf.get("MAP_DIFF_CMD") or "python codebase-map/map_diff.py",
            ),
        )
        (map_dir / "features").mkdir(parents=True, exist_ok=True)
        _seed_baseline()
        for path, content in _artifacts().items():
            _write(path, content)
        print("scaffolded — next: copy the gate template to GATE_FILE and run it")
        return 0

    if args.seed_baseline:
        _seed_baseline()
        return 0

    stale = False
    for path, fresh in _artifacts().items():
        if args.write:
            _write(path, fresh)
        else:
            committed = m.lf(path.read_text(encoding="utf-8")) if path.is_file() else ""
            if committed != fresh:
                print(f"STALE: {path} — regen: {m.REGEN_CMD}")
                stale = True
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
